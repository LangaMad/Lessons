def dubl(input_list):
    uniq_list  = []
    dubl_list = []
    
    for i in input_list:
        if i in uniq_list:
            dubl_list.append(i)
        else:
            uniq_list.append(i)
            
    return uniq_list, dubl_list


origin = [1,2,2,3,4,5,5,6]
uniq_list , dubl_list = dubl(origin)


print(origin)

print(dubl_list)

print(uniq_list)






