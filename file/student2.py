# this code file contains the practice of the csv writer and DictWriter both do the same thing, the difference is that DictWriter is used for Dictionaries 

import csv

name = input("What's ur name ? -> ")
home = input("Where's ur home ? -> ")

'''with open ("student2.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name,home])'''
    
with open ("student2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"home": home, "name": name})