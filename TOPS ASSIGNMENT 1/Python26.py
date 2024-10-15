#How will you remove last object from a list?

"""1)Using pop() method:"""
my_list = [1, 2, 3, 4, 5]
my_list.pop()  
print(my_list)

"""2) using del method :""" 
my_list = [1, 2, 3, 4, 5]
del my_list[-1] 
print(my_list)

"""3) using remove method"""
my_list = [1,2,3,4,5]
my_list.remove(my_list[-1])
print(my_list)
