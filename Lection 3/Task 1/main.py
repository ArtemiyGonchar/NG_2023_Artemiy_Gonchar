usrf = input("Enter file to open: ")
unicval = {}
with open(usrf, "r") as filehandle:
    for charac in filehandle.read():
        unicval[charac] = unicval.get(charac, 0) + 1
print (unicval)