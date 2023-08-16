"""
   The unit test for the models/square.py
"""

import unittest
import json
from models.square import Square


class TestSquare(unittest.TestCase):
    """
        Testing the square
    """
    def setUp(self):
        """
            Initializes the instance of the square
            With size 
        """
        self.sq = Square(20)

    def tearDown(self):
        """
            Delets the created instance
        """
        del self.sq

    def test_size(self):
        """
            Testing the square size getter
        """
        self.assertEqual(20, self.sq.width)

    def test_x(self):
        """
            Testing x getter
        """
        self.sq.x = 2
        self.assertEqual(2, self.sq.x)
        self.assertEqual(0, self.sq.y)

    def test_y(self):
        """
            Testing y getter
        """
        self.sq.y = 2
        self.assertEqual(2, self.sq.y)
        self.assertEqual(0, self.sq.x)

    def test_square_id(self):
        """
            Testing id of square
        """
        sq1 = Square(1, 0, 0, 12)
        self.assertEqual(12, sq1.id)

    def test_size_str(self):
        """
            Testing a wrong type for the size: str
        """
        with self.assertRaises(TypeError):
            sq1 = Square("s")

    def test_size_list(self):
        """
            Testing a wrong type for the size: list
        """
        with self.assertRaises(TypeError):
            sq1 = Square([1, 2])

    def test_size_bool(self):
        """
            Testing a wrong type for the size: boolean
        """
        with self.assertRaises(TypeError):
            sq1 = Square(True)

    def test_x_str(self):
        """
            Testing a wrong type for the x: str
        """
        with self.assertRaises(TypeError):
            sq1 = Square(2, "x", 0)

    def test_x_list(self):
        """
            Testing a wrong type for the x: list
        """
        with self.assertRaises(TypeError):
            sq1 = Square(2, [1, 2], 8)

    def test_x_bool(self):
        """
            Testing a wrong type for the x: boolean
        """
        with self.assertRaises(TypeError):
            sq1 = Square(2, True, 9)

    def test_y_str(self):
        """
            Testing a wrong type for the y: str
        """
        with self.assertRaises(TypeError):
            sq1 = Square(2, 0, "y")

    def test_y_list(self):
        """
            Testing a wrong type for the y: list
        """
        with self.assertRaises(TypeError):
            sq1 = Square(2, 6, [1, 2])

    def test_y_bool(self):
        """
            Testing a wrong type for the y: boolean
        """
        with self.assertRaises(TypeError):
            sq1 = Square(2, 9, True)

    def test_size_negative(self):
        """
            Testing a negative value for the size
        """
        with self.assertRaises(ValueError):
            sq1 = Square(-2)

    def test_size_zero(self):
        """
            Testing a zero value for the size
        """
        with self.assertRaises(ValueError):
            sq1 = Square(0)

    def test_x_negative(self):
        """
            Testing a negative value for the x
        """
        with self.assertRaises(ValueError):
            sq1 = Square(2, -1, 0)

    def test_y_negative(self):
        """
            Testing a negative value for the y
        """
        with self.assertRaises(ValueError):
            sq1 = Square(2, 4, -7)

    def test_area(self):
        """
            Testing for the area()
        """
        sq1 = Square(20)
        self.assertEqual(sq1.area(), 20 * 20)

    def test_str_overload(self):
        """
            Tests str overload
        """
        sq = Square(10, 2, 3, 9)
        self.assertEqual(sq.__str__(), "[Square] (9) 2/3 - 10")

    def test_update(self):
        """
            Tests the update function with *args
        """
        sq1 = Square(1)
        sq1.update(2, 4)
        self.assertEqual(sq1.__str__(), "[Square] (2) 0/0 - 4")

    def test_update_kwargs(self):
        """
            Tests the update() function with **kwargs
        """
        sq1 = Square(1)
        sq1.update(size=7, y=1, id=12)
        self.assertEqual(sq1.__str__(), "[Square] (12) 0/1 - 7")

    def test_update_both(self):
        """
            Tests the update() with both args and kwargs
        """
        sq1 = Square(1)
        sq1.update(2, 4, **{'x': 3, 'y': 4})
        self.assertEqual(sq1.__str__(), "[Square] (2) 0/0 - 4")

    def test_create_dict_equal(self):
        """
            Tests creating square is not equal
        """
        sq1 = Square(1, 3, 5, 6)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertNotEqual(sq1, sq2)

    def test_create_dict_is(self):
        """
            Tests create squaree is (sq1 is sq2)
        """
        sq1 = Square(1, 3, 5, 6)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertIsNot(sq1, sq2)

    def test_save_to_file_none(self):
        """
            Tests to save to file none
        """
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            content = json.load(f)
            self.assertEqual(content, [])

    def test_save_to_file_empty(self):
        """
            Tests to save to file empty list
        """
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            content = json.load(f)
            self.assertEqual(content, [])

    def test_save_to_file_rect(self):
        """
            Tests to save to file with the proper input
        """
        Square.save_to_file([Square(1, 3, 4, 5)])
        with open("Square.json", "r") as f:
            content = f.read()
            self.assertEqual(json.loads(content), [{"id": 5,
                                                    "size": 1,
                                                    "x": 3, "y": 4}])

    def test_save_to_file_noargs(self):
        """
            Tests to save to file with no arguments
        """
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_type(self):
        """
            Tests to save to file format saved in
        """
        Square.save_to_file([Square(1, 3, 4, 5)])
        with open("Square.json", "r") as f:
            content = f.read()
            self.assertEqual(str, type(content))

    def test_load_from_file_noexist(self):
        """
            Test the load from the file that does not exist
        """
        sq1 = Square(1)
        Square.save_to_file([sq1])
        list_output = Square.load_from_file()
        self.assertEqual(sq1.width, list_output[0].size)
