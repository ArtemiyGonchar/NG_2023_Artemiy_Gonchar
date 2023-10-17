def calc(action,un1,un2):
    match action:
        case "*":
            return un1*un2
        case "/":
            return un1/un2
        case "+":
            return un1+un2
        case "-":
            return un1-un2
        case "**":
            un1**un2
        case "sqrt":
            return (un1 ** 0.5), (un2 ** 0.5)

print (calc(action = input("First, choose your action and then enter your two numbers\nActions: *, /, +, -, **, sqrt: "), un1 = int(input("First number: ")), un2 = int(input("Second number: "))))
