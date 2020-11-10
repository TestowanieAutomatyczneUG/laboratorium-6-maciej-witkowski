import unittest
from src.zad2 import Password


class PasswordTest(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(self.password.ValidPassword(""), False)

    def test_valid_password(self):
        self.assertEqual(self.password.ValidPassword("AaBbCc123#"), True)

    def test_invalid_length(self):
        self.assertEqual(self.password.ValidPassword("ABc12#"), False)

    def test_without_capital_letter(self):
        self.assertEqual(self.password.ValidPassword("aabbcc123#"), False)

    def test_without_digit(self):
        self.assertEqual(self.password.ValidPassword("AaBbCc#&$"), False)

    def test_without_special_char(self):
        self.assertEqual(self.password.ValidPassword("AaBbCc123"), False)

    def test_password_not_string1(self):
        self.assertRaises(TypeError, self.password.ValidPassword, 2115)

    def test_password_not_string2(self):
        self.assertRaises(TypeError, self.password.ValidPassword, [])

    # Utility functions
    def setUp(self):
        self.password = Password()
