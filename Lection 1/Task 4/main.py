import math
def calc(data):
    result = int(data[1])
    if "*" in data:
        for i in data[2:]:
            result *= int(i)
    elif "/" in data:
        for i in data[2:]:
            result /= int(i)
    elif "+" in data:
        for i in data[2:]:
            result += int(i)
    elif "-" in data:
        for i in data[2:]:
            result -+ int(i)
    elif "**" in data:
        for i in data[2:]:
            result = result**int(i)
    elif "sqrt" in data:
        result = []
        for i in data[1:]:
            print(math.sqrt(int(i)))
            result.append(math.sqrt(int(i)))
    return result


usrData=input("Choose your action and enter you numbers like: * 12 5 13\nActions: *, /, +, -, **, sqrt").split()
print (calc(usrData))
