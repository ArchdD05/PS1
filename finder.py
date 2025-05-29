from pybloom_live import BloomFilter

user_word=input('Enter a word to find in the text: ')
with open('wordlist.txt', 'r') as file:
    words = file.read().splitlines()
    line_count=len(words)
n=line_count
p=0.01
bf=BloomFilter(capacity=n, error_rate=p) 
for word in words:
    bf.add(word)
if user_word in bf:
    print(f"The word '{user_word}' is in the wordlist.")
else:
    print(f"The word '{user_word}' is not in the wordlist.")