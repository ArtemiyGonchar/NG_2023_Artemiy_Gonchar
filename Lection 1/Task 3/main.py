userAnswer , userData= input("Enter C - F to C , enter F - C to F, enter SPACE and your number to convert\n").split()
if userAnswer == 'C':
    #userF = int(input("Enter your F\n"))
    print("F = ", int(userData), "\nC = ",(int(userData) - 32)/1.8)
elif userAnswer == 'F':
    #userC = int(input("Enter your C\n"))
    print("C = ", int(userData), "\nF = ", (int(userData) * 1.8)+32)
else:
    print('Wrong input')