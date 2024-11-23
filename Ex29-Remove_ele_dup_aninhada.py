#função para remover elementos duplicados
def remove_duplicates(list_aninhada):
    return [list(set(sublist)) for sublist in list_aninhada]

#list
list_aninhada = [[1, 1, 2, 3], [2, 3, 3, 4], [1, 2, 3, 4, 4]]

#resposta
list_aninhada_removed = remove_duplicates(list_aninhada)
print(list_aninhada_removed)