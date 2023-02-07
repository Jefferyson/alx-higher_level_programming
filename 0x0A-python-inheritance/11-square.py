#!/usr/bin/python3
"""creates a square class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square
    private instance attribute size
    public method area()
    inherits from rectangle.
    """

    def __init__(self, size):
        """Initializes a square
        Args:
            - size: size of the square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Computes the area of the square instance
        overwrites the area() method from rectangle
        """

        return self.__size ** 2

