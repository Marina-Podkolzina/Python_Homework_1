#1'. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.


print ('Введите число  от 1 до 7')
a= int (input())
if a == 1:
    print ('Нет,это будний день')
elif a == 2:
    print ('Нет,это будний день') 
elif a == 3:
    print ('Нет,это будний день')  
elif a == 4:
    print ('Нет,это будний день')
elif a==5:
    print ('Нет,это будний день')               
elif a==6 or a==7:
    print ('Да,это выходной день')
else:
    print('Неверно задано число,введите число от 1 до 7')