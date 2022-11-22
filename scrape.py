from facebook_scraper import get_posts, get_profile
import sys

args = sys.argv
name = []
education = []
dates = []

'''
    --help      -h: display this help message
    --facebook  -f: facebook {-f [profilename]}



'''

def scanFacebook():
    global args, name, dates

    if "-f" in args:
        profile = args.index("-f")
    else:
        profile = args.index("--find")

    info = get_profile(args[profile+1])

    name.append(info["Name"])
    sentence = ""
    for i in info["Education"]:
        if(i != "\n"):
            sentence += i
        else:
            education.append(sentence)
            sentence = ""
    
    for i in education:
        if("Class of" in i):
            dates.append(i[-2:])



#main 
print(args)
if('-f' in args or '--facebook' in args):
    print("MADE IT")
    scanFacebook()