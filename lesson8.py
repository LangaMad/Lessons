
# Работа с файлами 

# file = open(имя файла,режим доступа к файлу)

# 'r'- read() за чтение файла
# 'w' - write() запись с удалением уже существующих данных
# 'a' - write()  запись без удаления данных в 
# файле в новой строке
# 'x' - ---- создание файла если его не существует
# rb , wb -- чтение и запись в бинарном виде


# file = open('text.txt','r')
# text = file.read()

# print(text)
# file.close()

# file = open('text.txt','w')
# text = file.write('Hello world')

# print(text)
# file.close()

# file = open('text.txt','a')
# text = file.write('\thello')

# print(text)
# file.close()

# with open('text.txt','+a') as file:
#     text = file.write('plolokok;')

# with open('text.txt','x') as file:
#     text = file.write('plolokok;')


# with open('images.jpg','wb') as file:
#     data = file.write()
    
# print(data)


with open('text.txt','r','encoding-UTF-8') as file:
    text = file.read()
    
print(text)




