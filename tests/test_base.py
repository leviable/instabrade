try:
    import mock
except ImportError:
    from unittest import mock

import pytest
from selenium.common.exceptions import TimeoutException

from instabrade import LOG_IN_IDENTIFIER
from instabrade.exceptions import PageDetectionError, WrongPageError


def test_verify_on_page(instagram_full, element):
    """ Verify the verify_on_page decorator works """
    page_list = [
        [],           # Home Page
        [element, ],  # Log in page
    ]

    find_click_elem = [element, ]
    side_effects = page_list + find_click_elem
    instagram_full.driver.find_elements_by_css_selector.side_effect = side_effects
    attrs = {'class': "coreSpriteLoggedOutWordmark"}
    instagram_full.driver.execute_script.return_value = attrs

    instagram_full.log_in_page.log_in_link_click(False)

    page_call = mock.call.find_elements_by_css_selector(LOG_IN_IDENTIFIER.css_path)
    assert page_call in instagram_full.driver.method_calls
    assert instagram_full.driver.execute_script.called


def test_verify_on_page_exception_01(instagram_full, element):
    """ Verify _current_page raises a PageDetectionError """
    page_list = [
        [],           # Home Page
        [element, ],  # Log in page
    ]

    find_click_elem = [element, ]
    side_effects = page_list + find_click_elem
    instagram_full.driver.find_elements_by_css_selector.side_effect = side_effects

    attrs = {'class': "this doesnt exist"}
    instagram_full.driver.execute_script.return_value = attrs

    with pytest.raises(PageDetectionError):
        instagram_full.log_in_page.log_in_link_click()


def test_verify_on_page_exception_02(instagram_full, element):
    """ Verify assert_on_page raises a WrongPageError """
    instagram_full.driver.find_elements_by_css_selector.side_effect = TimeoutException

    with pytest.raises(WrongPageError) as exc:
        instagram_full.log_in_page.log_in_link_click()

    assert "Currently on an unknown page" in str(exc)


def test_verify_on_page_exception_03(instagram_full, element):
    """ Verify assert_on_page raises a WrongPageError """
    page_list = [
        [element, ],  # Home Page
        [],           # Log in page
    ]

    find_click_elem = [element, ]
    side_effects = page_list + find_click_elem
    instagram_full.driver.find_elements_by_css_selector.side_effect = side_effects
    attrs = {'href': "https://www.instagram.com/explore/"}
    instagram_full.driver.execute_script.return_value = attrs

    with pytest.raises(WrongPageError) as exc:
        instagram_full.log_in_page.log_in_link_click()

    assert "Wrong page loaded" in str(exc)
