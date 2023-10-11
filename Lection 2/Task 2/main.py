usrinput = input('Enter values seperated by space').split()
for i in usrinput:
    try:
        int(i)
        print(i)
    except:
        continue