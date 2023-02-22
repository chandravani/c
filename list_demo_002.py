# -*- coding: utf-8 -*-
"""List_demo_002.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PylTk6LEfeiBc-KSIulXeJnLlkHATA25

# Nesting of the list

list inside a list
"""

A = [[1,2,3], [11, 22, 33], [45, 56, 77]]

A

A[0]

A[1]

A[1][1]

A = [[1,2,3], [11, 22, 33, [500, 502]], [45, 56, 77]]

A[0]

A[1]

A[1][3]

A[1][3][0]

A = [[1,2,3], [11, 22, 33, [500, 502]], [45, [239, "Hiii"], 56, 77]]

A[2][1][1]

A[-1][1][-1]

A[-1][-3][-1]

amazon_cart = [["watch", 5000], ["phone", 10000], ["laptop", 50000]]

total_cost = 0

# without for loop

amazon_cart[0][1]

amazon_cart[1][1]

amazon_cart[2][1]

amazon_cart[0][1] + amazon_cart[1][1] + amazon_cart[2][1]

total_cost = 0

for i in range(len(amazon_cart)):
  # print(i)
  print(amazon_cart[i][1])
  total_cost = total_cost + amazon_cart[i][1]

print(total_cost)



total_cost = 0
print(f"empty cart: {total_cost}")

for item in amazon_cart:
  print(item[1])
  total_cost = total_cost + item[1]
  print(f"cart after adding {item[0]}: {total_cost}")

print(f"Total payable amount: {total_cost}")

"""## List comprehension"""

# list which contains list of square of nos between 1 to 10


A = [1,2,3,4,5,6,7,8,9,10]
ans = [1, 4, 9, 16, ...]

A = [1,2,3,4,5,6,7,8,9,10]

ans = list()

for ele in A:
  print(ele**2)
  ans.append(ele**2)

print(ans)

ans = [ele**2 for ele in A]

print(ans)

ans = [i**2 for i in A]

print(ans)

# only take the square of odd no in the list A

A = [1,2,3,4,5,6,7,8,9,10]

ans = list()
print(ans)

for ele in A:
  if ele%2 != 0:
    print(ele**2)
    ans.append(ele**2)
    print(ans)

ans

ans = [ele**2 for ele in A if ele%2 != 0]

print(ans)

"""# Count"""

A = [1,2,1,4,5,6,7,7,7]

A.count(1)

A.count(7)

A.count(7999)

A = [1,2,1,4,5,6,7,7,7]
for i in A:
  print(i, A.count(i))

A = [1,2,1,4,5,6,[7,7],[7,7]]

A.count([7,7])

A.count(7)

A[-1].count(7)

A = "Sunny"
for i in A:
  print(i, A.count(i))

A = ["Sunny", "Sunny", "Chandra"]
for i in A:
  print(i, A.count(i))

A = ["Sunny", "SUNNY", "Chandra"]
for i in A:
  print(i, A.count(i))

"""## Extend"""

A = [1,2,3]

B = [11, 22, 33]

print(A + B)
print("before assignment")
print(A)

A = A + B
print("after assignment")
print(A)



A = [1,2,3]

B = [11, 22, 33]

A.extend(B) # permananet operation, inplace assignment

A

A = [1,2,3]

B = [11, 22, 33]

A.append(B)  # permananet operation, inplace assignment

A

"""## index method"""

A = [11, 3, 4, 56+2j, "Sunny", 1+2j]

A.index(11)

A.index("Sunny")

# print the index of all the complex nos.
# do a for loop
# if condition for type check
# if type is complex then print the index

for ele in A:
  if type(ele) == complex:
    print(f"Element: {ele} | Type: {type(ele)} | Index: {A.index(ele)}")

for ele in A:
  if type(ele) == int:
    print(f"Element: {ele} | Type: {type(ele)} | Index: {A.index(ele)}")

for ele in A:
  if type(ele) == str:
    print(f"Element: {ele} | Type: {type(ele)} | Index: {A.index(ele)}")

"""## isinstance"""

for ele in A:
  if isinstance(ele, complex):
    print(f"Element: {ele} | Type: {type(ele)} | Index: {A.index(ele)}")

ans = [ele for ele in A if isinstance(ele, complex)]
ans

ans = [ele for ele in A if type(ele)==complex]
ans

# ele for ele in A if type(ele)==complex

# print the index all the complex or int also

for ele in A:
  if isinstance(ele, complex) or isinstance(ele, int):
    print(f"Element: {ele} | Type: {type(ele)} | Index: {A.index(ele)}")

# print the index all the complex or int also

