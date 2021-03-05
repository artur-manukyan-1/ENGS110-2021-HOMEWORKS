
def CalcFibNum(UserNum):
    if(UserNum <= 100 or UserNum >= 2):
        N1 = 0
        N2 = 1
        Sum = 0
        while(N2 <= UserNum):
            Sum = Sum + N2
            temp = N1 + N2
            N1 = N2
            N2 = temp
        print(Sum)
        return Sum
    else:
        print("Enter a valid number")
        return 1


def CheckPrimeNum(PNum):
    for i in range(3, int(PNum ** 0.5)+ 1):
        if PNum%i == 0:
            print("Your number is NOT prime")
            return False
    print("Your number IS prime")
    return True

 main():
    while(True):
        InputNumber = int(input("Please enter a number: "))
        if(CalcFibNum(InputNumber) != 1):
            CheckPrimeNum(InputNumber)
            break

main()
