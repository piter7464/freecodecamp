a = [12,1,1,2,3,4]
b = [5,6,7]
c = a + b
print(c)

print(c[:4])

print(c[0])
print(c[-1])
print(c[::-1])

print(c[:])

print(c.count(1))
c.append(8)
print(c)

x = 9 in c
print(x)

x = 9 not in c
print(x)

c.sort()
print(c)

print(len(c))

print(max(c))

print(min(c))

print(sum(c))

print(sum(c)/len(c))

##########################################################################
# def listextending(list_package, div):
#     while True:
#         summ = sum(list_package)
#         totalval = summ / div
#         print('Score:', totalval)
#         if totalval < 15:
#             add = int(input('Enter next element for extend list:'))
#             list_package.append(add)
#             continue
#         #stop extending when sum of list divided by 2 is higher than 15
#         if totalval >= 15:
#             return list_package
#             break
#
#
# # creating an empty list
# lst = []
#
# # number of elements as input
# n = int(input("Enter number of elements : "))
#
# # iterating till the range
# for i in range(n):
#     ele = int(input('enter element:'))
#     lst.append(ele)  # adding the element
#
#
# print('Created list:', lst)
# z = int(input('Put divider:'))
# listextending(lst,z)

####################################################


abc = 'Hello man'
splited = abc.split()
print(splited)
days = ['Mon', 'Tue', 'Wen', 'Thr', 'Fri', 'Sat', 'Sun']
x = 'From michal@wp.pl Sat Jan 25'

splitt = x.split()

print(splitt)
for day in days:
    for split in splitt:
        if day == split:
            print('The day included in title is:', day)
            break

