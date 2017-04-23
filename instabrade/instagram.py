from __future__ import absolute_import

from explicit import waiter, XPATH
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.common.exceptions import (
    StaleElementReferenceException,
    WebDriverException
)

from instabrade.log_in_page import LogInPage
from instabrade.home_page import HomePage

CENTER_POPUP_CLOSE_XPATH = '//div[@id="fb-root"]/preceding-sibling::div//button'
CENTER_POPUP_DISPLAYED_XPATH = '//div[@id="fb-root"]/preceding-sibling::div'
FOOTER_POPUP_CLOSE_XPATH = ('//span[contains(@class, "coreSpriteAppIcon")]/../../'
                            '../../following-sibling::span')
FOOTER_POPUP_DISPLAYED_CSS = 'span.coreSpriteAppIcon'


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

    def app_store_center_popup_close(self):
        """ Clicks the popup 'x' to close it """
        elem = waiter.find_element(self.driver, CENTER_POPUP_CLOSE_XPATH, XPATH)
        elem.click()

        Wait(None, 30).until(EC.staleness_of(elem))

    @property
    def app_store_center_popup_displayed(self):
        """ Returns True if the center screen app store popup is displayed
            False if not

        Returns:
            Bool
        """
        # Example: http://i.imgur.com/QmhZzix.png
        popup_elems = self.driver.find_elements_by_xpath(CENTER_POPUP_DISPLAYED_XPATH)
        return len(popup_elems) > 0

    def app_store_footer_popup_close(self):
        """ Clicks the popup 'x' to close it """
        elem = waiter.find_element(self.driver, FOOTER_POPUP_CLOSE_XPATH, XPATH)
        elem.click()

        Wait(None, 30).until(EC.staleness_of(elem))

    @property
    def app_store_footer_popup_displayed(self):
        """ Returns True if the app store footer popup is displayed
            False if not

        Returns:
            Bool
        """
        # Example: http://i.imgur.com/PxnJASh.png
        # This one is tricky. The footer popup is added to the DOM, but positioned
        # off screen, below the viewable area. After several seconds, the elements
        # location is slowly changed so that the footer slides up into the viewable
        # area. We need to check that the popup's location has a 'y' value that is
        # less than the current window size

        # Get the y component of the window size
        js = "return document.documentElement.clientHeight"
        window_y_coord = self.driver.execute_script(js)

        elems = self.driver.find_elements_by_css_selector(FOOTER_POPUP_DISPLAYED_CSS)
        try:
            if not elems or not elems[0].is_displayed():
                result = False
            else:
                result = elems[0].location['y'] < window_y_coord
        except StaleElementReferenceException:
            result = False

        return result

    def close_popups(self):
        """ Wait for the two App Store popups to display, and close them

        Returns:
            None
        """
        # Wait for the footer popup to load, then close it
        Wait(self, 30).until(lambda obj: obj.app_store_footer_popup_displayed)
        try:
            self.app_store_footer_popup_close()
        except WebDriverException as exc:
            if "Other element would receive the click" not in str(exc):
                raise

            # This happens when the center screen app store popup is displayed
            # This only happens with some accounts
            # Close it then retry closing the footer
            Wait(self, 30).until(lambda obj: obj.app_store_center_popup_displayed)
            self.app_store_center_popup_close()

            self.app_store_footer_popup_close()

    def scroll_to_bottom(self):
        """ Scroll to the bottom of the current window """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_center(self):
        """ Scroll to the center of the current window """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

    def scroll_to_top(self):
        """ Scroll to the bottom of the current window """
        self.driver.execute_script("window.scrollTo(0, 0);")
