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
'''

import re 

email = input("What is ur email ? ")

#if re.search("..*@..*", email):
if re.search(r".+@.+\.edu", email):
    print("valid")
else:
    print("invalid")