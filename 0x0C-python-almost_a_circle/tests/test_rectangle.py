#!/usr/bin/python3

"""tests performed 8"""

from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle(unittest.TestCase):

    def test_rectangle_id(self):
        r1 = Rectangle(1, 2, 3, 4, 50)
        self.assertEqual(r1.id, 50)

    def test_rectangle_width_and_height(self):
        r2 = Rectangle(10, 20, 5, 5)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 20)

    def test_rectange_x_y(self):
        r3 = Rectangle(1, 2, 50, 50, 10)
        self.assertEqual(r3.x, 50)
        self.assertEqual(r3.y, 50)

    def test_rectangle_valid_type(self):
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, (1,), 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2.67)
        self.assertRaises(TypeError, Rectangle, 1, 2, [3], 4)
        self.assertRaises(TypeError, Rectangle, 1, 2, (3, 3.16), 4)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, {4, })
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "Four")

    def test_rectangle_valid_value(self):
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3, 4)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

    def test_rectangle_calculate_area(self):
        r4 = Rectangle(10, 5)
        self.assertEqual(r4.area(), 50)
        r5 = Rectangle(20, 20)
        self.assertEqual(r5.area(), 400)

    def test_rectangle_str(self):
        r6 = Rectangle(10, 5, 2, 2, 100)
        r6 = r6.__str__()
        self.assertEqual(r6, "[Rectangle] (100) 2/2 - 10/5")

    def test_rectangle_update(self):
        r7 = Rectangle(10, 10, 10, 10, 10)
        r7.update(89)
        self.assertEqual(r7.id, 89)
        self.assertEqual(r7.x, 10)
        new_r7 = r7.__str__()
        self.assertEqual(new_r7, "[Rectangle] (89) 10/10 - 10/10")
        r7.update(50, 50, 50, 50)
        new_r7 = r7.__str__()
        self.assertEqual(new_r7, "[Rectangle] (50) 50/10 - 50/50")

    def test_restangle_update_kwargs(self):
        r8 = Rectangle(10, 10, 10, 10, 10)
        r8.update(id=89)
        self.assertEqual(r8.id, 89)
        r8.update(width=112, x=200)
        self.assertEqual(r8.width, 112)
        self.assertEqual(r8.x, 200)
