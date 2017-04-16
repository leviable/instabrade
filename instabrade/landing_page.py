from instabrade.base import InstagramBase, PageID


class LandingPage(InstagramBase):
    """ Page object for the page you see when you are not logged in and
        go to www.instagram.com
    """
    PAGE_IDENTIFIER = PageID(name="Landing Page Identifier",
                             css_path="h1.coreSpriteLoggedOutWordmark",
                             attr="class",
                             attr_value="coreSpriteLoggedOutWordmark")
