from Modul import registreeri_kasutaja, autoriseeri_kasutaja, muuda_parooli, unusta_parool, kontrolli_parooli, genereeri_parool, kasutajad, paroolid

print("Tere tulemast!")  # Приветственное сообщение

while True:  # Бесконечный цикл для отображения меню
    try:
        print("Menu:")
        print("1. Uue kasutaja registreerimine")  # Регистрация нового пользователя
        print("2. Kasutaja autoriseerimine")  # Авторизация пользователя
        print("3. Parooli muutmine")  # Изменение пароля
        print("4. Parooli taastamine")  # Восстановление пароля
        print("5. End")  # Выход из программы
        valik = input("Teie valik: ")  # Ввод выбора пользователя

        if valik == "1":    # Если пользователь выбрал регистрацию
            print("Uue kasutaja registreerimine:")
            username = input("Enter your username: ")  # Ввод имени пользователя

            if username in kasutajad:  # Проверка, существует ли уже такой пользователь
                print("Selle nimega kasutaja on juba olemas!")  # Сообщение, если пользователь уже есть
            else:
                print("Valige parooli loomise meetod:")
                print("1. Automaatne salasõna genereerimine")  # Автоматическая генерация пароля
                print("2. Looge ise parool")  # Пользователь вводит пароль вручную
                password_choice = input("Teie valik (1/2): ")  # Выбор метода создания пароля

                if password_choice == "1":  # Если выбран автоматический генератор пароля
                    password = genereeri_parool(5)  # Генерация пароля длиной 5 символов
                    print(f"Teie genereeritud parool: {password}")  # Вывод сгенерированного пароля
                elif password_choice == "2":  # Если пользователь хочет ввести пароль сам
                    while True:
                        password = input("Enter password: ")  # Ввод пароля вручную
                        if kontrolli_parooli(password):  # Проверка пароля на соответствие требованиям
                            break  # Если пароль подходит, выходим из цикла
                        else:
                            print("Parool peab sisaldama numbreid, suur- ja väiketähti ning erimärke.")  # Ошибка, если пароль не соответствует требованиям
                else:
                    print("Vale valik")  # Ошибка при неправильном выборе
                    continue  # Возвращение к выбору пароля

                if registreeri_kasutaja(username, password):  # Регистрация пользователя
                    print("Kasutaja edukalt registreeritud!")  # Успешная регистрация
                else:
                    print("Registreerimisviga!")  # Ошибка регистрации

        elif valik == "2":  # Если пользователь выбрал авторизацию
            print("Kasutaja autoriseerimine:")
            username = input("Enter username: ")  # Ввод имени пользователя
            password = input("Enter password: ")  # Ввод пароля
            if autoriseeri_kasutaja(username, password):  # Проверка имени пользователя и пароля
                print("Autoriseerimine õnnestus!")  # Успешная авторизация
            else:
                print("Vale kasutajanimi või parool!")  # Ошибка авторизации

        elif valik == "3":  # Если пользователь выбрал смену пароля
            print("Parooli muutmine:")
            username = input("Enter username: ")  # Ввод имени пользователя
            old_password = input("Enter old password: ")  # Ввод старого пароля
            if autoriseeri_kasutaja(username, old_password):  # Проверка старого пароля
                while True:
                    new_password = input("Sisestage uus parool: ")  # Ввод нового пароля
                    if kontrolli_parooli(new_password):  # Проверка нового пароля
                        if muuda_parooli(username, new_password):  # Изменение пароля в базе
                            print("Parool edukalt muudetud!")  # Успешное изменение пароля
                            break
                        else:
                            print("Parooli muutmise viga!")  # Ошибка изменения пароля
                    else:
                        print("Parool peab sisaldama numbreid, suur- ja väiketähti ning erimärke.")  # Ошибка, если пароль не соответствует требованиям
            else:
                print("Vale kasutajanimi või vana parool!")  # Ошибка, если старый пароль неверный

        elif valik == "4":  # Если пользователь выбрал восстановление пароля
            print("Parool taastamine:")
            username = input("Enter username: ")  # Ввод имени пользователя
            new_password = unusta_parool(username)  # Генерация нового пароля
            if new_password:
                print(f"Teie uus parool: {new_password}")  # Вывод нового пароля
            else:
                print("Kasutajat ei leitud!")  # Ошибка, если пользователь не найден
    
        elif valik == "5":  # Если пользователь выбрал выход из программы
            print("Programm lõpetatud.")  # Сообщение о завершении программы
            break  # Прерывание цикла и выход из программы

        else:
            print("Vale valik!")  # Ошибка, если пользователь ввел некорректный выбор

    except ValueError:  # Обработка ошибок ввода
        print("Sisestamisviga!")  # Сообщение об ошибке ввода
