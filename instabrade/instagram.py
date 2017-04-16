from instabrade.landing_page import LandingPage


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
        self.landing_page = LandingPage(self.driver)

        if load_webpage:
            self.driver.get('http://www.instagram.com')
