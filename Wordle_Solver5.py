import random

wordListFile = open("Wordle Common Words.txt", "r")
wordListRaw = wordListFile.read()
wordList = []

for i in range(0,2315):
    wordList.append(wordListRaw[int(0+6*i):int(5+6*i)])
    
originalWordList = wordList.copy()
    
def frequencyOfRemaining(wordList):
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    for word in wordList:
        lettersUsed = []
        for index in range(0,5):
            if word[0+index:1+index] == "a" and "a" not in lettersUsed:
                a +=1
                lettersUsed.append("a")
            elif word[0+index:1+index] == "b" and "b" not in lettersUsed:
                b +=1
                lettersUsed.append("b")
            elif word[0+index:1+index] == "c" and "c" not in lettersUsed:
                c +=1
                lettersUsed.append("c")
            elif word[0+index:1+index] == "d" and "d" not in lettersUsed:
                d +=1
                lettersUsed.append("d")
            elif word[0+index:1+index] == "e" and "e" not in lettersUsed:
                e +=1
                lettersUsed.append("e")
            elif word[0+index:1+index] == "f" and "f" not in lettersUsed:
                f +=1
                lettersUsed.append("f")
            elif word[0+index:1+index] == "g" and "g" not in lettersUsed:
                g +=1
                lettersUsed.append("g")
            elif word[0+index:1+index] == "h" and "h" not in lettersUsed:
                h +=1
                lettersUsed.append("h")
            elif word[0+index:1+index] == "i" and "i" not in lettersUsed:
                i +=1
                lettersUsed.append("i")
            elif word[0+index:1+index] == "j" and "j" not in lettersUsed:
                j +=1
                lettersUsed.append("j")
            elif word[0+index:1+index] == "k" and "k" not in lettersUsed:
                k +=1
                lettersUsed.append("k")
            elif word[0+index:1+index] == "l" and "l" not in lettersUsed:
                l +=1
                lettersUsed.append("l")
            elif word[0+index:1+index] == "m" and "m" not in lettersUsed:
                m +=1
                lettersUsed.append("m")
            elif word[0+index:1+index] == "n" and "n" not in lettersUsed:
                n +=1
                lettersUsed.append("n")
            elif word[0+index:1+index] == "o" and "o" not in lettersUsed:
                o +=1
                lettersUsed.append("o")
            elif word[0+index:1+index] == "p" and "p" not in lettersUsed:
                p +=1
                lettersUsed.append("p")
            elif word[0+index:1+index] == "q" and "q" not in lettersUsed:
                q +=1
                lettersUsed.append("q")
            elif word[0+index:1+index] == "r" and "r" not in lettersUsed:
                r +=1
                lettersUsed.append("r")
            elif word[0+index:1+index] == "s" and "s" not in lettersUsed:
                s +=1
                lettersUsed.append("s")
            elif word[0+index:1+index] == "t" and "t" not in lettersUsed:
                t +=1
                lettersUsed.append("t")
            elif word[0+index:1+index] == "u" and "u" not in lettersUsed:
                u +=1
                lettersUsed.append("u")
            elif word[0+index:1+index] == "v" and "v" not in lettersUsed:
                v +=1
                lettersUsed.append("v")
            elif word[0+index:1+index] == "w" and "w" not in lettersUsed:
                w +=1
                lettersUsed.append("w")
            elif word[0+index:1+index] == "x" and "x" not in lettersUsed:
                x +=1
                lettersUsed.append("x")
            elif word[0+index:1+index] == "y" and "y" not in lettersUsed:
                y +=1
                lettersUsed.append("y")
            elif word[0+index:1+index] == "z" and "z" not in lettersUsed:
                z +=1
                lettersUsed.append("z")
        
    return {"a":a,"b":b,"c":c,"d":d,"e":e,"f":f,"g":g,"h":h,"i":i,"j":j,"k":k,"l":l,"m":m,"n":n,"o":o,"p":p,"q":q,"r":r,"s":s,"t":t,"u":u,"v":v,"w":w,"x":x,"y":y,"z":z}

def frequencyOfPositions(wordList):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    positions = {0:{"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,
            "w":0,"x":0,"y":0,"z":0},1:{"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,
            "w":0,"x":0,"y":0,"z":0},2:{"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,
            "w":0,"x":0,"y":0,"z":0},3:{"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,
            "w":0,"x":0,"y":0,"z":0},4:{"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,
            "w":0,"x":0,"y":0,"z":0}}
    for word in wordList:
        for index in range(0,5):
            for letter in alphabet:
                if word[0+index:1+index] == letter:
                    positions[index][letter] += 1
        
    return positions

