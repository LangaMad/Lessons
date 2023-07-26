# task1
# words = input("words: ").split()
# un_words = list(set(words))
# print(un_words)

# task2
# words = str(input("Words: ")).split()

# longest_word = max(words,key=len)
# print(longest_word)

# task3

# words = str(input("Words: ")).split()
# words.reverse()
# print(words)

# task4
# words = input("Nums: ").split()
# words = list(map(int,words))

# sum_1 = sum(words)
# print(sum_1)


# task5

# [0:2:-1]

# word = input("Word : ")
# pal_word = word[::-1]
# if word == pal_word:
#     print('PALINDROM')
# else:
#     print("NOT PALINDROM")


# task6
# num = 10 

# while num >= 1:
#     print(num)
    # num -= 1
    
# task7
 
# for i in [1,2,3,4,5,6,7,8,9,10]: 
#    print(f'5 * {i} = {5*i}')

# task8

# total = 0
# count = 0

# while count != 5 :
#     number = int(input("Enter num: "))
#     total += number
#     count +=1
    
# print("summ of nums: ",total)

# a = True
# sum = 0


# task9
# while a :
#     num = int(input("enter num: "))
#     sum += num
#     if num == 0 :
#         a = False
#         print("Стоп") 
#     else:
#         print("enter again: ") 
        
# print(sum)

# task9.1

# num = int(input("enter num: "))
# sum = 0

# while num != 0  :
#     num = int(input("enter num: "))
#     sum += num
   
        
# print(sum)


# tesk10
# num = input("enter: ")

# with open('text.txt','r') as file:
#     text = file.read().split()
    
#     if num in text:
#         print('yes')
#     else:
#         print('no')
        
with open('text.txt','r') as file1,open('text2.txt','r') as file2:       
    text1 = file1.read()
    text2 = file2.read()

with open('merge.txt','w') as merge:
    merge.write(text1+text2)
    

        


