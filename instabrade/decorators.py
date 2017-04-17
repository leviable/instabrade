from __future__ import absolute_import

from functools import wraps


def verify_on_page(func):
    @wraps(func)
    def inner(obj, *args, **kwargs):
        obj.assert_on_page()

        return func(obj, *args, **kwargs)

    return inner
