#inputar frese/palavra
print('*Character counter :D*')
word = input('Set one phrase or one word you want: ')

#tirar espaços
word_no_space = word.replace(' ', '')
#função para contar frase inputada
character_num = len(word_no_space)

#printar o numero e resposta
print(f'The number of characters is: {character_num}')