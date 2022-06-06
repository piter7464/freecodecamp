(x, y) = (4, 'fred')

print(y)

d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)

if (0, 1, 2) < (5, 1, 2): ## is comparing 0 to 5 and if it's lower then it's stoping comparing
    print('True')

if ('Jones', 'Sally') < ('Jones', 'Sam'): ## because L in Sally is less than M it's comparing alphabet
    print('True')

c = {'a' : 10, 'c' : 1, 'b' : 22}
print(c.items())
for k,v in sorted(c.items()):
    print(k,v)
