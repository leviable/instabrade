try:
    import mock
except ImportError:
    from unittest import mock

from explicit import XPATH

from instabrade.log_in_page import (
    LOG_IN_LINK_XPATH,
    LOG_IN_BUTTON_XPATH,
    LOG_IN_FIELDS_DISPLAYED_XPATH,
)


def test_post_count(instagram, element):
    """ Verify post count prop returns an int """
    expected_count = 5
    instagram.driver.find_elements.return_value = [element] * 5

    actual_count = instagram.home_page.post_count
    assert isinstance(actual_count, int)
    assert expected_count == actual_count
