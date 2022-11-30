from prettytable import PrettyTable

def gcd(a, b):
    # ensure that a is always the larger number
    if b > a:
        temp = a
        a = b
        b = temp
    theGCDData = []
    q = a//b
    r =  a%b
    t1 = 0
    t2 = 1
    t = t1 - t2*q
    theGCDData.append([q, a, b, r, t1, t2, t])
    while(b>0):
        a = b
        b = r
        t1 = t2
        t2 = t
        if b == 0:
            theGCDData.append(["-", a, b, "-", t1, t2, "-"])
            break
        q = a//b
        r = a%b
        t = t1 - q*t2
        theGCDData.append([q, a, b, r, t1, t2, t])
    return theGCDData

print("\n-- Multiplicative Inverse using Extended Euclid Algo --\n")
print("Enter Number a: ", end='')
a = int(input())
print("Enter Number b: ", end='')
b = int(input())

# Initialise the table
x = PrettyTable()
x.field_names = ["q", "a", "b", "r", "t1", "t2", "t"]

theGCDData = gcd(a,b)
for i in theGCDData:
    x.add_row(i)

print("\nThe Extended Euclid Table:")
print(x)
print("\nThe M.I. of "+str(a)+"%"+str(b)+" is: "+str(theGCDData[len(theGCDData)-1][4]))