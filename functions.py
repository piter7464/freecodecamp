big = max('Hello world')
print(big)

small = min('Hello world')
print(small)

def greet(lang):
    if lang == 'es':
        print('Hola')

greet('es')

def returned():
    return ('Hello')

print(returned(), 'Piotr')