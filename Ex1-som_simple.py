#funcao para soma simples
def sum(a:float, b:float):
    s = a + b
    return s

#input e resposta
try:
    a = float(input('Set a number for a sum: '))
    b = float(input('Set a second num for a sum: '))
    s = sum(a, b)
    print(f'{a} + {b} = {s}')
except ValueError:
    print('Invalid value. Please try again.')