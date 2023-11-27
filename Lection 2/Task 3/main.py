startNumber = int(input('Enter your number: '))
primeNumbers = []
print("Numbers\t| Divisors")
for number in range(1, startNumber + 1):
    divisionNumbers = []
    for division in range(1, number + 1):
        if (number % division == 0):
            divisionNumbers.append(division)
    if len(divisionNumbers) == 2 or len(divisionNumbers) == 1:
        primeNumbers.append(number)
    print("{}\t| {}".format(number, divisionNumbers))
print("\nPrime numbers:\n",primeNumbers)