def narrowList(guess, colors, wordList):
    blackLetters = []
    yellowLetters = {}
    greenLetters = {}
    
    #Create greenLetters list
    for i in range(0,5):
        if colors[0+i:1+i] == "g":
            greenLetters[i] = guess[0+i:1+i]
    
    #Create yellowLetters list
    for i in range(0,5):
        if colors[0+i:1+i] == "y":
            yellowLetters[i] = guess[0+i:1+i]
    
    #Create blackLetters list
    for i in range(0,5):
        if colors[0+i:1+i] == "b":
            blackLetters.append(guess[0+i:1+i])
    
    #remove if has a black letter
    wordsToRemove = []
    for word in wordList:
        for i in range(0,5):
            #Remove if has a black letter
            if word[i:i+1] in blackLetters and word not in wordsToRemove:
                #Find number of green letters that are the same as the black letter and the number of that letter in the word
                numGreenOrYellow = 0
                numThatLetter = 0
                for j in range(0,5):
                    if j in greenLetters:
                        if greenLetters[j] == word[i:i+1]:
                            numGreenOrYellow += 1
                    if j in yellowLetters:
                        if yellowLetters[j] == word[i:i+1]:
                            numGreenOrYellow += 1
                    
                    if word[j:j+1] == word[i:i+1]:
                        numThatLetter += 1
                if numThatLetter > numGreenOrYellow:
                    wordsToRemove.append(word)
            #Remove if does not have a green letter at that spot
            if i in greenLetters:
                if greenLetters[i] != word[i:i+1] and word not in wordsToRemove:
                    wordsToRemove.append(word)
            #Remove if has a yellow letter at that spot
            if i in yellowLetters:
                if yellowLetters[i] == word[i:i+1] and word not in wordsToRemove:
                    wordsToRemove.append(word)
            
        #Remove if does not have a yellow letter
        for yellowLetter in yellowLetters.values():
            if yellowLetter not in word and word not in wordsToRemove:
                wordsToRemove.append(word)
            
    for wordToRemove in wordsToRemove:
        wordList.remove(wordToRemove)
        
    return wordList
        
def bestWord(attemptNum, wordList, originalWordList):
    letterFrequencies = frequencyOfRemaining(wordList)
    positionFrequencies = frequencyOfPositions(wordList)
    
    #Special Case
    numTo5 = [0,1,2,3,4,0,1,2,3,4,0,1,2,3,4]
    specialCase = False;
    if attemptNum < 5 and len(wordList) > 2 and len(wordList) < 10:
        sameLetters = ["1","2","3","4","5"]
        differentLetters = []
        for i in range(0,len(wordList)):
            if i == 0:
                letter1 = wordList[i][0:1]
                letter2 = wordList[i][1:2]
                letter3 = wordList[i][2:3]
                letter4 = wordList[i][3:4]
                letter5 = wordList[i][4:5]
            else:
                if wordList[i][0:1] != letter1:
                    differentLetters.append(wordList[i][0:1])
                    if letter1 not in differentLetters:
                        differentLetters.append(letter1)
                    if "1" in sameLetters:
                        sameLetters.remove("1")
                if wordList[i][1:2] != letter2:
                    differentLetters.append(wordList[i][1:2])
                    if letter2 not in differentLetters:
                        differentLetters.append(letter2)
                    if "2" in sameLetters:
                        sameLetters.remove("2")
                if wordList[i][2:3] != letter3:
                    differentLetters.append(wordList[i][2:3])
                    if letter3 not in differentLetters:
                        differentLetters.append(letter3)
                    if "3" in sameLetters:
                        sameLetters.remove("3")
                if wordList[i][3:4] != letter4:
                    differentLetters.append(wordList[i][3:4])
                    if letter4 not in differentLetters:
                        differentLetters.append(letter4)
                    if "4" in sameLetters:
                        sameLetters.remove("4")
                if wordList[i][4:5] != letter5:
                    differentLetters.append(wordList[i][4:5])
                    if letter5 not in differentLetters:
                        differentLetters.append(letter5)
                    if "5" in sameLetters:
                        sameLetters.remove("5")
        if len(sameLetters) >= 3:
            specialCase = True
            
    #Add scores for each word
    if specialCase == True:
        #Special Case
        highestScore = 0
        secondScore = 0
        thirdScore = 0
        currentBestWord = "No Words"
        currentBestWord2 = ""
        currentBestWord3 = ""
        for word in originalWordList:
            lettersUsed = []
            wordsLeftUsed = []
            wordScore = 0
            for i in range(0,5):
                wordHasBeenUsed = False
                for wordLeftUsed in wordsLeftUsed:
                    if word[i:i+1] in wordLeftUsed:
                        wordHasBeenUsed = True
                if word[i:i+1] in differentLetters and word[i:i+1] not in lettersUsed:
                    if wordHasBeenUsed == False:
                        wordScore += 10
                    else:
                        wordScore += 5
                    '''for wordLeft in wordList:
                        if word[i:i+1] in wordLeft:
                            wordScore += 1'''
                    for wordLeft in wordList:
                        wordLeft.replace(word[i:i+1],"")
                        if word[i:i+1] in wordLeft:
                            wordsLeftUsed.append(wordLeft)
                lettersUsed.append(word[i:i+1])
                
            #Check if is a high score
            if wordScore > highestScore:
                currentBestWord3 = currentBestWord2
                currentBestWord2 = currentBestWord
                currentBestWord = word
                thirdScore = secondScore
                secondScore = highestScore
                highestScore = wordScore
            elif wordScore > secondScore:
                currentBestWord3 = currentBestWord2
                currentBestWord2 = word
                thirdScore = secondScore
                secondScore = wordScore
            elif wordScore > thirdScore:
                currentBestWord3 = word
                thirdScore = wordScore
        if highestScore <= 15:
            specialCase = False
            
    if specialCase != True:
        #Normal
        highestScore = 0
        secondScore = 0
        thirdScore = 0
        currentBestWord = "No Words"
        currentBestWord2 = ""
        currentBestWord3 = ""
        for word in wordList:
            lettersUsed = []
            wordScore = 0
            for i in range(0,5):
                if word[i:i+1] in lettersUsed:
                    wordScore += letterFrequencies[word[i:i+1]] / 5
                    wordScore += positionFrequencies[i][word[i:i+1]]
                else:
                    wordScore += letterFrequencies[word[i:i+1]]
                    wordScore += positionFrequencies[i][word[i:i+1]]
                    lettersUsed.append(word[i:i+1])
            if wordScore > highestScore:
                currentBestWord3 = currentBestWord2
                currentBestWord2 = currentBestWord
                currentBestWord = word
                thirdScore = secondScore
                secondScore = highestScore
                highestScore = wordScore
            elif wordScore > secondScore:
                currentBestWord3 = currentBestWord2
                currentBestWord2 = word
                thirdScore = secondScore
                secondScore = wordScore
            elif wordScore > thirdScore:
                currentBestWord3 = word
                thirdScore = wordScore
            
    return [currentBestWord,currentBestWord2,currentBestWord3]
    
