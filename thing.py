#five_letter_word

import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)

WORDS = [word.decode("utf-8") for word in response.content.splitlines()]

WORDS = list(filter(lambda word: len(word) == 5, WORDS))


    