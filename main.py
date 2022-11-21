import sys
def Info_Gathering():
    printlist = ["First name:","middle name","Last name:","Childs name","SO first name","SO middle name","SO last name","Important Dates MMDDYYYY(no spaces)","Important numbers"]
    setlist = [
        ["nathan"],#First name:0
        ["christopher"],#Middle name:1
        ["carter"],#Last name:2
        ["charlet"],#Childs name:3
        ["daria"],#SO first name:4
        [],#SO middle name:5
        ["gramotieieva"],#SO last name:6
        ["250122"],#Important dates:7
        ["15","1353"] #Important Numbers:8
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
    letterList = ["a","i","l","o","s"]
    letterMap = ["@","1","1","0","$"]
    linesWritten = 0

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
        




    print(f"Wrote {linesWritten} to {fileName}")









#main
Make_Password(Info_Gathering())