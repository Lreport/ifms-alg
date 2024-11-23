#inputar numero INT
try:
    print('The multiplication table of integer number')
    num = int(input('Set a integer number: '))
    
    #loop de 0 a 11 e resposta
    print(f'Multiple table of {num}')
    for i in range(0, 11):
        S = num * i
        print(f'{num} . {i} = {S}')


except ValueError:
    print('Inavalid value. Plesa try again')