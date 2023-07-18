"""
    Tests case for the task base.py in the models directory.
"""
import unittest
from models.base import Base
from models.square import Square
import json


class TestBaseClass(unittest.TestCase):
    """
        Tests the class for a base class.
    """
    def test_id_none(self):
        """
            initializes the instance of a base class with no id
        """
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        """
            Initializes the instance with the id > 0
        """
        b = Base(12)
        self.assertEqual(12, b.id)

    def test_id_zero(self):
        """
            Initializes the instance with the id == 0
        """
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        """
            Initializes the instance with the id < 0
        """
        b = Base(-2)
        self.assertEqual(-2, b.id)

    def test_id_string(self):
        """
            Intializes the instance with the id string
        """
        b = Base("Base")
        self.assertEqual("Base", b.id)

    def test_id_list(self):
        """
            Initializes the instance with the id list
        """
        b = Base([1, 3, 6])
        self.assertEqual([1, 3, 6], b.id)

    def test_id_tuple(self):
        """
            Initializes the instance with the id tuple
        """
        b = Base((1, 3))
        self.assertEqual((1, 3), b.id)

    def test_id_dict(self):
        """
            Initializes the instance with the id dict
        """
        b = Base({'id': 12})
        self.assertEqual({'id': 12}, b.id)

    def test_to_json_type(self):
        """
           tests to_json type
        """
        sq = Square(9)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        """
             tests to json value (string)
        """
        sq = Square(1, 0, 0, 9)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string), [{"id": 9, "y": 0,
                                                    "size": 1, "x": 0}])

    def test_to_json_None(self):
        """
            tests to json None
        """
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_empty(self):
        """
            tests to_json Empty
        """
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_from_json_string(self):
        """
            tests from json_string
        """
        sq = Square(1, 0, 0, 234)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        json_list = Base.from_json_string(json_string)
        self.assertEqual(json_list, [{'size': 1, 'x': 0, 'y': 0, 'id': 234}])

    def test_from_json_none(self):
        """
            tests from json none
        """
        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])

    def test_from_json_empty(self):
        """
            tests from json none
        """
        json_list = Base.from_json_string([])
        self.assertEqual(json_list, [])
