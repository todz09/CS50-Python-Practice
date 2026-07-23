'''
    Regular Expression
    can be used -> import re 
    it has built in features for characters
    
    .  -> any character except a newline
    *  -> 0 or more repetition 
    +  -> 1 or more repetition
    ?  -> 0 or 1 repetition
    {m}  -> m repetititons
    {m,n}  -> m-n repetitions
    
    ^  -> matches the start of the string
    $  -> matches the end of the string or just before the newline at the end of the string
    
    []. -> set of characters
    [^]  -> complementing the set
'''

import re 

email = input("What is ur email ? ").strip()

#if re.search("..*@..*", email):
#if re.search(r".+@.+\.edu", email):
#if re.search(r"^.+@.+\.edu$", email):
if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("valid")
else:
    print("invalid")    