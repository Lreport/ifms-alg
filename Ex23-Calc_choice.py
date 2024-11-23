#funções para calcular escolha
def sum(a, b):
    s = a + b
    return s

def sub(a, b):
    s = a - b
    return s

def mult(a, b):
    s = a * b
    return s

def div(a, b):
    s = a / b
    return s

#escolher função
print('Calculator')
print('1 - Sum')
print('2 - Subtraction')
print('3 - Multiplication')
print('4 - Division')

choice = int(input('Choose one option: '))

#resposta da escolha
if choice == 1:
    a = int(input('Set a firstnumber: '))
    b = int(input('Set a second number: '))
    print(f'{a} + {b} = {sum(a, b)}')
elif choice == 2:
    a = int(input('Set a first number: '))
    b = int(input('Set a second number: '))
    print(f'{a} - {b} = {sub(a, b)}')
elif choice == 3:
    a = int(input('Set a first number: '))
    b = int(input('Set a second number: '))
    print(f'{a} * {b} = {mult(a, b)}')
elif choice == 4:
    a = int(input('Set a firstnumber: '))
    b = int(input('Set a second number: '))
    print(f'{a} / {b} = {div(a, b)}')
else:
    print('Invalid option. Please try again.')