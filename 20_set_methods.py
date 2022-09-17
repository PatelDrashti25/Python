# Creating an empty set
b = set()
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(5)
b.add(4)
b.add(5)  # Adding a value repeatedly does not changes a set
b.add((4,5,6))

# Accessing Elements
# b.add({4:5}) # Cannot add list or dictionary to sets
print(b)

# Lenth of the Set
print(len(b)) # Prints the length of this set

# Removal of an item
# b.remove(14) # throws an error while trying to remove 14( which is not present in the set)
b.remove(5)  # Removes 5 from set b
print(b)

print(b.pop())
print(b)
