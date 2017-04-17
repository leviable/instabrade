from __future__ import absolute_import

from explicit import waiter, NAME, XPATH

from instabrade.base import InstagramBase
from instabrade import LOG_IN_IDENTIFIER
from instabrade.decorators import verify_on_page

LOG_IN_LINK_XPATH = ('//h1[contains(@class, "coreSpriteLoggedOutWordmark")]/'
                     'parent::div/following-sibling::div/p/a')
LOG_IN_BUTTON_XPATH = '//input[@name="password"]/parent::div/following-sibling::span/button'


class LogInPage(InstagramBase):
    """ Page object for the page you see when you are not logged in and
        go to www.instagram.com
    """
    PAGE_IDENTIFIER = LOG_IN_IDENTIFIER

    @verify_on_page
    def log_in_link_click(self):
        """ Click the `log in` link on the log in page """
        waiter.find_element(self.driver, LOG_IN_LINK_XPATH, XPATH).click()

    @verify_on_page
    def log_in_button_click(self):
        """ Clicks the log in button """
        waiter.find_element(self.driver, LOG_IN_BUTTON_XPATH, by=XPATH).click()

    @property
    @verify_on_page
    def log_in_password(self):
        """ Returns the current text in the password field """
        password_elem = waiter.find_element(self.driver, 'password', by=NAME)
        return password_elem.get_attribute('value')

    @log_in_password.setter
    @verify_on_page
    def log_in_password(self, password):
        """ Sets the text in the password field to `password` """
        waiter.find_write(self.driver, 'password', password, by=NAME)

    @property
    @verify_on_page
    def log_in_username(self):
        """ Returns the current text in the username field """
        username_elem = waiter.find_element(self.driver, 'username', by=NAME)
        return username_elem.get_attribute('value')

    @log_in_username.setter
    @verify_on_page
    def log_in_username(self, username):
        """ Sets the text in the username field to `username` """
        waiter.find_write(self.driver, 'username', username, by=NAME)
