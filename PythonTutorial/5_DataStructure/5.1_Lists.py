# Methods of list objects
#
# list.append(x)
#   Add and item to the end of the list. Equivalent to a[len(a):] = [x]
#
# list.extend(iterable)
#   Extend the list b appending all the items from the iterable. Equivalent to a[len(a):] = iterable
#
# list.insert(i, x)
#   Insert an item at a given position. The first argument is the index of the element before which 
#   to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent
#   to a.append(x).
#
# list.remove(x)
#   Remove the first item from the list whose value is x. It is an error if there is no such item.
#
# list.pop([i])
#   Remove the item at the given position in the list, and return it. If no index is specified, a.pop() 
#   removes and returns the last item in the list. 
#
# list.clear()
#   Remove all items from the list. Equivalent to del a[:].
#
# list.index(x[, start[, end]])
#   Return zero-based index in the list of the first item whose value is x. Raise a ValueError if there is 
#   no such item.
# 
# list.count(x)
#   Return the number of times x appears in the list.
#
# list.sort(key=None, reverse=False)
#   Sort the items of the list in place (the arguments can be used for sort customization)
#
# list.reverse()
#   Reverse the elements of the list in place.
#
# list.copy()
#   Return a shallow copy of the list. Equivalent to a[:].

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))    # Find next banana starting a position 4

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

print(fruits.pop())
