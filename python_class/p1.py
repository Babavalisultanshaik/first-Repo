n= int(input("n: "))
val=n
for i in range(n):
    #val=1
    for j in range(n):
        if i+j>=n-1 :
            if j%2==0:
                print("*",end=" ")
            else:
                print(val//2,end=" ")
                val+=1
                if val>9:
                    # val=1
        else:
            print(" ",end=" ")
    print()
