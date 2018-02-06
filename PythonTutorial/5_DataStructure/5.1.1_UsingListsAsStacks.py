# The list methods make it very easy to use a list as a stack, where the last element added
# is the first element retrived ("last-in", "first-out"). To add an item to the top of the 
# stack, use append(). To retrive an item from te top of the stack, use pop() without an 
# explicit index.
#

stack = [3, 4, 5]
print(stack)

stack.append(6)
stack.append(7)
print(stack)

print(stack.pop())
print(stack)

print(stack.pop())
print(stack.pop())
print(stack)