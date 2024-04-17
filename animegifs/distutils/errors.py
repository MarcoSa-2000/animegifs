class CategoryError(Exception):
    """
    Not a valid category. Category must be an existent category and a string.
    You can check valid categories at: https://github.com/MarcoSa-2000/animegifs#category-list
    """

    def __init__(self, error="Not a valid category."):
        self.error = error
        super().__init__(self.error)

class ArgumentError(Exception):
    """
    Something went wrong, either a category, network or availability issue.
    Category must be an existent category and a string.
    You can check valid categories at: https://github.com/MarcoSa-2000/animegifs#category-list
    """

    def __init__(self, error="Something went wrong."):
        self.error = error
        super().__init__(self.error)

class GifError(Exception):
    """
    The gif in the input is wrong. Make sure you input the right gif url for get methods.
    Make sure gif url is a string.
    Make sure gif url belongs to the API source (they are usually hosted on oci).
    Best practice is to input directly the return of get_gif method.
    Check if myanimelist.net is working correctly.
    If still doesn't work please raise an issue in https://github.com/MarcoSa-2000/animegifs/issues.
    """

    def __init__(self, error="Wrong gif input."):
        self.error = error
        super().__init__(self.error)

class APIError(Exception):
    """
    This is an API error or a yet a not handled error.
    API hosting website might be down, retry in few minutes or hours.
    If the error persist please raise an issue in https://github.com/MarcoSa-2000/animegifs/issues.
    """

    def __init__(self, error="API hosting website is down."):
        self.error = error
        super().__init__(self.error)
