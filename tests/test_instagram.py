try:
    import mock
except ImportError:
    from unittest import mock

from instabrade import Instagram, PageID
from instabrade.log_in_page import LogInPage


def test___init__(driver):
    """ Verify Instagram object accepts webdriver as first arg """
    ig = Instagram(driver)

    assert ig.driver is driver
    assert mock.call.get('http://www.instagram.com') in driver.method_calls

    # Validate pages are instantiated
    assert isinstance(ig.log_in_page, LogInPage)
    assert hasattr(ig.log_in_page, 'PAGE_IDENTIFIER')
    assert isinstance(ig.log_in_page.PAGE_IDENTIFIER, PageID)


def test___init___no_default(driver):
    """ Verify Instagram object accepts bool as second arg """
    ig = Instagram(driver, False)

    assert ig.driver is driver
    assert mock.call.get('http://www.instagram.com') not in driver.method_calls
