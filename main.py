# List items are enclosed in square brackets
# List items are enclosed in square brackets
# Lists are odered
# Lists are mutable
# List elements do not need to be unique
# List can be of different data types

# ============================================

# list = [] # empty list
# list = [1,2,3]
# list = ['oranges', 'pear', 'banana', 'banana'] # Not unique elements
# list = [10, 'hello', 5.0] # Different Data types
# print(list)
''' List indexing'''

# fruits = ['oranges', 'pear', 'banana', 'banana']
# print(fruits[0])
# print(fruits[-2]) # count starts backwards
# print(fruits[15]) # IndexError: list index out of range

# fruits = ['oranges', 'pear', 'banana', 'banana', ['apple','kiwi','lemon']]
# print(fruits[4][1])

# shopping = ['oranges', 'pear', 'banana', 'banana', ['apple','kiwi','lemon'], ('kale','carrot'),['milk','juice']]
# print(shopping[6][1])
''' How to slice lists in Python '''

# fruits = ['oranges', 'pear', 'banana', 'banana', ['apple','kiwi','lemon']]
# print(fruits[4][:])

# fruits = ['oranges', 'pear', 'banana', 'banana', 'apple', 'kiwi', 'lemon']
# #print(fruits[1:6])
# print(fruits[::2]) # It prints every other item
# print(fruits[::-1]) # reversing the list order
# print(fruits[::-2]) # reverse the list order skiping an item

# print(fruits[:-2]) # Remove last two items
# print(fruits[-2:]) # Remove front items (0,1,-1,2?)

# list = ['box', 'star', 'metals', 'paper']
# print(list[:-2]) # Remove last two positioned items
# print(list[-2:]) # Still do not understand
''' Add elements to a list '''

# fruits = ['oranges', 'pear', 'banana', 'banana', 'apple', 'kiwi', 'lemon']

# fruits[2] = 'Berries' # Replaces the item on idex position 2
# fruits[1:4] = 'Mandarins', 'Peaches', 'Plums'
# fruits.append('limes') # Add items to the list
# print(fruits)
''' Remove or Delete list items '''

# fruits = ['oranges', 'pear', 'banana', 'banana', 'apple', 'kiwi', 'lemon']

# del fruits[0]
# del fruits[1:7]
# del fruits
# print(fruits)

''' Python List Methods'''

# print(dir(list))
# print(help(list.count))

#=======================================================

# fruits = ['orange', 'apple', 'pear', 'banana']
# fruits.append('cashew')
# print(fruits)

#=======================================================

# fruits = ['orange', 'apple', 'pear', 'banana']
# fruits.insert(1, 'guava')
# print(fruits)

#=======================================================

# fruits = ['orange', 'apple', 'pear', 'banana']
# fruits.clear()
# print(fruits)

#=======================================================

# fruits = ['orange', 'apple', 'pear', 'banana']
# fruits.pop(1) # it takes out the item at given index 
# fruits.pop(-1) 

# print(fruits.index('pear')) # it gives the index position of the item in the list 

# pos = fruits.index('pear')
# fruits.pop(pos)

# print(fruits)

#=======================================================

# fruits = ['orange', 'apple', 'pear', 'banana', 'pear', 'pear']

# # print(fruits.count('pear'))

# result = {}
# for items in fruits:
#     result[items] = fruits.count(items)

# print(result)

# result ['name'] = 'Adriana'
# print(result)

#===================================== Same as above importing modules ==========================

# from collections import Counter

# print(Counter(fruits))

#======================================================

''' List Membership Test '''

fruits = ['orange', 'apple', 'pear', 'banana', 'pear', 'pear']

print('orange' in fruits)
print('mango' not in fruits)

