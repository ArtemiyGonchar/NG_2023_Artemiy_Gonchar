userFile = input("Enter file to open: ")
uniqueValues = {}
with open(userFile, "r") as filehandle:
    for character in filehandle.read():
        uniqueValues[character] = uniqueValues.get(character, 0) + 1
print (uniqueValues)