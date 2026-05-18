import unittest
from password_checker import is_strong_password

class TestPasswordChecker(unittest.TestCase):
    def test_correct_password(self):
        """Проверка корректного пароля, соответствующего всем критериям"""
        self.assertTrue(is_strong_password("StrongPwd123!"))

    def test_too_short(self):
        """Пароль короче 8 символов должен быть отклонён"""
        self.assertFalse(is_strong_password("Sh1!"))

    def test_no_uppercase(self):
        """Пароль без заглавной буквы должен быть отклонён"""
        self.assertFalse(is_strong_password("weakpwd123!"))

    def test_no_lowercase(self):
        """Пароль без строчной буквы должен быть отклонён"""
        self.assertFalse(is_strong_password("WEAKPWD123!"))

    def test_no_digit(self):
        """Пароль без цифры должен быть отклонён"""
        self.assertFalse(is_strong_password("WeakPwd!"))

    def test_no_special_char(self):
        """Пароль без специального символа должен быть отклонён"""
        self.assertFalse(is_strong_password("WeakPwd123"))

    def test_edge_case_8_chars_with_all_criteria(self):
        """Пароль из 8 символов, соответствующий всем критериям"""
        self.assertTrue(is_strong_password("A1!bcdEf"))

if __name__ == "__main__":
    unittest.main()