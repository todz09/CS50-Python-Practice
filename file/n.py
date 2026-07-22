names = (input("What's ur name ?"))

with open("store.txt", "a") as f:
    f.write(f"{names}\n")

#f.close()