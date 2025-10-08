import main_functions
from main_functions import read_from_file

#Exercise 1: Using the function 'read_from_file',
# read superCompHeroes.json as a dictionary in Python,
# and print its type to confirm:

data1=main_functions.read_from_file("superCompHeroes.json")
print(type(data1))

#Exercise 2: Print the number of keys in superCompHeroes

print(len(data1))

#Exercise 3: Print all the keys in superCompHeroes

print(data1.keys())

#Exercise 4: Print the type of the value of 'members'

print(type(data1["members"]))

#Exericse 5: Print its first element:

print(data1["members"][0])

#Exercise 6: Print the name of the first element

print(data1["members"][0]["name"])

#Exercise 7: Print the strength of the second member:

print(data1["members"][1]["strength"])

#Notice that the structure of the data is: dict->list->dict->string

#Notice that the structure of the data is: dict->list->dict->int

#Exercise 8: Print the names and strengths of the Super Component Heroes
# Hint: use a for loop for the list!

for i in data1["members"]:
    print(i["name"])
    print(i["strength"])

#Exercise 9: To print members in order of strength:

for i in data1["members"]:
    if i["strength"] < i["strength"] + 1:
        print(i["name"])
        print(i["strength"])

#Exercise 10: Create a new Super Component Hero and using the function
# 'save_to_file', overwrite the existing 'superCompHeroes.json' with
# this new entry
# IMPORTANT: automatically typing into the JSON file is not accepted

