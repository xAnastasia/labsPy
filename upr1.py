#Первое задание
a = ('string')
b = ('s')
print(a.find(b)) # Возвращает 0, значит данное значение True.
result = int(a.find(b))
if result == 0:
    print("Данное значение содержиться в данной строке")
else:
    print("Данное значение не содержиться в данной строке")

#Второе задание
a = 5
b = 7
print('а = ' +str(a) + '\n' + 'b = '+ str(b) + '\n')
a,b=b,a
print('а = ' +str(a) + '\n' + 'b = '+ str(b))

#Третье задание
data = [12, 35, 64, 28, 40, 5]
max_num = max(data) #Ищем максимальный элемент и записываем в переменную.
print('Значение максимального элемента: ' + str(max_num))
print('Индекс максимального элемента: ' + str(data.index(max_num)))

#Четвертое задание
count_exit = 0;
main_menu = { 'Латте' : 100,
              'Раф' : 110,
              'Капучино' : 130,
              'Глясе' : 150}
print('### ОСНОВНОЕ МЕНЮ ###')
for key, value in main_menu.items():
    print(key)
print('### ### ### ### ### \n')
while(True):
    a = input('Введите название кофе, чтобы узнать стоимость:')
    if a not in main_menu:
        print('Вы допустили ошибку при вводе названия, попробуйте снова.\n')
        count_exit = count_exit+1
        if count_exit > 4:
            print('Слишком много раз было введено неверное значение.')
            break
    if a in main_menu:
        print('Стоимость напитка '+ a + ' составляет: ' + str(main_menu.get(a)) + " рублей.")
        break