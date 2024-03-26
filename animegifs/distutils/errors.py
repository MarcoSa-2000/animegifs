class CategoryError(Exception):
    """
    Not a valid category. Category must be an existent category and a string.
    You can check valid categories at: https://github.com/MarcoSa-2000/animegifs#category-list
    """

    def __init__(self, category, error="Not a valid category."):
        self.category = category
        self.error = error
        super().__init__(self.error)

class CommonError(Exception):
    """
    This is yet a not handled error.
    Make sure you input the gif url for get methods.
    Make sure gif url is a string.
    Check if myanimelist.net is working correctly.
    please raise an issue in https://github.com/MarcoSa-2000/animegifs/issues.
    """

    def __init__(self, gif, error="Gif url is not valid or anime's ID is either removed or MyAnimeList is currently down."):
        self.gif = gif
        self.error = error
        super().__init__(self.error)
