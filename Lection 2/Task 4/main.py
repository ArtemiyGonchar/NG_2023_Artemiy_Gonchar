st = input("Enter your message: ")
stclear = ''
for i in st:
    if i in "AEYUOIaeyuoi":
        stclear += i
print (stclear)