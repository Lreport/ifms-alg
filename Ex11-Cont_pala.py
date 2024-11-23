#inputarfrase
print('Word counter')
text = input('Set the text you want to count: ')

#split frases
words = text.split() #parentes para dividir a str em lista 

#contar frases split
num_words = len(words)

#resposta
print(f'The number of words in the text is: {num_words}')