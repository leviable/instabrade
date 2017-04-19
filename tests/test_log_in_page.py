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


def test_log_in_link_click(instagram, element):
    """ Verify log in page log_in_link_click method works """
    instagram.driver.find_element.return_value = element
    instagram.log_in_page.log_in_link_click(False)

    assert mock.call.find_element(XPATH, LOG_IN_LINK_XPATH) in instagram.driver.method_calls
    assert mock.call.click() in element.method_calls


def test_log_in_link_click_with_wait(instagram, element):
    """ Verify log in page log_in_link_click method works and waits"""
    instagram.driver.find_element.return_value = element
    instagram.driver.find_elements.return_value = (1, 2)
    instagram.log_in_page.log_in_link_click(True)

    call_1 = mock.call.find_element(XPATH, LOG_IN_LINK_XPATH)
    assert call_1 in instagram.driver.method_calls
    assert mock.call.click() in element.method_calls

    call_2 = mock.call.find_elements(XPATH, LOG_IN_FIELDS_DISPLAYED_XPATH)
    assert call_2 in instagram.driver.method_calls


def test_log_in_button_click(instagram, element):
    """ Verify log in page log_in_button_click method works """
    instagram.driver.find_element.return_value = element
    instagram.log_in_page.log_in_button_click()

    assert mock.call.find_element(XPATH, LOG_IN_BUTTON_XPATH) in instagram.driver.method_calls
    assert mock.call.click() in element.method_calls


def test_log_in_password_read(instagram, element):
    """ Verify log in page password field read works """
    exp_password = 'mock password value read'
    element.get_attribute.return_value = exp_password
    instagram.driver.find_element.return_value = element
    assert exp_password == instagram.log_in_page.log_in_password


def test_log_in_password_write(instagram, element):
    """ Verify log in page password field write works """
    exp_password = 'mock password value write'
    instagram.driver.find_element.return_value = element
    instagram.log_in_page.log_in_password = exp_password

    assert element.method_calls == [mock.call.clear(),
                                    mock.call.send_keys(exp_password)]


def test_log_in_username_read(instagram, element):
    """ Verify log in page username field read works """
    exp_username = 'mock username value read'
    element.get_attribute.return_value = exp_username
    instagram.driver.find_element.return_value = element
    assert exp_username == instagram.log_in_page.log_in_username


def test_log_in_username_write(instagram, element):
    """ Verify log in page username field write works """
    exp_username = 'mock username value write'
    instagram.driver.find_element.return_value = element
    instagram.log_in_page.log_in_username = exp_username

    assert element.method_calls == [mock.call.clear(),
                                    mock.call.send_keys(exp_username)]
