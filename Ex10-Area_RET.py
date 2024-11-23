#funcao para calcaular area de um retangulo
def rectangle_area(b, h):
    Area = b * h
    return Area

#imputar b, h e respostas
try:
    print('Rectangle Area Calculator')
    b = float(input('Set a base of rectangle: '))
    h = float(input('Set a high of rectangle: '))
    Area = rectangle_area(b, h)
    print(f'The area of rectangle is: {Area}')
except ValueError:
    print('Invalid Value. Please try again :/')