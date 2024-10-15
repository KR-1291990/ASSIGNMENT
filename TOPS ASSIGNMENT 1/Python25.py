#What is List? How will you reverse a list?
'''
list is one of the data types of collection and its orderable ,sequsnce , indexeble, mutable (elements of lists can be altered)and it can store different type of data together in one list.

'''
my_list = [1, 2, 3, "ABCD", 10.5,"EFGH"]


'''
1)using reverse()
'''
name=["JAVA","PHP","python"]
name.reverse()
print(name)
'''
2)using slicing
'''
rev=name[::-1]
print(rev)
'''
3)using reversed()
'''
rev_list =list(reversed(name))