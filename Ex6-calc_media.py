#inputar as notas em Float
try:
        Mat = float(input('Set your note in math: '))
        Eng = float(input('Set yor note in englsih: '))
        His = float(input('Set yor note in history: '))
        Sci = float(input('Set your note in science: '))
    
except ValueError:
    print('Invalid value. Please try again :/')

#função para calcular media e resposta
materials = Mat, Eng, His, Sci

M = sum(materials)/len(materials)
print(f'The arithmetic mean of the grades is: {M}')