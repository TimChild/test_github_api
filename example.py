"""
2024-03-29 -- Some block of text at the top of the file
This is just an example of a bunch of things that would be good to be able to parse from a python file
"""
# Followed by some imports
import os
import sys
import logging


# module level attribute
logger = logging.getLogger(__name__)


# module level function
def get_current_path():
    """
    Get the current path of the file
    """
    return os.path.dirname(os.path.abspath(__file__))


def function_with_full_docstring(a: int, b: str) -> str:
    """
    Some description of the function with args and returns

    Args:
        a: The first argument
        b: The second argument

    Returns:
        The joined string
    """
    # Comment about what is happening in this function
    return f"a: {a}, b: {b}"


class SomeClass:
    def __init__(self, a: int, b: str):
        self.a = a
        self.b = b
        self.sys_path = sys.path

    def join_contents(self, separator: str | None = None) -> str:
        """
        Some description of the method with args and returns

        Args:
            separator: The separator to use between printed values

        Returns:
            The joined string
        """
        # Comment about what is happening in this method
        s = (separator if separator else "\n").join([f"a: {self.a}", f"b: {self.b}"])
        return s

    class NestedClass:
        def __init__(self, c: int):
            self.c = c

        def add_to_a(self, a: int):
            """
            Some description of method in nested class
            """
            return a + self.c

    def method_with_no_docstring(self):
        return self.a, self.b


class SomeSubclass(SomeClass):
    def another_method(self):
        """
        Some subclass method that has a docstring, but not with Args or Returns
        """
        return self.a + len(self.b)
