#!/usr/bin/python3
"""Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""


import pep8
import unittest
import inspect
import models
from models import state
from datetime import datetime
from models.base_model import BaseModel

State = state.State


class TestStateDocs(unittest.TestCase):
    """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
    @classmethod
    def setUpClass(cls):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        cls.state_f = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_state(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_state(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_state_module_docstring(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        self.assertIsNot(state.__doc__, None,
                         "state.py needs a docstring")
        self.assertTrue(len(state.__doc__) >= 1,
                        "state.py needs a docstring")

    def test_state_class_docstring(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        self.assertIsNot(State.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(State.__doc__) >= 1,
                        "State class needs a docstring")

    def test_state_func_docstrings(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        for func in self.state_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestState(unittest.TestCase):
    """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
    def test_is_subclass(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_name_attr(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        if models.storage_t == 'db':
            self.assertEqual(state.name, None)
        else:
            self.assertEqual(state.name, "")

    def test_to_dict_creates_dict(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        s = State()
        new_d = s.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in s.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = State()
        new_d = s.to_dict()
        self.assertEqual(new_d["__class__"], "State")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], s.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], s.updated_at.strftime(t_format))

    def test_str(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        state = State()
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))