#!/usr/bin/python3
"""Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""

import pep8
import unittest
import inspect
import models
from models import review
from datetime import datetime
from models.base_model import BaseModel

Review = review.Review


class TestReviewDocs(unittest.TestCase):
    """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.review_f = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_review(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_module_docstring(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        self.assertIsNot(review.__doc__, None,
                         "review.py needs a docstring")
        self.assertTrue(len(review.__doc__) >= 1,
                        "review.py needs a docstring")

    def test_review_class_docstring(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        self.assertIsNot(Review.__doc__, None,
                         "Review class needs a docstring")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "Review class needs a docstring")

    def test_review_func_docstrings(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        for func in self.review_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))



class TestReview(unittest.TestCase):
    """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
    def test_is_subclass(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_place_id_attr(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        if models.storage_t == 'db':
            self.assertEqual(review.place_id, None)
        else:
            self.assertEqual(review.place_id, "")

    def test_user_id_attr(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        if models.storage_t == 'db':
            self.assertEqual(review.user_id, None)
        else:
            self.assertEqual(review.user_id, "")

    def test_text_attr(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        if models.storage_t == 'db':
            self.assertEqual(review.text, None)
        else:
            self.assertEqual(review.text, "")

    def test_to_dict_creates_dict(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in r.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(new_d["__class__"], "Review")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], r.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], r.updated_at.strftime(t_format))

    def test_str(self):
        """Tirmb rk vd vke vmd k vkdvk kv dkvdv ek ke v vdv"""
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))
