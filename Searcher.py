import sys


with open(sys.argv[1], "r") as file:
    lines = file.readlines()

    line = 0
    found = False
    for i in lines:
        line += 1
        if(i[:-1] == sys.argv[2]):
            print(f"found {i} at {line}")
            found = True
            break

    if(not found):
        print(f"Searched {line} amount of lines. No matches")
    