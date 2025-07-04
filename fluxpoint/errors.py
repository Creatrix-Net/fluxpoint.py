from enum import EnumType
from typing import Any


class HttpException(Exception):
    """
    Fluxpoint base exception class use this base class to catch any Fluxpoint errors.
    """

    def __init__(self, status: int, message: str) -> None:
        self.status: int = status
        self.message: str = message
        super().__init__(message)


class ApiError(HttpException):
    """
    Raised when Fluxpoint has an error it does not know how to handle
    """

    def __init__(self, message: str) -> None:
        super().__init__(500, message)


class WrongReturnType(Exception):
    """
    Exception raised when the when wrong return type is given
    """


class Unauthorised(HttpException):
    """
    Raised for an API 401
    """

    def __init__(self, message: str) -> None:
        super().__init__(401, message)


class RateLimited(HttpException):
    """
    You are exceeding the API's rate limits and built in Ratelimit handler
    Essentially a 429
    """

    def __init__(self, message: str) -> None:
        super().__init__(429, message)


class ParameterError(HttpException):
    """
    Parameters passed were not Sufficient
    """

    def __init__(self, message: str) -> None:
        super().__init__(400, message)

class InvalidCategory(Exception):
    """
    Category chosen to pass is invalid
    """
    def __init__(self, message: str = None) -> None:
        self.message: str = "Category chosen to pass in parameters is invalid"
        super().__init__(message)

class InvalidFeature(Exception):
    """
    The feature chosen is not valid
    """

def paramEnumValidCheck(parameter: Any, class2check: EnumType) -> None:
    """
    Checks if the ``parameter`` is a member of ``class2check`` :class::`Enum` and check if ``parameter`` is a instance of ``class2check`` :class::`Enum`

    :raises ValueError: if ``parameter`` is not a member of ``class2check``

    :param parameter: The parameter to check
    :type parameter: :class:`Any`
    :param class2check: The class to check
    :type class2check: :class:`EnumType`
    """
    if isinstance(parameter, class2check):
        raise Exception("Category must be a instance of NSFWImage or NSFWGif")
    if parameter not in class2check:
        raise ValueError(f"{parameter} is not a valid in {class2check}")