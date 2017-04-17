from __future__ import absolute_import

from instabrade.log_in_page import LogInPage
from instabrade.home_page import HomePage


class Instagram(object):
    """ Primary Instagram page object class """
    def __init__(self, driver, load_webpage=True):
        """ Instagram init method

        Args:
            driver (webdriver): Selenium webdriver object
            load_webpage (bool): Load instagram.com into the webdriver browser

        Returns:
            None
        """
        self.driver = driver
        self.log_in_page = LogInPage(self.driver)
        self.home_page = HomePage(self.driver)

        if load_webpage:
            self.driver.get('http://www.instagram.com')
