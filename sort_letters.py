sentence=input('Enter a sentence to sort:')
list_of_chars = []
for char in sentence:
    if char.isalpha(): 
        char=char.tolower()
        list_of_chars.append(char)
#print(list_of_chars)
sorted_list = sorted(list_of_chars)
print(''.join(sorted_list))
#print('Sorted characters:', sorted_list)

        