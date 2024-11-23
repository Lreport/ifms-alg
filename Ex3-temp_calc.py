#funcao para temp Fahrenheit e Celsius
def temp_coversor(C):
    F = C * 1.8 + 32
    return F

#input e resposta
try:
    print('Celsius to Fahreinheit :D')
    C = float(input('Set a temperature in Celsius: '))
    F = temp_coversor(C)
    print(f'the {C}°C Celsius in Fahreinheit is: {F}°F')

except ValueError:
    print('Invalid Value. Please try again.')