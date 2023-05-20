
import random
import string

def generate_password(length):
    # выбираем символы, из которых будет состоять пароль
    characters = string.ascii_letters + string.digits + string.punctuation

    # генерируем пароль
    password = ''.join(random.choice(characters) for i in range(length))

    # заменяем случайный символ на случайную цифру
    password = password.replace(random.choice(password), str(random.randint(0, 9)), 1)

    return password

def check_password_strength(password):
    # проверяем длину пароля
    if len(password) < 8:
        return False

    # проверяем наличие цифр
    if not any(char.isdigit() for char in password):
        return False

    # проверяем наличие букв в разных регистрах
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False

    # если все проверки пройдены, возвращаем True
    return True

# запрашиваем пароль у пользователя
user_password = input("Введите пароль: ")

# проверяем его надежность
if check_password_strength(user_password):
    print("Пароль надежный")
else:
    print("Пароль ненадежный, генерируем новый...")
    # генерируем новый пароль и выводим его на экран
    new_password = generate_password(8)
    print("Новый пароль: ", new_password)
