class InstabradeError(Exception):
    """ Base exception for all Instabrade exceptions"""
    pass


class PageDetectionError(InstabradeError):
    """ Error determining the currently loaded page """
    pass


class WrongPageError(InstabradeError):
    """ The wronge page is currently loaded """
    pass
