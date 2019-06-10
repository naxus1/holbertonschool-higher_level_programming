#!/usr/bin/python3

import unittest
from models.base import Base


""" """


class TestBase(unittest.TestCase):

    def test_base_no_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_id(self):
        b2 = Base(4)
        b3 = Base(-5)
        self.assertEqual(b2.id, 4)
        self.assertEqual(b3.id, -5)
