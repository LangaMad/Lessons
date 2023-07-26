# Функции

# def название (аргумент):
#     
#     блок кода
#     return результат

# def hello (a,b): Позиционные аргументы
#     c = a + b
#     # print("hello world")
    
#     return c


# def hello (a=2,b=4): Именованные аргументы
#     c = a + b
#     # print("hello world")
    
#     return c  
# print(hello())
# *args , **kwargs

# def hello (*args): Переменная которая принимет 
# в себя неогрниченное 
# колличество позиционных аргументов
    
#     resul = 0 
    
#     for i in args:
#         resul += i
#         return resul


# def hello (**kwargs): Переменная которая принимет 
# в себя неогрниченное 
# колличество именованных аргументов
    
    
#     for key , value in kwargs.items():
#         print(value**2)
    
# hello(name = 4,age = 2, male = 5)


# a = 3 Тип данных чисел (integer (int))
# b = 'Hello world' Тип данных строки (string(str))
# c = 3.5 Тип данных с плавающей запятой (float(float))
# d = True Тип данных истины (booling (bool))

# a = [2,'hello',8.8,True] Тип данных list() Тип данных лист 
# b = {key:value} Тип Данных словарь
# c = ()  Тип данныз кортеж
# d = {}    Тип данных множетсва

# a = 'не хелло'

# def hello(): #Пример глобалного и локального кода
#     a = "hello"
#     return a

# def ne_hello(*args):
#     return args


# print(hello())
# print(ne_hello(a))

# Анонимная функция 

# num = lambda x,y : x+y
# print(num(1,3))

# num = lambda n : n % 2 == 0 
# print(num(5))

# Функция рекурсия (вызов из самой себя)


# def fak (u):
#     if u == 0:
#         return 1
#     else:
#         return fak(u - 1) * u
    
# print(fak(6))


    








