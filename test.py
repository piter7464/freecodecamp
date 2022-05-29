# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(n):
    ele = input('enter element:')
    lst.append(ele)  # adding the element

print(lst)

def test(tablica):
    print(tablica)

x = [1,2,3]
test(x)

print(type(sum(x)))