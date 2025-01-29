# import random
# print('\tДобро пожаловать в игру "Орел и решка"')
# tries = 0 # переменная количества бросков
# eagle = 0 # переменная количество орлов
# tail = 0 # переменная количества решек
#
# while tries < 108: # пока количество бросков меньше 100
#     coin = random.randint(0, 1) #переменная монеты рандомно принимает значение 0 или 1
#     tries += 1 # счетчик бросков увеличивается на 1
#     if coin > 0: # если переменная монеты больше 0
#         eagle += 1 # переменная монеты увеличивает значение на 1
#     elif coin < 1: # если монета меньше 1
#         tail += 1 # решка увеличивает значение на 1
# print('\nМонета подброшена', tries, 'раз') # тут и ниже выводит на экран полученные данные
# print('Орел выпал', eagle, 'раз(а).')
# print('Решка выпал', tail, 'раз(а).')
#
# input('\n\nНажмите Enter, чтобы выйти.')
import random

numberOfStreaks = 0
arr = []
subArr = ["OOOOOO", "PPPPPP"]

def coinFlip(array) :
    for i in range(0, 1000, 1):
        coin = random.randint(0, 1)
        if coin == 1 :
            array.append("O")
        else :
            array.append("P")
    return array

res = coinFlip(arr)

sixO=0
sixR=0
nowO=0
nowR=0
for it in res:
    if it=='O':
        nowO+=1
        nowR=0
    else:
        nowR+=1
        nowO=0
    if nowO==6:
        sixO+=1
        nowO=0
    if nowR==6:
        sixR+=1
        nowR=0

print('Решка выпал:', sixR, 'раз.' "\nОрел выпал:", sixO, 'раз.')


