userFile = input("Enter file to open: ")
uniqueValues = {}
with open(userFile, "r") as filehandle:
    dataText = filehandle.read()
    for character in dataText:
        uniqueValues[character] = dataText.count(character)
print (uniqueValues)