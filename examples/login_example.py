import os

from selenium import webdriver

from instabrade import Instagram


def log_in(instagram):
    # Log in
    instagram.log_in_page.log_in_link_click(wait_until_displayed=True)
    instagram.log_in_page.log_in_username = os.environ['INSTA_USERNAME']
    instagram.log_in_page.log_in_password = os.environ['INSTA_PASSWORD']
    instagram.log_in_page.log_in_button_click()

    # Should be on the Home Page now
    instagram.home_page.assert_on_page()


def main():
    driver = webdriver.Chrome()
    try:
        log_in(Instagram(driver))
    finally:
        driver.quit()


if __name__ == '__main__':
    main()
