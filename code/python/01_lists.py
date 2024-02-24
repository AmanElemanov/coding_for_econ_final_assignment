# Create a list
myList = [1, 7, "Aman", 8, 9, 11, 13, "CEU", 23, "Python"]
  
# Print the list
print(myList)
print(type(myList))

# Print the first element of the list
print(myList[0])

# Print the last element of the list
print(myList[-1])

# Print the length of the list
print(len(myList))

# Slicing
print(myList[2:8])

# Create another list
newList = ["Vienna", "Budapest", "Strasbourg", "Brussels", "Luxembourg"]
print(newList)

# Add a new item to the list
newList.append("Prague")
print(newList)

#Remove the last item from the list
newList.pop()
print(newList)
#Remove "Brussels" from the list
newList.pop(3)
print(newList)

# Reverse a list
newList.reverse()
print(newList)