#3'. Напишите программу, которая принимает на вход координаты точки 
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

#Здесь в задаче я не поняла условие.Вроде x и y не равны нулю,
# но в тоже время спрашивают в условии "или на какой оси она находится".
# Я прописала для всех вариатов.


print ('Введите значение x')
x = int (input())
print ('Введите значение y')
y = int (input())

if x == 0 or y == 0:
    if x == 0 and y == 0:
        print ('Точка лежит в начале координат')
    elif x == 0 and y > 0:
        print ('Точка лежит на координате "Y" между 1 и 2 четвертями')
    elif x == 0 and y < 0:
        print ('Точка лежит на координате "Y" между 3 и 4 четвертями')
    elif y == 0 and x > 0:
        print ('Точка лежит на координате "X" между 1 и 4 четвертями')
    elif y == 0 and x < 0:
        print ('Точка лежит на координате "X" между 2 и 3 четвертями')
else:
    if x > 0 and y > 0:
        print ('Точка лежит в первой четверти')
    elif x > 0 and y < 0:
        print ('Точка лежит в четвертой четверти')
    elif x < 0 and y > 0:
        print ('Точка лежит во второй четверти')
    elif x < 0 and y < 0:
        print ('Точка лежит в третьей четверти')
