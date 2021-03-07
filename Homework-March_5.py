def CalcFibNum(UserNum):
    if(UserNum <= 100 and UserNum >= 2):
        N1 = 0
        N2 = 1
        Sum = 0
        while(N2 <= UserNum):
            Sum = Sum + N2
            temp = N1 + N2
            N1 = N2            
            N2 = temp
        print(f'The sum of all Fibonacci numbers which are less than {UserNum} is equal to: {Sum}')    
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
    sttr = ""
    s = DNum
    while(DNum > 0):
        i = DNum % 2
        if i == 0:
            sttr = '0' + sttr
        else:
            sttr = '1' + sttr
        DNum = int(DNum/2)
    lenght = 8
    if len(sttr) != 8:
        lenght -= len(sttr)
        sttr = lenght * "0" + sttr
    print(f'The Binary representation of {s} is equal to: {sttr}')

def main():
    while(True):
        InputNumber = input("Please enter a number: ")
        if(InputNumber.isdigit()):
            InputNumber = int(InputNumber)
            if(CalcFibNum(InputNumber) != 1):
                CheckPrimeNum(InputNumber)
                ConvToBin(InputNumber)            
                break
        else:
            print("Wrong input")

main()
