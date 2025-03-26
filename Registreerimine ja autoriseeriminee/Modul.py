import random

kasutajad = []  # Список пользователей
paroolid = []   # Список паролей

def genereeri_parool(length: int) -> str:  # Генерация пароля
    sumbolid = ".,:;!_*-+()/#¤%&"  # Допустимые символы
    numbrid = '0123456789'  # Числа
    kirju = 'qwertyuiopasdfghjklzxcvbnm'  # Маленькие буквы
    kirju_add = kirju.upper()  # Заглавные буквы
    all = sumbolid + numbrid + kirju + kirju_add  # Общий набор символов
    return ''.join(random.choice(all) for i in range(length))  # Генерация случайного пароля

def kontrolli_parooli(password: str) -> bool:  # Проверка пароля
    if (any(i.isdigit() for i in password) and  # Проверяем, есть ли цифры
        any(i.islower() for i in password) and  # Проверяем, есть ли строчные буквы
        any(i.isupper() for i in password) and  # Проверяем, есть ли заглавные буквы
        any(i in ".,:;!_*-+()/#¤%&" for i in password)):  # Проверяем, есть ли спецсимволы
        return True  # Пароль соответствует требованиям
    return False  # Пароль не соответствует требованиям

def registreeri_kasutaja(username: str, password: str) -> bool:  # Регистрация пользователя
    if username in kasutajad:
        return False  # Пользователь уже существует
    kasutajad.append(username)  # Добавляем имя пользователя в список
    paroolid.append(password)  # Добавляем пароль в список
    return True  # Регистрация успешна

def autoriseeri_kasutaja(username: str, password: str) -> bool:  # Авторизация пользователя
    if username in kasutajad:
        check = kasutajad.index(username)  # Находим индекс пользователя
        return paroolid[check] == password  # Проверяем, совпадает ли пароль
    return False  # Неверное имя пользователя или пароль

def muuda_parooli(username: str, new_password: str) -> bool:  # Изменение пароля
    if username in kasutajad:
        check = kasutajad.index(username)  # Находим индекс пользователя
        paroolid[check] = new_password  # Меняем пароль на новый
        return True  # Пароль успешно изменен
    return False  # Пользователь не найден

def unusta_parool(username: str) -> str:  # Восстановление пароля
    if username in kasutajad:
        check = kasutajad.index(username)  # Находим индекс пользователя
        new_password = genereeri_parool(10)  # Генерируем новый пароль
        paroolid[check] = new_password  # Сохраняем новый пароль
        return new_password  # Возвращаем новый пароль
    return ""  # Если пользователя нет, возвращаем пустую строку
