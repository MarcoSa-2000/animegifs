class CategoryIntegral(Exception):
    """
    Category can't be an integral, only a string.
    You can check valid categories at: https://github.com/MarcoSa-2000/animegifs
    """

    def __init__(self, category, error="Category can't be an integral."):
        self.category = category
        self.error = error
        super().__init__(self.error)

class CategoryError(Exception):
    """
    Not a valid category. Category must be a string.
    You can check valid categories at: https://github.com/MarcoSa-2000/animegifs
    """

    def __init__(self, category, error="Not a valid category."):
        self.category = category
        self.error = error
        super().__init__(self.error)

class CategoryUnknown(Exception):
    """
    This is a not handled error, probably the category type is neither an int nor a str.
    Make sure to check category is a string and is a valid category.
    You can check valid categories at: https://github.com/MarcoSa-2000/animegifs
    """

    def __init__(self, category, error="Not a valid category."):
        self.category = category
        self.error = error
        super().__init__(self.error)

class MethodNotUpdated(Exception):
    """
    The method for get the gif's <title, mal link, mal id> is not yet supported for that gif url.
    Usually means is just in work in progress and will be available soon.
    """

    def __init__(self, gif, error="Method not yet available for this gif."):
        self.gif = gif
        self.error = error
        super().__init__(self.error)

class AuthTimeout(Exception):
    """
    Authentication request timed out. Probably status 504 on server side. Check your connection too.
    """

    def __init__(self, exc, error="Authentication request timed out."):
        self.exc = exc
        self.error = error
        super().__init__(self.error)

class AuthError(Exception):
    """
    Authentication request returned an error. Probably status error 4xx.
    It will be resolved soon, if it persist,
    issue an issue on https://github.com/MarcoSa-2000/animegifs/issues.
    """

    def __init__(self, exc, error="Authentication request returned an error."):
        self.exc = exc
        self.error = error
        super().__init__(self.error)
