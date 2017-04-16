try:
    import mock
except ImportError:
    from unittest import mock

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    """ Returns a mock selenium driver object """
    return mock.create_autospec(webdriver.Firefox)
