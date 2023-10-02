#!/usr/bin/python3
"""Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""


import pep8
import unittest
import inspect
import models
from models import city
from datetime import datetime
from models.base_model import BaseModel

City = city.City


class TestCityDocs(unittest.TestCase):
    """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
    @classmethod
    def setUpClass(cls):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        cls.city_f = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_city(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_city_module_docstring(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        self.assertIsNot(city.__doc__, None,
                         "city.py needs a docstring")
        self.assertTrue(len(city.__doc__) >= 1,
                        "city.py needs a docstring")

    def test_city_class_docstring(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")

    def test_city_func_docstrings(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        for func in self.city_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestCity(unittest.TestCase):
    """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
    def test_is_subclass(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_name_attr(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        if models.storage_t == 'db':
            self.assertEqual(city.name, None)
        else:
            self.assertEqual(city.name, "")

    def test_state_id_attr(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        if models.storage_t == 'db':
            self.assertEqual(city.state_id, None)
        else:
            self.assertEqual(city.state_id, "")

    def test_to_dict_creates_dict(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        c = City()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in c.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = City()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "City")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))
