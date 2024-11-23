#inputa um srt e inverter
print('Palindrome Checker')
text = str(input('Set a word you want: ')).strip()
text = text.lower() 


#(Slicing)
text_slic = text[::-1]

if text_slic == text:
    print('This word is a palindrome :D')
else:
    print('This word is not a palindrome :(')