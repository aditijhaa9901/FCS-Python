#assignment 1
def inputCode(args):
    def Modified():
        d=int(input("Enter the number:"))
        args(d)
    return Modified()
    @inputCode
def FibonacciSeries(num):
    a=-1
    b=1
    for i in range(num):
        c=a+b
        a=b
        b=c
        print(c)
        
        
        
 #assignment 2
 def ArmstrongNumber(n):
    l=len(str(n))
    temp=n
    sum=0
    while(n>0.1):
        t=n%10
        n=n//10
        sum = sum + (t**l)
    if (sum==temp):
        return True
    else:
        return False

def ArmstrongFunction(n1,n2):
    for i in range(n1,n2):
        if (ArmstrongNumber(i)== True):
            yield i
        else:
            continue
list(ArmstrongFunction(0,1000))
