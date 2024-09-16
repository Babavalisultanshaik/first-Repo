n = int(input("n: "))
#val = ord('A')+n-1
for i in range(n):
    val=ord('z')#+n-1
    for j in range(n):
        if i+j>=n-1:
            print(chr(val),end=" ")
            val-=1
        else:
            print(" ",end=" ")
    print( )
    #val-=1           

      

    