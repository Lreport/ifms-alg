#funcao def para numeros pares
def pair_numbers(num_list):
    return [num for num in num_list if num % 2 == 0]

#input e resposta
try:
    print('Filer integer pair numbers ;D')
    print('Set the number separated by space')
    num = input('Set a list of numbers: ')
    number_list = [int(num) for num in num.split()]

    pair = pair_numbers(number_list)

    print(f'The pair number is: {pair}')

except ValueError:
    print('Invalid value. Please try again.')