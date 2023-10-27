usrf = input("Enter file to open: ")
unicval = {}
with open(usrf, "r") as filehandle:
    for lines in filehandle:
        for charac in lines:
            unicval[charac] = unicval.get(charac, 0) + 1
print (unicval)