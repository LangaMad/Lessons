# print('hello world')

a = ['8','Jhon','7.9',8,'jhon'] # Список - List
b = {'ANDREY':20,'TOPAEV':'ANDREY'}  # Словарь - Dict
c = ('8','Jhon','7.9',8,'jhon')  # Кортеж - Tuple
 

# x = str(input('введите ваше имя: '))
# n = str(input('введите ваше фамилие : '))

# print(x,'',n) 



# def din(a):
#     m = 4 + a
#     print(m)

# din(4)
# for:

# while:

# break
# continue
# a = 2

# b = 2
# c = a-b
# if 
# a == 0  
# else

# elif


# print('Hello')


# num  = int(input('Enter num : '))
# num2  = int(input('Enter num : '))
# c = num + num2
# print(c)
# n = 'Hello'
# print(n.lower()) #Уменььшает быквы слова
# print(n.upper())  #  увеличивает буквы слова
# print(len(n))   #Cчитает количество букв в слове 

# n = 5
# m = 6
# print(max(n,m))
# print(min(n,m))
# + - * /
# c = n**2 
# c = n // m
# b = n % m



def remove_duplicates(input_list):
    unique_list = []
    duplicates = []
    
    for item in input_list:
        if item in unique_list:
            duplicates.append(item)
        else:
            unique_list.append(item)
    
    return unique_list, duplicates

original_list = [1, 2, 2, 3, 4, 5, 5, 6]
unique_list, duplicates = remove_duplicates(original_list)

print("Оригинальный список с дубликатами:")
print(original_list)

print("Список дубликатов:")
print(duplicates)

print("Список без дубликатов:")
print(unique_list)



