tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)

l = list(tel.keys())
print(l)

s = sorted(tel.keys())
print(s)

print('guido' in tel)
print('jack' not in tel)

