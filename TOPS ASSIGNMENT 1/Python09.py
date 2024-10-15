""" Swap the Values of Variables with a 3rd Variable """

a = 100
b = 200
temp = a # 100
# a and temp both have the same value so we will change the value of a

a = b # so now a = 200
b = temp # now b = 100

print (a,b)

""" Swap the Values of Variables without a 3rd Variable """

a = a+b  # a = 100+200, a =300
b = a-b  # b = 300-200, new b = 100
a = a-b  # a = 300-100, a = 200

print(a,b)





