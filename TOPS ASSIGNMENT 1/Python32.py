'''
Write a Python program to remove duplicates from a list. 

'''
list1 = [1, 2, 2, 3, 4, 4, 5, 1, 6, 7, 7,10,10]
new_list =[]
for i in list1:
    if i not in new_list:
        new_list.append(i)
print(new_list)        