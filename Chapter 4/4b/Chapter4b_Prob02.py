import os
os.system('cls||clear')

#----CODE STARTS HERE------

sentence = input()
count = 0
if ("a" in sentence) or ("A" in sentence):
    count += 1
if ("e" in sentence) or ("E" in sentence):
    count += 1
if ("i" in sentence) or ("I" in sentence):
    count += 1
if ("o" in sentence) or ("O" in sentence):
    count += 1
if ("u" in sentence) or ("U" in sentence):
    count += 1

if count == 1:
    print("There is only one different vowel in the string.")
else:
    print(f"There are {count} different vowels in the string.")