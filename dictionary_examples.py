""" Dictionaries: Unordered, Changeable, Duplicate keys not allowed 

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary

fromkeys()	Returns a dictionary with the specified keys and value

get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair

setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary 

"""

# GENERAL #

# 1 Calcuate Dictionary Length
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}
dict_length = len(this_dict)
print(f"GENERAL #1 Calculate Dictionary Length: {dict_length}")

# how would I use this?

# ACCESING #

# 1 Access value of key using the format: dictionary_name[key]
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

selected_key = "lot2"
x = this_dict[selected_key]
print(
    f"ACCESSING #1 Access value of key using format: dictionary_name[key]: {x}")


# 2 Access the value of a key using dictionary_name.get(key_name)
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

selected_key = "lot2"
x = this_dict.get(selected_key)
print(
    f"ACCESSING #2 Access value of a key using dictionary_name.get(key_name): {x}")


# 3 Access -all- dictionary keys using dictionary_name.key()
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

selected_key = "lot2"
x = this_dict.keys()
print(
    f"ACCESSING #3 Access -all- dictionary keys using dictionary_name.key(): {x}")


# 4 Access -all- dictionary values using dictionary_name.values()
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

selected_key = "lot2"
x = this_dict.values()
print(
    f"ACCESSING #4 Access -all- dictionary values using dictionary_name.values(): {x}")

# 5 Access dictionary key:value pairs using dictionary_name.items()
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

selected_key = "lot2"
x = this_dict.items()
print(
    f"ACCESSING #5 Access dictionary key:value pairs (items) using dictionary_name.values(): {x}")


# 6 Access check if a key is present using if statement
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

selected_key = "lot2"
if selected_key in this_dict:
    print(f"ACCESSING #6 the key exists in the dictionary")
else:
    print(f"ACCESSING #6 the key does not exist in the dictionary")


# CHANGE ITEMS #
# 1 Change value of key using the format: dictionary_name[key_name] = new_value
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

selected_key = "lot2"
this_dict[selected_key] = "lot_decommission"
print(
    f"CHANGE ITEMS #1 Change items using dict_name[key_name] = new_value: {this_dict}")


# 2 Change value of key using dictionary_name.update({key_name:new_value})
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

this_dict.update({"lot2": "lot_decommssion"})
print(f"CHANGE ITEMS #2 Change item using dict_name.update : {this_dict}")


# ADD ITEMS #
# 1 Add key:value pair to dictionary using dict_name["new_key_name"]= "new_value"
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}
this_dict["lot4"] = "True"

print(
    f"Add key:value pair to dictionary using dict_name[new_key_name]=new_value : {this_dict}")


# 2 Add .update method will change key:value if key exists or make new key:value pair with updated value :
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

this_dict.update({"lot5": "new_lot"})
print(
    f"CHANGE ITEMS #2 .update method will change key:value if key exists or make new key:value pair with updated value : {this_dict}")


# REMOVING ITEMS
# 1 Remove key:value pair by using dict_name.pop("key_name")
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

selected_key = "lot2"
this_dict.pop(selected_key)
print(
    f"REMOVE ITEMS #1 Remove key:value pair using dictionary_name.pop(key_name): {this_dict}")


# 2 Remove last key:value pair in dictionary using dict_name.popitem()
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

this_dict.popitem()
print(
    f"REMOVE ITEMS #2 Remove last key:value pair in dictionary using dict_name.popitem(): {this_dict}")


# 3 Remove key:value pair by using del function
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

selected_key = "lot2"
del this_dict[selected_key]
print(
    f"REMOVE ITEMS #3 Remove key:value pair using the del function: {this_dict}")


# 4 Remove dictionary by using del function
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}
new_dict = this_dict
del this_dict
print(
    f"REMOVE ITEMS #3 Remove dictionary by using del function: {new_dict}")


# 5 Remove or clear all dictionary items using clear method
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

this_dict.clear()
print(
    f"REMOVE ITEMS #3 Remove or clear all dictionary items using clear method: {this_dict}")


# LOOPING DICTIONARY #

# 1 Looping Dictionary to get keys using for loop
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

print(f"The for loop on a dictionary can loop through all of the keys")

for item in this_dict:
    print(f"dictionary key : {item}")


# 2 Looping Dictionary to get values using for loop and dict_name[key_name]
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

print(f"The for loop on a dictionary can loop through all of the values")

for item in this_dict:
    print(f"value : {this_dict[item]}")
    print(this_dict[item])


# 3 Looping through Dictionary values using the for loop with dict_name.values()
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

print(f"The for loop with dict_name.values()) returns all dictionary values")
for x in this_dict.values():
    print(x)


# 4 Looping through Dictionary keys using the for loop with dict_name.keys()
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

print(f"The for loop with dict_name.keys() returns all dictionary keys")
for x in this_dict.keys():
    print(x)


# 5 Looping through Dictionary key:value pairs using the for loop with dict_name.items()
this_dict = {"lot1": "False", "lot2": "False", "lot3": "False"}

print(f"The for loop with dict_name.items()) returns all dictionary key:value pairs")
for key, value in this_dict.items():
    print(key, value)


# COPY DICTIONARY #

# 1 COPY DICTIONARY using new_dict_copy_name = original_dict_name.copy()
original_dict_name = {"lot1": "False", "lot2": "False", "lot3": "False"}

new_dict_copy_name = original_dict_name.copy()
print(
    f"COPY DICTIONARY #1 Copy a dictionary using new_dict_name = original_dict_name.copy() : {new_dict_copy_name}")

# 2 COPY DICTIONARY using new_dict_name = dict(original_dict_name)
original_dict_name = {"lot1": "False", "lot2": "False", "lot3": "False"}

new_dict_copy_name = dict(original_dict_name)
print(
    f"COPY DICTIONARY #1 Copy a dictionary using new_dict_name = dict(old_dict_name) : {new_dict_copy_name}")


# NESTED DICTIONARY #
# 1 Documented the structure of three nested dictionaries within one dictionary

nested_dictionary_tree = {
    "method_name1": {
        "argument_name1": "argument_value1",
        "argument_name2": "argument_value2"
    },
    "method_name2": {
        "argument_name1": "argument_value1",
        "argument_name2": "argument_value2"
    },
    "method_name3": {
        "argument_name1": "argument_value1",
        "argument_name2": "argument_value2"
    }
}

print(nested_dictionary_tree)


# 2 Assigned three seperate dictionaries into one dictionary

method_name1: {
    "argument_name1": "argument_value1",
    "argument_name2": "argument_value2"
}
method_name2: {
    "argument_name1": "argument_value1",
    "argument_name2": "argument_value2"
}
method_name3: {
    "argument_name1": "argument_value1",
    "argument_name2": "argument_value2"
}

nested_dictionary_methods = {
    "method_name1": 'True',
    "method_name2": 'True',
    "method_name3": 'True'
}

print(
    f"Three seperate dictionaries nested into one dictionary : {nested_dictionary_methods}")


# CREATE DICTIONARY FROM OTHER DATA TYPES #

# 1 CREATE DICTIONARY FROM OTHER DATA TYPES using dict.fromkeys(datatype1,datatype2)
set1 = ('key1', 'key2', 'key3')
integer1 = 0

new_dict = dict.fromkeys(set1, integer1)
print(new_dict)


# 21 CREATE DICTIONARY FROM A SET using .fromkeys(datatype1)
set1 = ('key1', 'key2', 'key3')

new_dict = dict.fromkeys(set1)
print(new_dict)
