words = []

with open('words.txt', 'rt') as wordlist:
    for line in wordlist:
        words.append(line.strip())