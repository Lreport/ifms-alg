#lista vazia para ser inputada
numbers = []

try:
    #quantida de numeros para add na list
    print('list sorter of integers')
    n = int(input('How many numbers you want add? '))

    #inputando numero e add na list
    for i in range(n):
        num = int(input(f'Seted number {i+1}: '))
        numbers.append(num)
    

    #ordem list
    numbers.sort()

    #resposta
    print(f'The ordered list is: {numbers}')    

except ValueError:
    print('Invalid Value. Please try again.')