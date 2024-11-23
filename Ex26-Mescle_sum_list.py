#importar counter da classe collections
from collections import Counter #coubter conta a frequencia de cada item na lista ou dictionario

dic1 = {}

dic2 = {}

#

#inputar dic1
num_values_dic1 = int(input('Set numbers values you want for dictionary1: '))
for i in range(num_values_dic1):
    key = input(f'Set the key {i+1}: ')
    value = int(input(f'Set the value {i+1}: '))
    dic1[key] = value

#inputar dic2
num_values_dic2 = int(input('Set numbers values you want for dictionary2: '))
for i in range(num_values_dic2):
    key = input(f'Set the key {i+1}: ')
    value = int(input(f'Set the value {i+1}: '))
    dic2[key] = value

dic3 = Counter(dic1) + Counter(dic2)
print(dic3)