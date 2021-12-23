#!/usr/bin/python3
"""
UNITEST
"""

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.amenity import Amenity
import pep8


class TestAmenity(unittest.TestCase):
    """
    Test for amenity
    """

    def test_amenity(self):
        """
        amenity
        """
        a = Amenity(name="a")
        self.assertEqual(str, type(a.name))

    def test_pep8(self):
        """
        style
        """
        i = pep8.StyleGuide(quiet=True)
        style = i.check_files(['models/amenity.py'])
        self.assertEqual(style.total_errors, 0, 'Found errors.')


if _name_ == '_main_':
    unittest.main()
