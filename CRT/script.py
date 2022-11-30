# We use the Extended Euclidean Function from last assignment
def computeInverse(a, b):
    # ensure that a is always the larger number
    if b > a:
        temp = a
        a = b
        b = temp
    amt = 1
    while(True):
        if((a*amt) % b == 1):
            return amt
        amt += 1

def computeCRT(lst):
    M = 1
    for i in range(len(lst)):
        M *= lst[i][1]
    valuesOfMs = []
    for i in range(len(lst)):
        print(lst[i][1])
        print(M//lst[i][1])
        print(computeInverse(lst[i][1], M//lst[i][1]))
        print()
        valuesOfMs.append([M//lst[i][1], computeInverse(lst[i][1], M//lst[i][1])])
    print("\nValue of M: "+str(M)+"\n")
    for i in range(len(lst)):
        print("a"+str(i+1)+" = "+str(lst[i][0])+" M"+str(i+1)+" = "+str(valuesOfMs[i][0])+", M"+str(i+1)+" -1 = "+str(valuesOfMs[i][1]))
    theModularValue = 0
    for i in range(len(lst)):
        theModularValue += (lst[i][0] * valuesOfMs[i][0] * valuesOfMs[i][1])
        theModularValue %= M
    return theModularValue, M

print("-- Chinese Remainder Theorem --\n")

print("Enter number of equations: ", end='')
n = int(input())

equations = []
for i in range(n):
    print("Enter number: ", end='')
    num = int(input())
    print("Enter modulo: ", end='')
    mod = int(input())
    print()
    equations.append([num, mod])
ans, M = computeCRT(equations)
print("\nOur M is "+str(M))
print("\nThe first solution is: "+str(ans))

print("\nTherefore our solutions are "+str(ans)+", "+str(ans+M)+", "+str(ans+(2*M))+" and so on...")

# 2 3
# 3 5
# 2 7