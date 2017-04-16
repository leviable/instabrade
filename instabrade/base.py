import six
from collections import namedtuple

from abc import ABCMeta, abstractmethod

PageID = namedtuple("PageID", "name css_path attr attr_value")


@six.add_metaclass(ABCMeta)
class InstagramBase():
    """ Base object for all Instagram pages """
    def __init__(self, driver):
        self.driver = driver

    @property
    @abstractmethod
    def PAGE_IDENTIFIER(self):
        """ Any objects that inherit from InstagramBase must assign
            a PAGE_IDENTIFIER property
        """
        pass  # pragma: no cover
