
Instabrade
==========

|PyPIVersion| |TravisCI| |CoverageStatus| |CodeHealth| |PythonVersions| |Gitter|

Selenium based Instagram scraper

Note that is project is currently in alpha: APIs can and will change without warning.

.. |TravisCI| image:: https://travis-ci.org/levi-rs/instabrade.svg?branch=master
    :target: https://travis-ci.org/levi-rs/instabrade
.. |CoverageStatus| image:: https://coveralls.io/repos/github/levi-rs/instabrade/badge.svg
   :target: https://coveralls.io/github/levi-rs/instabrade
.. |CodeHealth| image:: https://landscape.io/github/levi-rs/instabrade/master/landscape.svg?style=flat
   :target: https://landscape.io/github/levi-rs/instabrade/master
.. |PyPIVersion| image:: https://badge.fury.io/py/instabrade.svg
    :target: https://badge.fury.io/py/instabrade
.. |PythonVersions| image:: https://img.shields.io/pypi/pyversions/instabrade.svg
    :target: https://wiki.python.org/moin/Python2orPython3
.. |Gitter| image:: https://badges.gitter.im/levi-rs/instabrade.svg
    :alt: Join the chat at https://gitter.im/levi-rs/instabrade
    :target: https://gitter.im/levi-rs/instabrade?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge


Currently support functionality:

- Log into Instagram
- Handle the mobile app related popups


Planned functionality in upcoming release(s):

- Return all posts from Home page


Example usage:

.. code-block:: python

    from selenium import webdriver

    from instabrade import Instagram

    my_username = "my username"
    my_password = "my password"

    driver = webdriver.Chrome()

    try:
        # Instantiate the object
        # - This also loads instagram's URL
        ig = Instagram(driver)

        # Click the "Log in" link to display the login fields
        ig.log_in_page.log_in_link_click()

        # Fill in the username and password fields
        ig.log_in_page.log_in_username = my_username
        ig.log_in_page.log_in_password = my_password

        # Click the Log In button
        ig.log_in_page.log_in_button_click()

    finally:
        driver.quit()

Instabrade is page-aware. If you attempt to interact with a property or method
for a page that isn't currently loaded, a WrongPageError exception will get
thrown:

.. code-block:: shell

    In [1]: from selenium import webdriver

    In [2]: from instabrade import Instagram

    In [3]: driver = webdriver.Chrome()

    In [4]: ig = Instagram(driver)

    In [5]: ig.log_in_page.log_in_link_click()

    In [6]: ig.log_in_page.log_in_username = my_username

    In [7]: ig.log_in_page.log_in_password = my_password

    In [8]: ig.log_in_page.log_in_button_click()

    In [9]: ig.log_in_page.log_in_username = my_username
    ---------------------------------------------------------------------------
    WrongPageError                            Traceback (most recent call last)
    <ipython-input-9-eb1e96eabcf5> in <module>()
    ----> 1 ig.log_in_page.log_in_username = my_username

    /Users/levi/workspace/instabrade/instabrade/decorators.py in inner(obj, *args, **kwargs)
        7     @wraps(func)
        8     def inner(obj, *args, **kwargs):
    ----> 9         obj.assert_on_page()
        10
        11         return func(obj, *args, **kwargs)

    /Users/levi/workspace/instabrade/instabrade/base.py in assert_on_page(self)
        64             exc_msg = "Wrong page loaded. Expected {0} but found {1}"
        65             raise WrongPageError(exc_msg.format(self.PAGE_IDENTIFIER,
    ---> 66                                                 current_page_identifier))
        67
        68     @property

    WrongPageError: Wrong page loaded. Expected
    PageID(name='Log In Page Identifier', css_path='h1.coreSpriteLoggedOutWordmark', attr='class', attr_value='coreSpriteLoggedOutWordmark')
    but found
    PageID(name='Home Page Identifier', css_path='main[role="main"] > section a[href$="explore/"]', attr='href', attr_value='/explore/')

    In [10]:
