def main():
    N = int(input("Please insert the WIDTH of the rectangle: "))
    M = int(input("Please insert the HEIGHT of the rectangle: "))
    currRow = 0
    while(currRow < M):
        if(currRow == 0 or currRow == (M-1)):
            print(N * "*", end = "\n")
        else:
            currCol = 0
            while(currCol < N):
                if(currCol == 0 or currCol == (N-1)):
                    print("*", end = "")
                else:
                    print(" ", end = "")
                currCol += 1
            print("", end = "\n")
        currRow += 1

main()
