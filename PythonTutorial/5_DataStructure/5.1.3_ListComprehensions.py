squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x !=y]
print(combs)

vec = [-4, -2, 0, 2, 4]
print(vec)

# create a new list with the values doubled
vec1 = [x*2 for x in vec]
print(vec1)

# filter the list to exclude negative numbers
vec2 = [x for x in vec if x >= 0]
print(vec2)

# apply a function to all the elements
vec3 = [abs(x) for x in vec]
print(vec3)

# call a method on each element
freshfruit = ['   banana', '   loganberry ', 'passion fruit   ']
print(freshfruit)

freshfruit1 = [weapon.strip() for weapon in freshfruit]
print(freshfruit1)

# create a list of 2-tuples like (number, square)
t = [(x, x**2) for x in range(6)]
print(t)

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
vec1 = [num for elem in vec for num in elem]
print(vec1)

from math import pi
p = [str(round(pi, i)) for i in range(1, 6)]
print(p)