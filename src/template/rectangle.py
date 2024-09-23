class Rectangle:
    """A class representing a rectangle.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """Initializes a rectangle with given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def get_area(self):
        """Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def get_width(self):
        """Gets the width of the rectangle.

        Returns:
            float: The width of the rectangle.
        """
        return self.width
