import json
import random
import os

def languageSelection():
    print("\033[H\033[J", end="")
    print("Choose a language from the list below")

    fileNames = os.listdir("./wordlists")
    languagePaths = []
    languageCounter = 1
    for fileName in fileNames:
        languageName = fileName.split(".")[0].lower()
        languagePaths.append(languageName)
        languageNameToPrint = f"{languageCounter}: {languageName.capitalize()}"
        print(languageNameToPrint)
        languageCounter += 1

    lastValidLanguageArrayPosition = len(languagePaths) - 1
    selectedLanguageArrayPosition = int(input()) - 1
    
    if(selectedLanguageArrayPosition > lastValidLanguageArrayPosition):
        return languagePaths[lastValidLanguageArrayPosition]
    return languagePaths[selectedLanguageArrayPosition]

languageToLoad = languageSelection();
languageToDisplay = languageToLoad.capitalize()

with open(f'wordlists/{languageToLoad}.json', encoding='utf-8') as json_file:
    wordPairArray = json.load(json_file)

numberOfWordPairs = len(wordPairArray) - 1
correctAmount = 0
incorrectAmount = 0
lastCorrectId = -1

#While the program is running
while True:
    #Choose a word as well as a decoy one
    correctID = random.randrange(0, numberOfWordPairs)
    if(correctID == lastCorrectId): continue
    while True:
        wrongID = random.randrange(0, numberOfWordPairs)
        if wrongID != correctID:
            break
    #Choose the order in which the words are presented
    order = random.randint(1, 2)
    #Which one of these two words is the correct translation
    print("\033[H\033[J", end="")
    print(f"Correct guesses: {correctAmount}\tIncorrect guesses: {incorrectAmount}")
    print(f"How do you say {wordPairArray[correctID]['word2']} in {languageToDisplay}?")
    if order == 1:
        print("1:", wordPairArray[correctID]['word1'] + "\nor\n2.", wordPairArray[wrongID]['word1'])
    else:
        print("1:", wordPairArray[wrongID]['word1'] + "\nor\n2.", wordPairArray[correctID]['word1'])
    if order == int(input()):
        correctAmount += 1
    else:
        incorrectAmount += 1