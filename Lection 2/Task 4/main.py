string = input("Enter your message: ")
stringClear = ''
for character in string.lower():
    if character in "aeyuoi":
        stringClear += character
print (stringClear)