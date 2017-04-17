try:
    import mock
except ImportError:
    from unittest import mock

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from instabrade import Instagram


@pytest.fixture(scope="function")
def element():
    ''' Returns a mock selenium element object '''
    return mock.create_autospec(WebElement)


@pytest.fixture(scope="function")
def driver():
    """ Returns a mock selenium driver object """
    return mock.create_autospec(webdriver.Firefox)


@pytest.fixture(scope="function")
def instagram_full(driver):
    """ Returns an complete Instagram instance object """
    return Instagram(driver)


@pytest.fixture(scope="function")
def instagram(driver):
    """ Returns an Instagram instance object with assert_on_page patched out """
    with mock.patch('instabrade.base.InstagramBase.assert_on_page'):
        yield Instagram(driver)
