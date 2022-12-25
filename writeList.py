import sys
def Info_Gathering():
    printlist = ["First name:","middle name","Last name:","Childs name","SO first name","SO middle name","SO last name","Important Dates MMDDYYYY(no spaces)","Important numbers"]
    # setlist = [
    #     ["john"],#First name:0
    #     ["Middle"],#Middle name:1
    #     ["doe"],#Last name:2
    #     ["child"],#Childs name:3
    #     ["jane"],#SO first name:4
    #     ["middle"],#SO middle name:5
    #     ["doe"],#SO last name:6
    #     ["01012022","02012022"],#Important dates:7
    #     ["10","1515"] #Important Numbers:8
    # ]
    setlist = [
        [],#First name:0
        [],#Middle name:1
        [],#Last name:2
        [],#Childs name:3
        [],#SO first name:4
        [],#SO middle name:5
        [],#SO last name:6
        [],#Important dates:7
        [] #Important Numbers:8
    ]

    setting = 0
    while(setting >= 0):
        x=-1
        for i in printlist:
            x+=1
            print(f"[{x}] {i}")
        print("[-1] stop\n")

        setting = int(input("List to update:"))
        info = (input("Add to a list: ")).lower()
        setlist[setting].append(info)
        print("\n\n\n")
    return setlist

def Make_Password(list):
    #run through lists with words
    letterList = ["a","e","i","l","o","s"]
    letterMap = ["@","3","1","1","0","$"]
    linesWritten = 0

    #Make names
    firstName = ""
    middleName = ""
    lastName = ""
    SOfirstName = ""
    SOmiddleName = ""
    SOlastName = ""
    yyDate = []

    firstLetter = []

    if(len(list[0]) != 0 ):
        firstName = list[0][0]
        firstLetter.append(firstName[0])

    if(len(list[1]) != 0):
        middleName = list[1][0]
        firstLetter.append(middleName[0])

    if(len(list[2]) != 0):
        lastName = list[2][0]
        firstLetter.append(lastName[0])

    if(len(list[4]) != 0):
        SOfirstName = list[4][0]
        firstLetter.append(SOfirstName[0])

    if(len(list[5]) != 0):
        SOmiddleName = list[5][0]
        firstLetter.append(SOmiddleName[0])

    if(len(list[6]) != 0):
        SOlastName = list[6][0]
        firstLetter.append(SOlastName[0])
    
    if(len(list[7]) != 0):
        for i in list[7]:
            yyDate.append(i[-2:])


    list.append(firstLetter)
    list.append(yyDate)

    try:
        fileName = sys.argv[1]
        if ".txt" not in fileName:
            fileName += ".txt"
    except:
        fileName = "WL.txt"

    with open(f"{fileName}", "w") as file:

        #write all to a list
        for i in list:
            for j in i:
                file.write(j+"\n")
                linesWritten += 1
        #switch common chars
        for i in list:
            for j in i:
                for l in j:
                    if l in letterList:
                        file.write(letterMap[letterList.index(l)])
                    else:
                        file.write(l)
                file.write("\n")
                linesWritten += 1
        #Permutations
        for i in list:
            for j in i:
                for k in list:
                    for l in k:
                        file.write(j+l+"\n")
                        linesWritten += 1
        #permutations plus common chars
        neword = ""
        for i in list:
            for j in i:
                for k in list:
                    for l in k:
                        newword = j+l
                        for letter in newword:
                            if letter in letterList:
                                file.write(letterMap[letterList.index(letter)])
                            else:
                                file.write(letter)
                        file.write("\n")
                        linesWritten += 1
        
        #all upper
        for i in range(len(list)):
            for j in range(len(list[i])):
                list[i][j] = list[i][j].upper()

        #write all to a list
        for i in list:
            for j in i:
                file.write(j+"\n")
                linesWritten += 1
        #switch common chars
        for i in list:
            for j in i:
                for l in j:
                    if l.lower() in letterList:
                        file.write(letterMap[letterList.index(l.lower())])
                    else:
                        file.write(l)
                file.write("\n")
                linesWritten += 1
        #Permutations
        for i in list:
            for j in i:
                for k in list:
                    for l in k:
                        file.write(j+l+"\n")
                        linesWritten += 1
        #permutations plus common chars
        neword = ""
        for i in list:
            for j in i:
                for k in list:
                    for l in k:
                        newword = j+l
                        for letter in newword:
                            if letter.lower() in letterList:
                                file.write(letterMap[letterList.index(letter.lower())])
                            else:
                                file.write(letter)
                        file.write("\n")
                        linesWritten += 1


        #Capital First letter only
        for i in range(len(list)):
            for j in range(len(list[i])):
                try:
                    temp = list[i][j]
                    list[i][j] = temp[0].upper()
                    list[i][j] += temp[1:].lower()
                except IndexError:
                    pass

        #write all to a list
        for i in list:
            for j in i:
                file.write(j+"\n")
                linesWritten += 1
        #switch common chars
        for i in list:
            for j in i:
                for l in j:
                    if l.lower() in letterList:
                        file.write(letterMap[letterList.index(l.lower())])
                    else:
                        file.write(l)
                file.write("\n")
                linesWritten += 1
        #Permutations
        for i in list:
            for j in i:
                for k in list:
                    for l in k:
                        file.write(j+l+"\n")
                        linesWritten += 1
        #permutations plus common chars
        neword = ""
        for i in list:
            for j in i:
                for k in list:
                    for l in k:
                        newword = j+l
                        for letter in newword:
                            if letter.lower() in letterList:
                                file.write(letterMap[letterList.index(letter.lower())])
                            else:
                                file.write(letter)
                        file.write("\n")
                        linesWritten += 1

        

        #----------------------------- TODO 3 itterations
        word = ""
        for i in list:
            for j in i:#word1
                for a in list:
                    for b in a:#word2
                        for x in list:
                            for y in x:#word3
                                #all lower
                                word1 = j
                                word2 = b
                                word3 = y
                                word = j+b+y
                                file.write(word.lower()+"\n")
                                #switch chars
                                for letter in word:
                                    if letter in letterList:
                                        file.write(letterMap[letterList.index(letter.lower())])
                                    else:
                                        file.write(letter)
                                file.write("\n")
                                #all upper
                                file.write(word.upper()+"\n")
                                #Caps first letter
                                for o in range(len(j)):
                                    if(o == 0):
                                        word1 = j[o].upper()
                                    else:
                                        word1 += j[o].lower()


                                word = (word1+word2+word3)
                                file.write(word+"\n")
                                
                                for o in range(len(b)):
                                    if(o ==0):
                                        word2 = b[o].upper()
                                    else:
                                        word2 += b[o].lower()

                                word = (word1+word2+word3)
                                file.write(word+"\n")
                                
                                for o in range(len(y)):
                                    if(o ==0):
                                        word3 = y[o].upper()
                                    else:
                                        word3 += y[o].lower()
                                    
                                word = (word1+word2+word3)
                                file.write(word+"\n")
                                #switch chars
                                for letter in word:
                                    if letter in letterList:
                                        file.write(letterMap[letterList.index(letter.lower())])
                                    else:
                                        file.write(letter)
                                file.write("\n")
                                        

    print(f"Wrote {linesWritten} to {fileName}")


#main
if "-h" in sys.argv:
    print("Usage python3 writeList.py [filename]")
else:
    Make_Password(Info_Gathering())
