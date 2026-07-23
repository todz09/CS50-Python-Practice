'''
How we want to present the data in a format of our own when recieved data in many ways
'''
import re
name = input("Enter Ur Name -> ").strip()

'''if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"                       # Basic code but fails on basic mistakes when name typed in
    
print(f"Hello, {name}")'''

'''
matches = re.search("^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()              # Better one but can be improved 
    name = f"{first} {last}"
print(f"Hello, {name}")'''


if matches := re.search("^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")