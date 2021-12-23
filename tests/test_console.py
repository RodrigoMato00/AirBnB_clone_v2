#!/usr/bin/python3
"""
Unittests for the console
"""

import os
import pep8
import unittest
import models
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

class TestHBNBCommand(unittest.TestCase):
    """
    Test the console
    """

    def setUp(self):
        """
        Set up
        """
        self.stdout = StringIO()
        self.stderr = StringIO()
        self.stdin = StringIO()
        self.cmd = HBNBCommand()

    def test_pep8_conformance(self):
        """
        Test that we conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """
        Test docstring
        """
        self.assertIsNotNone(HBNBCommand.__doc__)

    def test_init(self):
        """
        Test init
        """
        self.assertTrue(isinstance(self.cmd, HBNBCommand))

    def test_quit(self):
        """
        Test quit
        """
        with patch('sys.exit') as m_sys_exit:
            self.cmd.onecmd("quit")
            m_sys_exit.assert_called_with(0)

    def test_empty_command(self):
        """
        Test empty command
        """
        with patch('sys.stdout', new=self.stdout):
            self.cmd.onecmd("")
            self.assertEqual(self.stdout.getvalue(), "")

    def test_do_quit(self):
        """
        Test do_quit
        """
        with patch('sys.exit') as m_sys_exit:
            self.cmd.do_quit(None)
            m_sys_exit.assert_called_with(0)

    def test_do_EOF(self):
        """
        Test do_EOF
        """
        with patch('sys.exit') as m_sys_exit:
            self.cmd.do_EOF(None + "\n")

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBStorage")
    def test_create(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("create BaseModel")
            self.assertEqual(f.getvalue(), "")
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("create User")
            self.assertEqual(f.getvalue(), "")
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("create State")
            self.assertEqual(f.getvalue(), "")
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("create City")
            self.assertEqual(f.getvalue(), "")
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("create Place")
            self.assertEqual(f.getvalue(), "")
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("create Amenity")
            self.assertEqual(f.getvalue(), "")
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("create Review")
            self.assertEqual(f.getvalue(), "")
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("all BaseModel")
            self.assertIn("BaseModel", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("all User")
            self.assertIn("User", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("all State")
            self.assertIn("State", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("all City")
            self.assertIn("City", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("all Place")
            self.assertIn("Place", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("all Amenity")
            self.assertIn("Amenity", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.cmd.onecmd("all Review")
            self.assertIn("Review", f.getvalue())


if __name__ == "__main__":
    unittest.main()