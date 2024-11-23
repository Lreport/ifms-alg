#funcao para descobrir se é par ou impar
def verify(num):
    if num % 2 == 0:
        return 'pair'
    else:
        return 'odd'
    
#imput e resposta
try:
    print('Is it even or odd?')
    num = int(input('Set a num for discover: '))

    result = verify(num)
    print(f'The num {num} is {result}')

except ValueError:
    print('Invalid value. Please, try again')