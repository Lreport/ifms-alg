#inputar as notas em Float
try:
        Mat = float(input('Set your note in math: '))
        Eng = float(input('Set yor note in englsih: '))
        His = float(input('Set yor note in history: '))
        Sci = float(input('Set your note in science: '))
    
except ValueError:
    print('Invalid value. Please try again :/')

#dic para materia e nota
materials = {
      'Math': Mat,
      'Engleshi': Eng,
      'History' : His,
      'Science': Sci
}

#função para calcular media e resposta
M = sum(materials.values())/len(materials)
print(f'The arithmetic mean of the grades is: {M}')

#mostrar notas acima da média
print('Notes above the total mean: ')
for matter, notte in materials.items():
      if notte > M:
            print(f'{matter}: {notte}')