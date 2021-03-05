
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


    
def main():
    InputNumber = int(input("Please enter a number: "))
    CalcFibNum(InputNumber)

main()
