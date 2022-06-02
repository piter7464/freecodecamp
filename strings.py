s = 'Porsche Taycan'

print(s[0:4])

print(s[0:30])

print(s[:])

a = 'hello'
b = 'there'

c = a + ' ' + b

print(c)

fruit = 'banana'

x = 'n' in fruit
print(x)

xy = 'HELLO'
print(xy.lower())

# for string
seq_string = 'Python'
print(list(reversed(seq_string)))

# for tuple
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seq_tuple)))

# for range
seq_range = range(5, 9)
print(list(reversed(seq_range)))

# for list
seq_list = [1, 2, 4, 3, 5]
print(list(reversed(seq_list)))


# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# reverse the order of list elements
prime_numbers.reverse()


print('Reversed List:', prime_numbers)