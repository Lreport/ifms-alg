#função para contar freq
def word_most_repeat():

    #inputar texto para freq
    print('Repeated word counter :D')
    text = input('Set a text if you want:')
    words = text.lower().split()

    # Cria um dicionário para contar a quantidade de vezes que cada palavra aparece
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Encontra as 5 palavras mais frequentes
    most_repeated_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    # Imprime as 5 palavras mais frequentes e suas contagens
    print("As 5 palavras mais frequentes no texto são:")
    for word, count in most_repeated_words:
        print(f"{word}: {count}")
        
#chamar a função para executar o código 
word_most_repeat()