import os

from selenium import webdriver

from instabrade import Instagram


def main():
    driver = webdriver.Chrome()
    try:
        # Instantiate object
        ig = Instagram(driver)

        # Log in
        ig.log_in_page.log_in_link_click(wait_until_displayed=True)
        ig.log_in_page.log_in_username = os.environ['INSTA_USERNAME']
        ig.log_in_page.log_in_password = os.environ['INSTA_PASSWORD']
        ig.log_in_page.log_in_button_click()

        # Close the two App Store Popups
        ig.close_popups()

    finally:
        driver.quit()

if __name__ == '__main__':
    main()
