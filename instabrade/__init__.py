from __future__ import absolute_import

from collections import namedtuple

from pbr.version import VersionInfo

__version__ = VersionInfo('instabrade').semantic_version().release_string()

PageID = namedtuple("PageID", "name css_path attr attr_value")

LOG_IN_IDENTIFIER = PageID(name='Log In Page Identifier',
                           css_path='h1.coreSpriteLoggedOutWordmark',
                           attr='class',
                           attr_value='coreSpriteLoggedOutWordmark')

HOME_IDENTIFIER = PageID(name='Home Page Identifier',
                         css_path='main[role="main"] > section a[href$="explore/"]',
                         attr='href',
                         attr_value='/explore/')

from instabrade.instagram import Instagram  # noqa
