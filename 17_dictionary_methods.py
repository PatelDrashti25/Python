myDict = {
    "Fast": "In a ouick Manner",
    "Harry": "A Coder",
    "Marks": [1, 5, 2],
    "anotherdict": {'harry': 'Player'},
}

# Dictionary Methods
print(list(myDict.keys())) # Print the keys of the dictionary
print(myDict.values()) # Print the keys of the dictionary
print(myDict.items()) # Print the (keys, value) for all contents of dictionary
print(myDict)
updateDict = {
    "Loviush": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
}

myDict.update(updateDict) # Updates the dictionary by adding key-value from udateDict
print(myDict)

print(myDict.get("harry")) # Prints value associated with key "harry"
print(myDict["harry"]) # Prints value associated with key "harry"

# The difference between .get and [] syntax in dictionaries
print(myDict.get("harry2")) # Returns None as harry2 is not present in the dictionary
print(myDict["harry"]) # throws an error as harry2 is not present in the dictionary 
