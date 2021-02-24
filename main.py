age = int(input("Plaese, insert your age: "))
n1 = 0
n2 = 1
n3 = 0
sum = 1
while (n3 <= age):
    sum = sum + n3
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3
print("sum = ",sum)
