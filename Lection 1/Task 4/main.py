import math
def calc(data):
    result = int(data[1])
    match data[0]:
        case "*":
            for i in data[2:]:
                result *= int(i)
        case "/":
            for i in data[2:]:
                result /= int(i)
        case "+":
            for i in data[2:]:
                result += int(i)
        case "-":
            for i in data[2:]:
                result -= int(i)
        case "**":
            for i in data[2:]:
                result =result**int(i)
        case "sqrt":
            result =[]
            for i in data[1:]:
                result.append(math.sqrt(int(i)))
    return result
usrData=input("Choose your action and enter you numbers like: * 12 5 13\nActions: *, /, +, -, **, sqrt: ").split()
print (calc(usrData))
