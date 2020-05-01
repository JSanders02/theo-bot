import nltk
import winsound
import time
arpabet = nltk.corpus.cmudict.dict()

while True:
    sentence = input('Enter a sentence for Theo to say: ')

    wordList = []
    currentIndex = -1
    lastSpace = False
    for i in sentence:
        currentIndex += 1
        if i == ' ':
            if not lastSpace:
                word = sentence[:currentIndex]
            else:
                word = sentence[lastSpace + 1: currentIndex]
            lastSpace = currentIndex
            wordList.append(word.lower())
    if sentence[lastSpace + 1:].lower() != ' ':
        wordList.append(sentence[lastSpace + 1:].lower())
    print(wordList)

    phonemeList = []
    for i in tuple(wordList):
        print(i)
        phonemeList.append(arpabet[i][0])

    print(phonemeList)

    for word in phonemeList:
        for phoneme in word:
            print(phoneme + ".wav")
            winsound.PlaySound("phonemes/" + phoneme + ".wav", winsound.SND_FILENAME)
        time.sleep(0.5)
    time.sleep(5)