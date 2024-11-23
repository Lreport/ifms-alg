#lista vazia para ser inputada
numbers = []

try:
    #inputar quantia de num
    print('List without duplicate numbers :D')
    n = int(input('How many numbers you want add? '))

    for i in range(n):
        num = float(input(f'Seted number {i+1}: '))

        #virificar num ja add
        if num not in numbers:
            numbers.append(num)

    #resposta
    print('The list without duplicate numbers is: ')
    print(numbers)

except ValueError:
    print('Invalid Value. Please try again :/')