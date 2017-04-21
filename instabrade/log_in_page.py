from __future__ import absolute_import

from explicit import waiter, NAME, XPATH
from selenium.webdriver.support.wait import WebDriverWait as Wait

from instabrade.base import InstagramBase
from instabrade import LOG_IN_IDENTIFIER
from instabrade.decorators import verify_on_page

LOG_IN_LINK_XPATH = ('//h1[contains(@class, "coreSpriteLoggedOutWordmark")]/'
                     'parent::div/following-sibling::div/p/a')
LOG_IN_FIELDS_DISPLAYED_XPATH = (
    '//h1[contains(@class, "coreSpriteLoggedOutWordmark")]'
    '/following-sibling::div/form/div'
)
LOG_IN_BUTTON_XPATH = '//input[@name="password"]/parent::div/following-sibling::span/button'


class LogInPage(InstagramBase):
    """ Page object for the page you see when you are not logged in and
        go to www.instagram.com
    """
    PAGE_IDENTIFIER = LOG_IN_IDENTIFIER

    @property
    @verify_on_page
    def log_in_fields_displayed(self):
        """ Returns True if the log in fields are displayed, False if not

        Returns:
            bool
        """
        # Insta uses similar names for both the login and register fields. Use an
        # XPATH that can locate the divs at that level, and count them. The log
        # in fields only have two div elements
        found_elems = waiter.find_elements(
            self.driver, LOG_IN_FIELDS_DISPLAYED_XPATH, XPATH)
        return len(found_elems) == 2

    @verify_on_page
    def log_in_link_click(self, wait_until_displayed=True):
        """ Click the `log in` link on the log in page
        Args:
            wait_until_displayed (bool): Block until all the log in fields are
                                         displayed

        Returns:
            None

        Raises:
            TimeoutException: Raised if the link isn't found, and if the fields
                              aren't displayed
        """
        waiter.find_element(self.driver, LOG_IN_LINK_XPATH, XPATH).click()

        if wait_until_displayed:
            Wait(self, 30).until(lambda obj: obj.log_in_fields_displayed)

    @verify_on_page
    def log_in_button_click(self):
        """ Clicks the log in button """
        waiter.find_element(self.driver, LOG_IN_BUTTON_XPATH, by=XPATH).click()

    @property
    @verify_on_page
    def log_in_password(self):
        """ Returns the current text in the password field

        Returns:
            str
        """
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
        """ Returns the current text in the username field

        Returns:
            str
        """
        username_elem = waiter.find_element(self.driver, 'username', by=NAME)
        return username_elem.get_attribute('value')

    @log_in_username.setter
    @verify_on_page
    def log_in_username(self, username):
        """ Sets the text in the username field to `username` """
        waiter.find_write(self.driver, 'username', username, by=NAME)
