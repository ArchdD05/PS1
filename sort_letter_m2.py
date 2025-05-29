sentence = input('Enter a sentence to sort: ')
list_of_chars = []

for char in sentence:
    ascii_val = ord(char)
    if (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122):
        if 65 <= ascii_val <= 90:
            ascii_val += 32
        list_of_chars.append(chr(ascii_val))
print(list_of_chars)

# sorting manually
n = len(list_of_chars)
for i in range(n):
    for j in range(0, n - i - 1):
        if list_of_chars[j] > list_of_chars[j + 1]:
            list_of_chars[j], list_of_chars[j + 1] = list_of_chars[j + 1], list_of_chars[j]

print(''.join(list_of_chars))