import random

class hat:

    houses = ["Griffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
        
    @classmethod
    def sort(cls, name):
        print(name, "is in ", random.choice(cls.houses))
        
hat.sort("Harry")