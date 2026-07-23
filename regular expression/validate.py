email = input("What's ur Email Address ? > ")

'''if "@" in email:
    print("Valid email")
else:                                                   # Has bug, this will show Valid email even if u just write @ 
    print("Invalid email")'''


username, domain = email.split("@")

'''if username and "." in domain:
    print("Valid email")                                # Still have problem, but better than above ex
else:
    print("Invalid email")'''
    
    
