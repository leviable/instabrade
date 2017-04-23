from __future__ import print_function

from selenium import webdriver

from instabrade import Instagram
from login_example import log_in


def get_posts(instagram):
    # Confirm we are on the homepage
    instagram.home_page.assert_on_page()

    # Close the two App Store Popups
    instagram.close_popups()

    # Show the current post count
    print(instagram.home_page.post_count)  # Should be ~11

    # Load at least 100 posts
    while instagram.home_page.post_count < 100:
        instagram.scroll_to_bottom()  # Hit the infinit scroll trigger

    # Show the current post count
    print(instagram.home_page.post_count)  # Should be > 100


def main():
    driver = webdriver.Chrome()
    try:
        instagram = Instagram(driver)
        log_in(instagram)
        get_posts(instagram)
    finally:
        driver.quit()


if __name__ == '__main__':
    main()
