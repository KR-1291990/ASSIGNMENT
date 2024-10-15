""" Factorial Number of a given number """
factorial = 1
num = int(input("Enter a number : "))

for i in range (1,num+1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")
