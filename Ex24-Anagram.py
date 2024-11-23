#função para verificar anagrama 
def verify_anagram(word1:str, word2:str):
    return sorted(word1.lower()) == sorted(word2.lower())

#inputar palavras e reposta
print('Anagram checker :D')
word1 = input('Set the first word: ')
word2 = input('Set the second word: ')

#reposta
if verify_anagram(word1, word2):
    print('The words are anagrams :D')
else:
    print('The words are not anagrams :(')

