#Задание 1
text = 'всем привет'
first_text = text[:text.find(' ')]       #Ищем первый пробел, разделяющий 2 слова, и берем всё, что до него.
second_text = text[text.find(' ') + 1:]  #Ищем первый пробел, разделяющий 2 слова, и берем всё, что после него.
last_text = second_text + ' ' + first_text
print(first_text)
print(second_text)
print(text)
print(last_text)


#Задание 2
text = input('Введите числа через пробел: ')
text_to_list = text.split()           #Преобразуем из типа str в list.
print(text_to_list)
elements = set(text_to_list)
print('Список чисел содержит различных элементов: "' + str(len(elements)) + '"')


#Задание 3
text = str.lower(input('Введите слово для проверки: '))
if text != text[::-1]:
    print('Слово не является полиндром.')
else:
    print('Слово является полиндром.')


# Задание 4
text = input('Введите числа через пробел: ')
text_to_list = text.split()                     #Преобразуем из типа str в list.
print (text_to_list)
list_to_int = [int(x) for x in text_to_list]    #Преобразование string в int в списке.
sum_elements = sum(list_to_int)
print ('Сумма чисел: ' + str(sum_elements) + '"')


Задание 5
a = input('Введите числа через пробел: ')
if all(map(str.isdigit, a)):
    sm = 0
    a = list(map(int, a))
    for i in a:
        if i % 2 != 0:
            sm += i**2
    print('Сумма квадротов нечетных чисел: ' + str(sm))
else:
    print('Ошибка ввода.')


# Задание 6
#Вар.1 (С ошибкой)
text = input('Введите текст для расшифровки: ')
print("".join([text[i+1] * int(text[i]) for i in range(0, len(text) - 1, 2)]))

#Вар.2
import re

text = input('Введите текст для расшифровки: ')
print(re.sub(r'(\d+)(\w)', lambda x: x[2] * int(x[1]), text))


# Задание 7
import string
import random
from typing import List

def generate_random_string(length: int, *choices: str) -> str:
    if not choices:
        # Будем использовать только буквы если нам все равно, из каких символов пароль
        choices = (string.ascii_letters, )

    # Создадим строку со всеми доступными символами
    all_choices = "".join(choices)
    result: List[str] = []
    choice_index = 0
    while len(result) < length:
        # Получим по символу из каждого списка, чтобы
        # Каждый список был использован хотя бы один раз
        if choice_index < len(choices):
            symbol = random.choice(choices[choice_index])
            result.append(symbol)
            choice_index += 1
            continue

        # После этого добавляем символы из любого списка
        symbol = random.choice(all_choices)
        result.append(symbol)

    # Перемешаем наш результат чтобы распределить начальные символы
    random.shuffle(result)
    return "".join(result)

def generate_password(length: int) -> str:

    #if length < 8:  # Проверка на длинну пароля
        #raise ValueError("Password length should be at least 8")

    return generate_random_string(
        length,
        string.ascii_uppercase, # В пароле должны быть заглавные буквы
        string.ascii_lowercase, # Строчные
        string.digits, # Цифры
        "!&?", # Спец-символы
    )

length = int(input('Введите длину пароля: '))
print(generate_password(length))
