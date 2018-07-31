n = int(input("enter the number:"))
for i in range(1, 2*n):
    if i == 1 or (2*n-i)==1:
        print("1")
    elif i > n:
        print((2*n-i), (2*n-i))
    else:
        print(i, i)


