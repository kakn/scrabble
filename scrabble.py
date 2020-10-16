### WORDS WITH FRIENDS HACKS ###

import enchant
import random
import time
import os

#os.system('clear')

"""
T H I N G S  T O  A D D
- replace random.sample with something that iterates all options
- add an option to use pre-existing word[letter].upper()s from words on the board for spelling
"""

def reader(filename):
    infile = open(filename, 'r').read()
    words = infile.split('\n')
    return words

filename = "alphabet.txt"
words = reader(filename)
#print(words)

d = enchant.Dict("en_UK")
p = enchant.Dict("en_UK")

def factorisation(n):
    if n == 1:
        return n
    else:
        return n * factorisation(n-1)

processor = []
realwords = []
fuck = input()
n1 = list((fuck))
n = len(n1)

def quicksearch(n):
    if n == 1:
        return 0
    else:
        for i in range(factorisation(n)):
            word = random.sample(n1, n)
            word = ''.join(word)
            if word not in processor:
                processor.append(word)
            if d.check(word) == True:
                if word not in realwords:
                    realwords.append(word)
        return quicksearch(n-1)

def hacks(n):
    cunt = n**n
    if n == 1:
        return 0
    if n >= 7:
        for i in range(factorisation(n)):
            word = random.sample(n1, n)
            word = ''.join(word)
            if word not in processor:
                processor.append(word)
            if d.check(word) == True:
                if word not in realwords:
                    realwords.append(word)
        return hacks(n-1)
    else:
        for i in range(cunt):
            word = random.sample(n1, n)
            word = ''.join(word)
            if word not in processor:
                processor.append(word)
            if d.check(word) == True:
                if word not in realwords:
                    realwords.append(word)
        return hacks(n-1)

#quicksearch(n)
hacks(n)

#print(realwords)

word_dict = {}
def pointsystem(realwords):
    for word in realwords:
        word_dict[word] = 0
        for letter in range(len(word)):
            if (word[letter].upper() == 'A' or word[letter].upper() == 'E' or word[letter].upper() == 'I' or word[letter].upper() == 'O'
                or word[letter].upper() == 'U' or word[letter].upper() == 'L' or word[letter].upper() == 'N' or word[letter].upper() == 'S'
                or word[letter].upper() == 'T' or word[letter].upper() == 'R'):
                word_dict[word] += 1
            if word[letter].upper() == 'D' or word[letter].upper() == 'G':
                word_dict[word] += 2
            if word[letter].upper() == 'B' or word[letter].upper() == 'C' or word[letter].upper() == 'M' or word[letter].upper() == 'P':
                word_dict[word] += 3
            if word[letter].upper() == 'F' or word[letter].upper() == 'H' or word[letter].upper() == 'V' or word[letter].upper() == 'W' or word[letter].upper() == 'Y':
                word_dict[word] += 4
            if word[letter].upper() == word[letter].upper() == 'K':
                word_dict[word] += 5
            if word[letter].upper() == word[letter].upper() == 'J' or 'X':
                word_dict[word] += 8
            if word[letter].upper() == word[letter].upper() == 'Q' or 'Z':
                word_dict[word] += 10

pointsystem(realwords)

def winner(word_dict):
    v = list(word_dict.values())
    k = list(word_dict.keys())
    return k[v.index(max(v))]

print(processor)
print("{iter} total iterations.".format(iter=len(processor)))
time.sleep(1)
print(realwords)
time.sleep(0.5)
print("{words} words found".format(words=len(realwords)))
time.sleep(1)
#print(word_dict)
#print(realwords[0])
best = realwords[0]
print("Best match was {word}".format(word=best))
time.sleep(0.5)
print("Similar words to this best match = {match}".format(match=d.suggest(best)))

#print(factorisation(5))

"""
1, 2, 3, 4, 5
1, 2, 6, 24, 120
"""
