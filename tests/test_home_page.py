try:
    import mock
except ImportError:
    from unittest import mock  # NOQA


def test_post_count(instagram, element):
    """ Verify post count prop returns an int """
    expected_count = 5
    instagram.driver.find_elements.return_value = [element] * 5

    actual_count = instagram.home_page.post_count
    assert isinstance(actual_count, int)
    assert expected_count == actual_count
