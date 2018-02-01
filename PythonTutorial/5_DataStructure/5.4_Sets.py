basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   # show that duplicates have been removed

print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(a-b)
print(a|b)
print(a&b)
print(a^b)

c = {x for x in a if x not in 'abc'}
print(c)