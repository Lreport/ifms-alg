#recursiva ? 
#função para calcular fatorial
def factorial_num(n):
    if n < 0:
        return 'factorial < 0 cannot be calculated.'
    
    s = 1
    for i in  range(1, n + 1):
        s *= i
    return s

try:
    num = int(input('Set the factorial num you want calculate: '))
    print(f'the factorial {num} is {factorial_num(num)}')

except ValueError:
    print('Invalid Value. Please try a integer num.')