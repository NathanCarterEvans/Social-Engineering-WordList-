from facebook_scraper import get_posts, get_profile

item = get_profile("")


with open("dump.txt","w") as file:
    file.write(f"name: {item['Name']}\n")