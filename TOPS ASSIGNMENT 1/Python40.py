"""Write a Python program to get unique values from a list 
"""

org_list = [10, 23, 23, 33, 44, 44, 50, 10, 50, 87, 87,"Apple","Samsung","Vivo","Apple"]


uni_value= list(set(org_list))


print("Original list:", org_list)
print("List of unique values:", uni_value)