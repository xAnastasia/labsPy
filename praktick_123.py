#Задание 1
guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me == 7:
    print('just right')
else:
    print('too hight')


#Задание 2
guess_me = 7
start = 1
while(True):
    if start < guess_me:
        print('too low')
        start += 1
    elif start == guess_me:
        print('found it!')
        break
    else:
        print('oops')


#Задание 3
text = [3, 2, 1, 0]
for element in text:
    print(element)


# #Задание 4
a = [i for i in range(1,15)
if i%2 != 0]
print(a)


#Задание 5
def good():
    a = ['Harry','Ron','Hermione']
    return a
print (good())


#Задание 6
def multiplication(a, b):
    if a%2 == 0 and b%2 == 0:
        print(a*b)
    else:
        return print('-1')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
multiplication(a,b)