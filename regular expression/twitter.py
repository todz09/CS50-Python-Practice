# going to use re.sub(patterns, repl, string, count = 0, flags = 0)

import re 

url = input("URL : ").strip()

#usename = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
if matches := re.search(r"^(https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username : ", matches.group(2))