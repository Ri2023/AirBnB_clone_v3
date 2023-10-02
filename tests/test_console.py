#!/usr/bin/python3
"""Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""

import pep8
import console
import inspect
import unittest
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
    def test_pep8_conformance_console(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")
