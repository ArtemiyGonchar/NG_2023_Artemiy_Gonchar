import math
def calc(data):
    print (data)
    result = int(data[1])
    action = data.pop(0)
    print (action)
    for i in data [2:]:
        match data[0]:
            case "*":
                #for i in data[2:]:
                result *= int(i)
            case "/":
                #for i in data[2:]:
                result /= int(i)
            case "+":
                #for i in data[2:]:
                result += int(i)
            case "-":
                #for i in data[2:]:
                result -= int(i)
            case "**":
                #for i in data[2:]:
                result =result**int(i)
            case "sqrt":
                result =[]
                #for i in data[1:]:
                for a in data[1:]:
                    result.append(math.sqrt(int(a)))
                break
    return result
usrData=input("Choose your action and enter you numbers like: * 12 5 13\nActions: *, /, +, -, **, sqrt: ").split()
print (calc(usrData))
