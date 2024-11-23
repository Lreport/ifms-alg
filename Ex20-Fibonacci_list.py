#funcao fibonacci
def fibonacci(n:int):
    if n == 0:
        return 0
    elif n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
try:
    #inputar n e resposta
    print('Fibonacci List :D')
    print('Given the equation =  Fn = Fn-1 + Fn-2')
    num = int(input('Set a integer number for n: '))
    print(f'The fibonacci list of {num} is: ')

    #list
    for i in range(num + 1):
        print(fibonacci(i), end=' ')



except ValueError:
    print('Invalid value. Please try again :/')