"""
Write a Python program to select an item randomly from a list. 
"""

import random


my_list = [20.10, 500, 3000, 60,"PHP", 90, "JAVA", "PYTHON"]


random_item = random.choice(my_list)


print("The randomly selected item is:", random_item)