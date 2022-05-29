# while True:
#     line = input('> ')
#     if line == 'done':
#         break  #uciekazpetli
#     print('line')
# print('done')
#
# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue #wraca znowu w warunek petli
#     if line == 'done':
#         break
#     print(line)
# print('done')

for i in [5, 4, 3, 2, 1]:
    print(i)

friends = ['Mike', 'John']

for friend in friends:
    print('Hello', friend)

list = [1, 3, 5, 8, 2, 4]

highest = 0

for x in list:
    if highest < x:
        highest = x

print(highest)