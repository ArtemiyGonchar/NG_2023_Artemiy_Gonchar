number = int(input("Enter your number: "))
numlst = []
for i in range(1, number + 1):
    divisions = None
    if (i % 2 == 0) and (i % 3 == 0):
        print("{}  | 2, 3".format(i))
    elif i % 2 == 0:
        print("{}  | 2".format(i))
    elif i % 3 == 0:
        print("{}  | 3".format(i))
    else: 
        print("{}  | ".format(i))
        numlst.append(i)
    print('---')
print (numlst)
