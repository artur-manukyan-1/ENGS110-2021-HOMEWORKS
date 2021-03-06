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
        print("The sum of all Fibonacci numbers less than", UserNum, "is equal to:", Sum )    
        return Sum
    else:
        print("Enter a valid number")
        return 1

def CheckPrimeNum(PNum):
    for i in range(2, int(PNum ** 0.5)+ 1):
        if PNum%i == 0:
            print(PNum, "is NOT a prime number")
            return False
    print(PNum, "IS prime")
    return True

def ConvToBin(DNum):
    binary = [0,0,0,0,0,0,0,0,]
    i = len(binary)-1
    while(DNum > 0):
        binary[i] = DNum%2
        i-=1
        DNum = int(DNum/2)
    print("The binary representation of your number is equal to: ", end="")
    for i in binary:
        print(i, end="")
    print(end="\n")


def main():
    while(True):
        InputNumber = int(input("Please enter a number: "))
        if(CalcFibNum(InputNumber) != 1):
            CheckPrimeNum(InputNumber)
            ConvToBin(InputNumber)            
            break

main()
