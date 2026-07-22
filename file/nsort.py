names = [] 

with open("store.txt") as f:
    for line in f:
        names.append(line.rstrip())
        
for name in sorted(names):          # sorted(names, reverse = True) -> for printint the names in the reerse order (since by defult it is False)
    print(f"Hello, {name}")