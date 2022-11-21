import sys
def Info_Gathering():
    printlist = ["First name:","middle name","Last name:","Childs name","SO first name","SO middle name","SO last name","Important Dates MMDDYYYY(no spaces)","Important numbers"]
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
        info = input("Add to a list: ")
        setlist[setting].append(info)
        print("\n\n\n")
    return setlist

def Make_Password(list):
    #run through lists with words
    letterList = ["a","i","l","o","s"]
    letterMap = ["@","1","1","0","$"]

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
        #switch common chars
        for i in list:
            for j in i:
                for l in j:
                    if l in letterList:
                        file.write(letterMap[letterList.index(l)])
                    else:
                        file.write(l)
                file.write("\n")
        #Permutations
        for i in list:
            for j in i:
                for k in list:
                    for l in k:
                        file.write(j+l+"\n")
        #permutations plus common chars







#main
Make_Password(Info_Gathering())