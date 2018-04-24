#!/usr/bin/env python3

import unittest
from dont_get_volunteered import google_position_to_position, position_to_google_position, is_valid_position, valid_moves, answer_acc, answer

class Test(unittest.TestCase):

    def test_first(self):
        self.assertEqual(google_position_to_position(6), (1,7))

    def test_second(self):
        self.assertEqual(google_position_to_position(0), (1,1))

    def test_third(self):
        self.assertEqual(google_position_to_position(45), (6,6))

    def test_fourth(self):
        self.assertEqual(google_position_to_position(59), (8,4))

    def test_fifth(self):
        self.assertEqual(position_to_google_position((5,1)), 32)

    def test_sixth(self):
        self.assertEqual(position_to_google_position((8,8)), 63)

    def test_seventh(self):
        self.assertEqual(is_valid_position((5,1)), 1)

    def test_eighth(self):
        self.assertEqual(is_valid_position((-1, 4)), 0)

    def test_ninth(self):
        self.assertEqual(is_valid_position((1,0)), 0)

    def test_tenth(self):
        self.assertEqual(is_valid_position((9,9)), 0)

    def test_eleventh(self):
        self.assertCountEqual(valid_moves((1,1)), [(3,2), (2,3)])

    def test_twelfth(self):
        self.assertCountEqual(valid_moves((0,1)), [])

    def test_thirteenth(self):
        self.assertCountEqual(valid_moves((8,1)), [(6,2), (7,3)])

    def test_fourteenth(self):
        self.assertCountEqual(valid_moves([(6,3), (8,4)]), [(4,2), (4,4), (8,2), (8,4), (5,1), (5,5), (7,1), (7,5), (6,3), (6,5), (7,2), (7,6)])

    def test_fifteenth(self):
        self.assertEqual(answer(19,36), 1)

    def test_sixteenth(self):
        self.assertEqual(answer(0,1), 3)

if __name__ == '__main__':
    unittest.main()

