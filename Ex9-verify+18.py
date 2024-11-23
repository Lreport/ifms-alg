#inputar a idade
try:
    age = int(input('Set your agr: '))

except ValueError:
    print('Sorry, invald value. Please try again :/')

#resposta se pode passar ou não
if age >= 18:
    print('Ok, you can pass')
else:
    print("Sorry, you can't pass...")