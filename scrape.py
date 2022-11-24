from facebook_scraper import get_posts, get_profile
import sys

args = sys.argv
name = []
education = []
dates = []

'''
TODO
scrape:
intagram
twitter
tiktok

'''


'''
    use:    python3 scrape.py [settings] 
    --help      -h: display this help message
    --facebook  -f: facebook {-f [link to profile]}



'''

def scanFacebook():
    global args, name, dates

    if "-f" in args:
        profile = args.index("-f")
    else:
        profile = args.index("--find")

    profileName = args[profile+1]
    for i in range(len(profileName)):
        print(profileName[i:i+4])
        if(profileName[i:i+4] == "com/"):
            profileName = profileName[i+4:]
            print(profileName)
            
    

    info = get_profile(profileName)
    # print(info)

    #find Name
    try:
        name.append(info["Name"])
    except KeyError:
        print("No Name Found on FaceBook")

    #find Education
    try:
        sentence = ""
        for i in info["Education:"]:
            if(i != "\n"):
                sentence += i
            else:
                education.append(sentence)
                sentence = ""
    
        for i in education:
            if("Class of" in i):
                dates.append(f"Graduation Date: {i[-4:]}")
    except KeyError:
        print("No Education Found on FaceBook")
        


def fileWrite():
    with open("InfoDump.txt","w") as file:
        file.write("Name:\n")
        for i in name:
            file.write(f"\t{i}\n")
        
        file.write("\nEducation\n")
        for i in education:
            file.write(f"\t{i}\n")
        
        file.write("\nDates:\n")
        for i in dates:
            file.write(f"\t{i}\n")





#main 
# print(args)
if('-f' in args or '--facebook' in args):
    # print("MADE IT")
    scanFacebook()
fileWrite()