names = (input("What's ur name ?"))

f = open("store.txt", "a")
f.write(f"{names}\n")
f.close()