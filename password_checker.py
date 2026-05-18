import re

def is_strong_password(password: str) -> bool:
    """
    Проверяет, является ли пароль надёжным.
    Критерии:
    - длина не менее 8 символов
    - хотя бы одна заглавная буква
    - хотя бы одна строчная буква
    - хотя бы одна цифра
    - хотя бы один специальный символ
    """
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

def main() -> None:
    """Демонстрация работы программы"""
    test_passwords = ["weak", "StrongPwd1!", "nodigits!", "NOLOWER1!", "short1!"]
    for pwd in test_passwords:
        result = is_strong_password(pwd)
        print(f"Пароль: {pwd} -> {'принят' if result else 'отклонён'}")
    print("\nВведите пароль для проверки: ")
    user_input = input()
    print(f"Результат: {'надёжный' if is_strong_password(user_input) else 'ненадёжный'}")

if __name__ == "__main__":
    main()