from __future__ import absolute_import

from explicit import waiter

from instabrade import HOME_IDENTIFIER
from instabrade.base import InstagramBase
from instabrade.decorators import verify_on_page


class HomePage(InstagramBase):
    """ Page object for the Instagram Home page """
    PAGE_IDENTIFIER = HOME_IDENTIFIER

    @property
    @verify_on_page
    def post_count(self):
        """ Returns the number of currently on the screen

        Returns:
            post count (int): Number of posts currently on screen
        """
        css_path = "main > section > div > div > article"
        return len(waiter.find_elements(self.driver, css_path))
