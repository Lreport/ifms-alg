#função para descobrir se é primo
def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
        
#inputar os numeros
try:
    print('List of integer prime numbers :D')
    print('Set exemple: x to n, 1 to 10')

    first_num = int(input('Set the first number: '))
    final_num = int(input('Ser the final number: '))

    #verificar se o first é menor que o final
    if first_num > final_num:
        print('The first number cannot be bigger than or equal to the final number')
    else:
        #imprimir os numero primos
        print(f'The prism numbers between {first_num} and {final_num} is: ')
        for num in range(first_num, final_num):
            if primo(num):
                print(num, end=' ')

except ValueError:
    print('Invalid values. Please try again :/')

