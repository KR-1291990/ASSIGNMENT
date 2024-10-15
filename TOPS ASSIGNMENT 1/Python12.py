""" Write a sum of 3 integers, however two values are equal, sum will be zero """

num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
num3 = int(input("Enter a number : "))
sum = 0

if num1 == num2 or num2 == num3 or num3 == num1 :
    print("Sum is zero")
else :
    total = num1 + num2 + num3
    sum = total
    print(f"Sum is equal to : {sum}")    