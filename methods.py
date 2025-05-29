with open ('wordlist.txt','r') as file:
    words=file.read().splitlines()
    length=len(words)
#print(words)
def hash(word, base, mod):
    hash_val = 0
    power = 1
    for ch in word:
        hash_val = (hash_val + ord(ch) * power) % mod
        power = (power * base) % mod
    return hash_val

def get_hashes(word, size, k, base=31):
    hashes = []
    for i in range(k):
        # adding delta to hash funcion for multiple hashes
        salted_word = chr(i + 65) + word  
        hashes.append(hash(salted_word, base, size))
    return hashes
def bloom_filter(words, size, k):
    bf = [0] * size  
    for word in words:
        for index in get_hashes(word, size, k):
            bf[index] += 1
    return bf

def check_word(word, bf, size, k):
    for index in get_hashes(word, size, k):
        if bf[index] == 0:
            return False
    return True


def main():
    size = int(length* 9.59)
    k=round(size*0.063/length)
    
    bf = bloom_filter(words, size,k)
    
    user_word = input('Enter a word to find in the text: ')
    if check_word(user_word, bf, size,k):
        print(f"The word '{user_word}' is in the wordlist.")
    else:
        print(f"The word '{user_word}' is not in the wordlist.")


if __name__ == "__main__":
    main()

    
    

    