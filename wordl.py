import json
from random import choice

'''
orstr = "cem"
indices  = [0,3]
newLet = "*"
orstr = list(orstr)
for i in indices :
    if 0 <= len(indices)  < len(orstr):
        orstr[i] = newLet
orstr = ''.join(orstr)
print(orstr)
'''

theletterto = "*"

def GuessTheLetter():
    while True:
        letter = input("Enter A Letter: ")
        if len(letter) != 1:
            print("Please Input a SINGLE LETTER!")
            continue
        else:
            return letter

def ChangeLetter(indices, lettertochangeto, wordtobechanged):
    wordtobechanged = list(wordtobechanged)
    for index in indices:
        wordtobechanged[index] = lettertochangeto
    wordtobechanged = ''.join(wordtobechanged)
    print(wordtobechanged)
    return wordtobechanged
    

def TheGame(letter):
    with open("words.json", "r") as f:
            words_data = json.load(f)
            the_hidden_word = choice(words_data["data"])
    print(the_hidden_word)
    while(not all(char == "*" for char in the_hidden_word)):
        
        letter = GuessTheLetter()
        positions = []
        for i, char in enumerate(the_hidden_word):
            if char == letter:
                positions.append(i)
            
        if letter in the_hidden_word:
            print("it is valid")
            print(f"the letter is the {positions}. character")
      
            the_hidden_word = ChangeLetter(positions, theletterto, the_hidden_word)
            print(the_hidden_word)
            if all(char == "*" for char in the_hidden_word):
                print("congrulations!")
                TheGame(None)
            continue
            
        else:
            print("I WILL EAT YOUR SOUL")
            continue
    



'''
def TheGame(letter):
    with open("words.json", "r") as f:
        words_data = json.load(f)
    the_hidden_word = choice(words_data["data"])
    print(the_hidden_word)
    letter = GuessTheLetter()
    positions = []
    for i, char in enumerate(the_hidden_word):
            if char == letter:
                positions.append(i)
            
    if letter in the_hidden_word:
        print("it is valid")
        print(f"the letter is the {positions}. character")
      
        ChangeLetter(positions, theletterto, the_hidden_word)
        if all(char == "*" for char in the_hidden_word):
            print("congrulations!")
            TheGame(None)
        GuessTheLetter()
    else:
        print("I WILL EAT YOUR SOUL")
        GuessTheLetter()
'''

def Main():
    TheGame(None)    


if __name__ == "__main__":
    Main()
