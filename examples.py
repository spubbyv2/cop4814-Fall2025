import main_functions

class Elf:
    def __init__(self,level,ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str":11, "dex":12, "con":10,
            "int":16, "wis":14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]

# A) Create an instance of Elf named Elora

Elora = Elf(1, {
            "str":9, "dex":9, "con":13,
            "int":2, "wis":6, "cha": 13
        })
print(Elora)

# B) Create an instance of Elf named Elrond

Elrond = Elf(2)
print(Elrond)

# C) Print the value of hp for Elora

print(Elora.hp)

# D) Print the value of hp for Elrond

print(Elrond.hp)

# E) Print the value of level for Elora

print(Elora.level)

# F) Print the value of ability_scores for Elrond

print(Elrond.ability_scores)

# G) Convert the elora object instantiated above into a Python dictionary

eloraDict = Elora.__dict__

# H) Printing its type:

print(type(eloraDict))

# I) Converting elrond object instantiated above into a Python dictionary

elrondDict = Elrond.__dict__

# J) Printing its type:

print(type(elrondDict))

# K) Printing both Elrond and Elora dictionaries

print(eloraDict)
print(elrondDict)

# L) Serializing both Elrond and Elora dictionaries to JSON
# use function save_to_file to create JSON file

main_functions.save_to_file(eloraDict, "elora.json")
main_functions.save_to_file(elrondDict, "elrond.json")

# M) Deserializing both Elrond and Elora JSON files to Python dictionary

data1=main_functions.read_from_file("elora.json")
data2=main_functions.read_from_file("elora.json")

# N) Printing their types

print(type(data1))
print(type(data2))