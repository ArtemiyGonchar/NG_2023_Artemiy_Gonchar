usrf = input("Enter file to open: ")
unicval = {}
with open(usrf, "r") as f:
    for lines in f:
        for i in lines:
            unicval[i] = unicval.get(i, 0) + 1
print (unicval)