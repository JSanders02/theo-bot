import winsound
import time
from cmudict import cmuDict
from addedwords import addedWords
cmuDict.update(addedWords)

while True:
    sentence = input('Enter a sentence for Theo to say: ')

    newSentence = []
    for i in sentence:
        print(i)
        if i.isalpha() or i == "'" or i == " ":
            newSentence.append(i)
        else:
            pass
    
    sentence = ''.join(newSentence)

    wordList = sentence.split()
    print(wordList)

    phonemeList = []
    try:
        for i in tuple(wordList):
            print(i)
            phonemeList.append(cmuDict[i.upper()])

        for word in phonemeList:
            for phoneme in word:
                print(phoneme + ".wav")
                winsound.PlaySound("phonemes/" + phoneme + ".wav", winsound.SND_FILENAME)
            time.sleep(0.5)
        time.sleep(2)
    except KeyError:
        print('Phrase contained word(s) not in the CMU dictionary! Please try again!')
        time.sleep(2)