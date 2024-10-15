"""Write a Python function that takes a list and returns a new list with 
unique elements of the first list."""

list1 = [1, 2, 3, 3, 4, 6, 5, 1, 6, 7, 7,8,8,10,10,1,5,5,50,60,70,50,70,90,]
new_list =[]
for i in list1:
    if i not in new_list:
        new_list.append(i)
print(new_list) 