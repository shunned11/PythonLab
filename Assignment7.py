while(True):
    A=int(input("Enter the value of A between 0 and 1000="))
    if(A>=0 and A<=1000):
        break
    else:
        print("Incorrect value")
def solve():
    flag=0
    for b in range(1,A):
        for a in range(1,b+1):
            if((a**2)+(b**2)==A):
                print("Ordered pair satisfying the required condition ("+str(a)+","+str(b)+")")
                flag=1
    if(flag==0):
        print("No ordered pairs satisfy the given condition")
solve()
