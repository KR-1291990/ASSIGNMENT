"""
Write a Python function that takes two lists and returns true if they 
have at least one common member """


list1 = [80,90,10]
list2 = [50,90,20]


status= False    


for item in list1:
    if item in list2:
        status = True
        break


if status == True:
    print("The lists have at least one common num.")
else:
    print("The lists do not have any common num.")
