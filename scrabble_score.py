#create a dictionary with values for each letter

scores = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1,
                'l': 1, 'n': 1, 'r': 1, 's': 1, 't': 1,
                'd': 2, 'g': 2,
                'b': 3, 'c': 3, 'm': 3, 'p': 3,
                'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
                'k': 5,
                'j': 8, 'x': 8,
                'q': 10, 'z': 10,
               }

def score(word):
    #need to return a total
    total = 0
    #need to loop through each word, add letters score from dict
    for letter in word:
        word = word.strip().lower()
        total += scores[letter.lower()]
    return total

#shorter version
#return sum([LETTER_SCORE[c] for c in word.strip().lower()])
