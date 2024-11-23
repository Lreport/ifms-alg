#função para contar vogais e consoantes
def cont_vows_cons(text):
    vowels = 'aeiou'
    text = text.lower()
    num_vowels = 0
    num_consonantes = 0

    for i in text:
        if i in vowels:
            num_vowels += 1
        elif i not in vowels:
            num_consonantes += 1

    return num_vowels, num_consonantes

#inputar text e resposta
print('Vowel and consonant counter :D')
text = input("Set a text: ")
num_vowels, num_consonantes = cont_vows_cons(text)

print(f"Vowels: {num_vowels}")
print(f"Consonants: {num_consonantes}")