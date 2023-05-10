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
