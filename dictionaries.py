purse = dict()

purse['money'] = 12
purse['candy'] = 3
purse['keys'] = 75

print(purse)

print(purse['candy'])

purse['candy'] = purse['candy'] + 2
print(purse['candy'])
print(purse)


counts = purse

names = ['money', 'car', 'keys', 'egg']
#
# for name in names:
#     if name not in counts:
#         counts[name] = 1 # przypisanie nowego klucza
#     else:
#         counts[name] = counts[name] + 1
# print(counts)


for name in names:
    counts[name] = counts.get(name, 0) + 1


print(counts)

counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])

print(list(counts))

print(counts.keys())

print(counts.values())

print(counts.items()) ### tuples inside

# axd = dict()
# line = input('Enter line of text:')
# words = line.split()
#
# print('Words:', words)
# print('Counting...')
#
# for word in words:
#     axd[word] = axd.get(word, 0) + 1
# print('Counts', axd)

jjj= { 'chuck' : 1 , 'annie' : 42, 'jan': 100}

for aaa,bbb in jjj.items():
    print(aaa,bbb)



name = input(str('Type the text:'))

counts2 = dict()
#
# words = name.split() ## counting words
# for line in words:
#     counts2[line] = counts2.get(line,0) + 1
#
# print(counts2)


for line in name:
    words = line.split()  ## counting letters
    for word in words:
        counts2[word] = counts2.get(word,0) + 1

print(counts2)

