# range(start:stop:step)Функция геренации чисел

list()
dict()
set()
tuple()
# b ={1:3}
# x = [1,2,3,4,5,6,7,8,9,10]

# x = ['adfafa','affe',5]

# x = [a**2 for a in range(1,6)]

# print(x)

# sqr = {x: a**2 for a in range(1,10)}

# print(sqr)

# sqr = {x**2 for x in range(1,15)}
# print(sqr)


# words = 'Hello how are you'
# print(words.split())
# # sent = [word[0] for word in words.split()]
# # print(sent)


sentence = "Hello i am good and you , so what is your name"

words_num = [len(i) for i in sentence.split() if i != ',']

print(words_num)






