from __future__ import absolute_import

import six
from abc import ABCMeta, abstractmethod

from explicit import waiter
from selenium.common.exceptions import TimeoutException

from instabrade.exceptions import PageDetectionError, WrongPageError
from instabrade import (
    HOME_IDENTIFIER,
    LOG_IN_IDENTIFIER
)


@six.add_metaclass(ABCMeta)
class InstagramBase():
    """ Base object for all Instagram pages """
    def __init__(self, driver):
        self.driver = driver

    def _current_page(self):
        """ Determine which Instagram page is currently loaded by
            finding elements unique to that page
        """
        page_types = [
            HOME_IDENTIFIER,
            LOG_IN_IDENTIFIER,
        ]

        page_elem = waiter.find_one(self.driver, [p.css_path for p in page_types])

        # Get all attributs for this element
        attr_script = '''var items = {};
                         attrs = arguments[0].attributes
                         for (i = 0; i < attrs.length; ++i)
                         { items[attrs[i].name] = attrs[i].value };
                         return items;
                      '''
        attrs = self.driver.execute_script(attr_script, page_elem)

        # Determine page
        for pt in page_types:
            if pt.attr_value in attrs.get(pt.attr, ''):
                return pt
        else:  # pylint: disable=W0120
            msg = ("Could not determine page from element: {0}\n"
                   "Using element {1}")
            raise PageDetectionError(msg.format(page_elem, attrs))

    def assert_on_page(self):
        """ Raises a WrongPageError if anything other than the expected
            page is loaded
        """
        try:
            current_page_identifier = self._current_page()
        except TimeoutException:
            exc_msg = ("Currently on an unknown page. Expected to be on\n{0}\n"
                       "but currently on\n{1}")
            raise WrongPageError(exc_msg.format(self.PAGE_IDENTIFIER,
                                                self.driver.current_url))

        if current_page_identifier is not self.PAGE_IDENTIFIER:
            exc_msg = "Wrong page loaded. Expected\n{0}\nbut found\n{1}"
            raise WrongPageError(exc_msg.format(self.PAGE_IDENTIFIER,
                                                current_page_identifier))

    @property
    @abstractmethod
    def PAGE_IDENTIFIER(self):
        """ Any objects that inherit from InstagramBase must assign
            a PAGE_IDENTIFIER property
        """
        pass  # pragma: no cover
