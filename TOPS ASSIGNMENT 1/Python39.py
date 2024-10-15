"""Write a Python program to find the second smallest number in a list."""

num = [5, 40, 90, 10, 40, 10, 2,5,50,60,]


sort = sorted(set(num)) 

if len(sort) >= 2:
    
    second_smallest = sort[1]
    print("The second smallest number is:", second_smallest)
else:
    print("The list does not have enough unique elements to find the second smallest number.")