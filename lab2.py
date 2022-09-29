#Первое задание
name = input("Введите ваше имя: ")
print("Ваше имя: " + str(name))
print("Первый символ: " + str(name[0]))
print("Последний символ: " + str(name[-1]))

#Второе задание
x = input("Введите первое число: ")
y = input("Введите второе число: ")
print("Первое число: " + str(x))
print("Второе число: " + str(y))
proizvedenie = int(x)*int(y)
print("Произведение: " +str(proizvedenie))

#Третье задание
a = input("Введите сообщение: ")
print("Сообщение: " + str(a))
print("Модифицированное сообщение: " + str(a[0:2]) + str(a[-2]) +str(a[-1]))

#Четвертое и пятое задание
years_list = [1997, 1998, 1999, 2000, 2001, 2002]
print("Третий день рождения: " + str(years_list[3]))

#Шестое и седьмое задание
things = ["mozzarella", "cinderella", "salmonella"]
print("Взятие элемента: " + str.upper(things[1]))
print("Cписок: " + str(things)) #Список не изменился

things.pop(-1)
print("Измененный список: " + str(things))

#Восьмое задание
e2f = { 'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print("Англо-французский словарь :" + str(e2f))
print("Французский вариант слова walrus :" + str(e2f['walrus']))

#Девятое и десятое задание
life = {"Animals": {
    "cats": ["Hungry", "Grumpy", "Lucy"],
    "octopi": "",
    "emus": ""},
        "plants":{
    ""},
        "other":{
    ""}
        }
# print(life)
print(life.keys())
print(life['Animals'].keys())
print(life['Animals'])
print(life['Animals']['cats'])