for ele in A:
  if isinstance(ele, (complex, int)): # pythonic way  # OR case
    print(f"Element: {ele} | Type: {type(ele)} | Index: {A.index(ele)}")

A = [11, 3, 4, 56+2j, "Sunny", 1+2j, 3, 3] # duplicate elements

A.index(3)

A = [11, "xyz", 3, 4, 56+2j, "Sunny", 1+2j, 3, 3] # duplicate elements

A.index(3)

A = [11, "xyz", 3, 4, 56+2j, "Sunny", 1+2j, 3, 3] # duplicate elements

A.index(4444444)

A = [1, 2, 3, [4,5,6], 7,8,9]

A.index(4) # sir its showing value Error

A = [1, 2, 3, [4,5,6], 7,8,9]

A.index([4,5,6]) # sir its showing value Error

A = [1, 2, 3, [4,5,6], 7,8,9]

A[3].index(4) # sir its showing value Error

"""## insert"""

A = [1,2,3,4,5]

A.append(99)
A

A.insert(2, "Sunny")

A

A.insert(2000, "Sunny")

A

A[2000]

A.insert(-2000, "Sunny")

A

A[2000]

A = [3,4,5]

len(A)

A.insert(2, "Sunny")

len(A)

A.insert(2000, "Sunny")

len(A)

A.insert(, "Sunny")

len(A)

A.insert("Sunny")

len(A)

A

A.insert(2, [1,2,34])

A

"""## remove"""

A = [1,2,3,455, 6, 77]

A.remove(455)

A

A = [1,2,3,455, 6, 77]

A.remove(77)

A

A = [1,1,2,3,455, 6, 77]

A.remove(1)

A

A = [1,1,2,3,455, 6, 88, 6, 77]

A.remove(6)

A

A = [1,1,2,3,455, 6, 88, 6, 77]

A.remove(9999)

A

A.pop(-1)

A.pop() # this removes the last element

"""# TUPLES - () - immutable
list = [] - mutable

"""

A = (1,2,3)

type(A)

A[0]

A[-1]

A[0] = 22

A = (22, 12, 34, 1)

A.sort()

A

sorted(A) # convert it into list and then return the sorted list

A = sorted(A) 

A

A = (22, 12, 34, 1)

len(A)

A * 2

A

A ** 2

max(A)

min(A)

A.index(12)

A.count(12)

sum(A)

# A.reversed()

A

A[1:]

A[::-1]

# ("item_name", amount) 

amazon_cart = [("watch", 5000), ("phone", 10000), ("laptop", 50000), ("shirt", 1000)]

total_cost = 0

total_cost = 0
print(f"empty cart: {total_cost}")

for item in amazon_cart:
  print(item[1])
  total_cost = total_cost + item[1]
  print(f"cart after adding {item[0]}: {total_cost}")

print(f"Total payable amount: {total_cost}")

# user input what you want to purchase?
# 


amazon_website = [("watch", 5000), ("phone", 10000), ("laptop", 50000), ("shirt", 1000)]

my_choice = input("What you want to purchase? : ")

my_choice

for item in amazon_website:
  if item[0] == my_choice:
    print(item)

"""## Assignment

1. On amazon website we have the following available items - 

```python
amazon_website = [("watch", 5000), ("phone", 10000), ("laptop", 50000), ("shirt", 1000)]
```
Take the user input N no. of times and find out the total cost to be paid?

OR

You can ask the user quntity or the count of item?

if the item is not present in the amazon website then print that item as out of stock and do add it total


HINT: while, for loop.. indexing

## Sets
unordered collection of unique elements
"""

x = {1,2,33,6,7}

type(x)

x =  {1,2,33,6,7, 7, 7}

x

x = set() # RECOMMENDED

type(x)

x = {} # NOT recommended

type(x)

x = tuple()
x

x = list()
x

x =  {1,2,33,6,7, 7, 7}

x

x[0] # NOT allowed as set is unordered

x =  {1,2,33,6,"Sunny"}

x

x.add(99)

x

x.add(99+2j)

x

x.add( -100)

x

x.add( -200)

x

x.add( 20.2)

x

x.add( 40.2)

x

x.remove(-100)

x

## return the list with unique elements

A = [1,2,3,5,5,6,6,7,7,7]

A = list(set(A))

A

x.append(99)

x

A = {1,2,3}
B = {4,5,6}


A + B

name = "rishi"

example = [name*2 for i in range(10)]

example

example = [i for i in range(10)]

example

example = [i**2 for i in range(10)]

example

example = [i**2 for i in range(1, 11)]

example