def wordle(answer, wordList, originalWordList):
    numEachLetterInAnswer = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    for i in range(0,5):
        numEachLetterInAnswer[answer[i:i+1]] += 1
    
    for j in range(0,21):
        guess = bestWord(j,wordList, originalWordList)[0]
        
        colors = ""
        
        #Make Yellow Lists
        numYellowsUsed = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
        
        #Add letter of color for each word
        for i in range(0,5):
            if guess[i:i+1] == answer[i:i+1]:
                colors += "g"
            elif guess[i:i+1] in answer:
                if numYellowsUsed[guess[i:i+1]] < numEachLetterInAnswer[guess[i:i+1]]:
                    colors += "y"
                    numYellowsUsed[guess[i:i+1]] += 1
                else:
                    colors += "b"
            else:
                colors += "b"
        
        if guess == answer:
            '''print ("Finished in " + str(j + 1) + " guesses")
            if (j+1 < 3):
                print(answer)
            if (j+1 > 6):
                print(answer)'''
            if (j+1 >= 7):
                print(answer + ": " + str(j+1))
            return(j+1)
        else:
            narrowList(guess, colors, wordList)
    
'''num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13,num14,num15,num16,num17,num18,num19,num20,num21 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

for n in range(0,2315):
    wordList = originalWordList.copy()
    answer = wordList[n]
    
    num = wordle(answer, wordList, originalWordList)
    if num == 1:
        num1 += 1
    elif num == 2:
        num2 += 1
    elif num == 3:
        num3 += 1
    elif num == 4:
        num4 += 1
    elif num == 5:
        num5 += 1
    elif num == 6:
        num6 += 1
    elif num == 7:
        num7 += 1
    elif num == 8:
        num8 += 1
    elif num == 9:
        num9 += 1
    elif num == 10:
        num10 += 1
    elif num == 11:
        num11 += 1
    elif num == 12:
        num12 += 1
    elif num == 13:
        num13 += 1
    elif num == 14:
        num14 += 1
    elif num == 15:
        num15 += 1
    elif num == 16:
        num16 += 1
    elif num == 17:
        num17 += 1
    elif num == 18:
        num18 += 1
    elif num == 19:
        num19 += 1
    elif num == 20:
        num20 += 1
    elif num == 21:
        num21 += 1
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)
print(num7)
print(num8)
print(num9)
print(num10)'''
    
for i in range(0,21):
    print("Guess: " + str(bestWord(i, wordList, originalWordList)))
    wordList = narrowList(input("Word: "), input("Colors of letters: ") ,wordList)
    print(wordList)
    
'''scores = frequencyOfRemaining(wordList)
print(scores)'''

