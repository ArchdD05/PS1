import requests

URL='http://codekata.com/data/wordlist.txt'

response = requests.get(URL)
if response.status_code == 200:
    with open('wordlist.txt', 'w') as file:
        file.write(response.text)
else:
    print(f"Failed to retrieve wordlist. Status code: {response.status_code}")