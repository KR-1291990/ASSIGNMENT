""" Write a python program to sum of the n positive integers """
num = int(input("Enter a number : "))
sum = 0

for i in range(num+1) : 
  sum +=i  # Using a for loop in iteration (repetition) ‘i’ iterate between [1, num]
  print(sum)   
  """ 1,2,3,4,5,6,7,8 
  0+1 = 1, 1+2 = 3, 3+3 = 6, 6+4 = 10, 10+5 = 15, 15+6 = 21, 21+7 = 28, 28+8 = 36"""

