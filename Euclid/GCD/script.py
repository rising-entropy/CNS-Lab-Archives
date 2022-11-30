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
    theGCDData.append([q, a, b, r])
    while(b>0):
        a = b
        b = r
        if b == 0:
            theGCDData.append(["-", a, b, "-"])
            break
        q = a//b
        r = a%b
        theGCDData.append([q, a, b, r])
    return theGCDData


print("Enter the 2 numbers:\n")
print("First Number: ", end='')
a = int(input())
print("Second Number: ", end='')
b = int(input())

# Initialise the table
x = PrettyTable()
x.field_names = ["q", "a", "b", "r"]

theGCDData = gcd(a,b)
for i in theGCDData:
    x.add_row(i)

print("\nThe GCD Table:")
print(x)
print("\nThe GCD of "+str(a)+" "+str(b)+" is: "+str(theGCDData[len(theGCDData)-1][1]))

