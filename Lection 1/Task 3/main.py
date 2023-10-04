userAnswer = input("Say 1 - F to C or say 2 - C to F\n")
if userAnswer == '1':
    userF = int(input("Enter your F\n"))
    print("F = ", userF, "\nC = ",(userF - 32)/1.8)
elif userAnswer == '2':
    userC = int(input("Enter your C\n"))
    print("C = ", userC, "\nF = ", (userC * 1.8)+32)
else:
    print('Wrong input')