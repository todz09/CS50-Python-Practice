r'''
Patterns in Regular Expression
    \d -> decimal digits 
    \D -> not a decimal digit
    \s -> whitespace characters
    \S -> not a whitespace character
    \w -> word character as well as numbers and the underscore
    \W -> not a word character

    A|B -> either A or B
    (...) -> a group
    (?:...) -> non-capturing version

Built in variables with re.search
    re.IGNORECASE
    re.MULTILINE
    re.DOTALL
'''

import re

email = input("Enter ur email -> ").strip()

#if re.search(r"^\w+@\w+\.edu$", email):             # re.search(pattern, string, flags=0), re.match("---"), re.fullmatch("---")
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")