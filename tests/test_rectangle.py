import unittest
from template.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Minimal unit tests for the Rectangle class."""

    def test_get_area(self):
        """Test that the area is calculated correctly."""
        rect = Rectangle(4, 5)
        self.assertEqual(rect.get_area(), 20)

    def test_get_width(self):
        """Test that the width is returned correctly."""
        rect = Rectangle(4, 5)
        self.assertEqual(rect.get_width(), 4)

if __name__ == '__main__':
    unittest.main()
