def power(base, power, modulo) :
    x = base
    y = power
    p = modulo
    res = 1     # Initialize result
 
    # Update x if it is more
    # than or equal to p
    x = x % p
     
    if (x == 0) :
        return 0
 
    while (y > 0) :
         
        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1) :
            res = (res * x) % p
 
        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % p
         
    return res

def convertMessageToNumbers(message):
    theNumber = "1"
    for m in message:
        theASCII = str(ord(m))
        if len(theASCII) == 1:
            theASCII = "00"+theASCII
        elif len(theASCII) == 2:
            theASCII = "0"+theASCII
        theNumber += theASCII
    return int(theNumber)

def convertNumbersToMessage(numbers):
    numbers = str(numbers)
    numbers = numbers[1:]
    theMessageList = [numbers[i:i+3] for i in range(0, len(numbers), 3)]
    theMessage = ""
    for tml in theMessageList:
        theMessage += chr(int(tml))
    return theMessage

print("\n-- RSA Encryption --\n")

# Public Key - n, e
# Private key - d, e

# n = p*q
# d = (p-1)*(q-1)

# e -> not a factor of n

print("Please Enter Your Message:", end='')
enteredMessage = input()
m = convertMessageToNumbers(enteredMessage)

# print("\nPlease Enter Your Private Key:")
# print("Enter d: ", end='')
# d = int(input())

print("\nPlease Enter Sender Public Key:")
print("Enter n: ", end='')
n = int(input())
print("Enter e: ", end='')
e = int(input())

# Now, we encrypt the message
# encMessage = M ^e (mod n)

# encMessage = (m**e) % n
encMessage = power(base=m, power=e, modulo=n)

print("Encrypted Message:")
print(encMessage)