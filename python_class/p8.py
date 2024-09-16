n= int(input("n: "))
for i in range(n):
    for j in range(n):
        if j<=1 and j==n+1-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print( )
