try:
    import mock
except ImportError:
    from unittest import mock

import pytest
from selenium.common.exceptions import (
    StaleElementReferenceException as SERE,
    WebDriverException
)

from instabrade import Instagram, PageID
from instabrade.log_in_page import LogInPage
from instabrade.instagram import (
    CENTER_POPUP_CLOSE_XPATH,
    CENTER_POPUP_DISPLAYED_XPATH,
    FOOTER_POPUP_CLOSE_XPATH,
)

call = mock.call
patch = mock.patch
PropertyMock = mock.PropertyMock


def test___init__(driver):
    """ Verify Instagram object accepts webdriver as first arg """
    ig = Instagram(driver)

    assert ig.driver is driver
    assert call.get('http://www.instagram.com') in driver.method_calls

    # Validate pages are instantiated
    assert isinstance(ig.log_in_page, LogInPage)
    assert hasattr(ig.log_in_page, 'PAGE_IDENTIFIER')
    assert isinstance(ig.log_in_page.PAGE_IDENTIFIER, PageID)


def test___init___no_default(driver):
    """ Verify Instagram object accepts bool as second arg """
    ig = Instagram(driver, False)

    assert ig.driver is driver
    assert call.get('http://www.instagram.com') not in driver.method_calls


def test_app_store_center_popup_close(instagram, element):
    """ Verify the center app store popup can be closed """
    instagram.driver.find_element.return_value = element
    element.is_enabled.side_effect = [None, SERE]

    instagram.app_store_center_popup_close()

    exp_driver_call = call.find_element('xpath', CENTER_POPUP_CLOSE_XPATH)
    assert exp_driver_call in instagram.driver.method_calls
    exp_elem_calls = [call.click(), call.is_enabled(), call.is_enabled()]
    assert exp_elem_calls == element.method_calls


def test_app_store_center_popup_displayed(instagram):
    """ Verify the center app store popup display check works """
    instagram.driver.find_elements_by_xpath.side_effect = [[], [1, 2]]

    assert instagram.app_store_center_popup_displayed is False
    assert instagram.app_store_center_popup_displayed is True

    exp_call = call.find_elements_by_xpath(CENTER_POPUP_DISPLAYED_XPATH)
    assert exp_call in instagram.driver.method_calls


def test_app_store_footer_popup_close(instagram, element):
    """ Verify the footer app store popup can be closed """
    instagram.driver.find_element.return_value = element
    element.is_enabled.side_effect = [None, SERE]

    instagram.app_store_footer_popup_close()

    exp_driver_call = call.find_element('xpath', FOOTER_POPUP_CLOSE_XPATH)
    assert exp_driver_call in instagram.driver.method_calls
    exp_elem_calls = [call.click(), call.is_enabled(), call.is_enabled()]
    assert exp_elem_calls == element.method_calls


def test_app_store_footer_popup_displayed(instagram, element):
    """ Verify footer popup detection works """
    instagram.driver.execute_script.return_value = 100

    side_effects = [[], [element, ], [element, ], [element, ]]
    instagram.driver.find_elements_by_css_selector.side_effect = side_effects

    element.is_displayed.side_effect = [False, True, True, True]

    loc_side_effect = [SERE, {'y': 110}, {'y': 90}]
    type(element).location = PropertyMock(side_effect=loc_side_effect)

    instagram.app_store_footer_popup_displayed is False
    instagram.app_store_footer_popup_displayed is False
    instagram.app_store_footer_popup_displayed is False
    instagram.app_store_footer_popup_displayed is True


def test_close_popups(instagram):
    """ Test the popup closing functionality """
    with patch.object(instagram, 'app_store_center_popup_close') as cc_mock:
        with patch.object(instagram, 'app_store_footer_popup_close') as fc_mock:
            cd_prop = PropertyMock(side_effect=[False, True])
            type(instagram).app_store_center_popup_displayed = cd_prop

            fd_prop = PropertyMock(side_effect=[False, True])
            type(instagram).app_store_footer_popup_displayed = fd_prop

            exc_text = "Other element would receive the click"
            fc_mock.side_effect = [WebDriverException(exc_text), None]

            instagram.close_popups()

            assert cc_mock.call_args_list == [call()]
            assert fc_mock.call_args_list == [call(), call()]
            assert cd_prop.call_args_list == [call(), call()]
            assert fd_prop.call_args_list == [call(), call()]


def test_close_popups_exception(instagram):
    """ Test the popup closing reraises exception """
    with patch.object(instagram, 'app_store_center_popup_close'):
        with patch.object(instagram, 'app_store_footer_popup_close') as fc_mock:
            cd_prop = PropertyMock(side_effect=[False, True])
            type(instagram).app_store_center_popup_displayed = cd_prop

            fd_prop = PropertyMock(side_effect=[False, True])
            type(instagram).app_store_footer_popup_displayed = fd_prop

            exc_text = "Not the expected text"
            fc_mock.side_effect = [WebDriverException(exc_text), None]

            with pytest.raises(WebDriverException):
                instagram.close_popups()


def test_scroll_to_bottom(instagram):
    """ Test the scroll_to_bottom method call """
    instagram.scroll_to_bottom()

    assert instagram.driver.execute_script.called
    assert "0, document.body.scrollHeight" in str(instagram.driver.execute_script.call_args)


def test_scroll_to_center(instagram):
    """ Test the scroll_to_center method call """
    instagram.scroll_to_center()

    assert instagram.driver.execute_script.called
    assert "0, document.body.scrollHeight/2" in str(instagram.driver.execute_script.call_args)


def test_scroll_to_top(instagram):
    """ Test the scroll_to_top method call """
    instagram.scroll_to_top()

    assert instagram.driver.execute_script.called
    assert "scrollTo(0, 0)" in str(instagram.driver.execute_script.call_args)
