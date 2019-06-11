 #!/usr/bin/python3

"""tests performed ?"""

from models.square import Square
from models.base import Base
import unittest

class TestSquare(unittest.TestCase):

    def test_create_square(self):
        s1 = Square(2, 2, 2, 2)
        s1 = s1.__str__()
        self.assertEqual(s1, "[Square] (21) 2/2 - 2")
        self.assertEqual(self.area(), 4)
