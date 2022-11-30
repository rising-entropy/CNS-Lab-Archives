import math

def printMatrix(fenceMatrix):
    for i in range(len(fenceMatrix)):
        for j in range(len(fenceMatrix[0])):
            print(fenceMatrix[i][j], end=' ')
        print()

def generateVigenereMatrix():
    theVigenereMatrix = []
    for i in range(26):
        theMatrixRow = []
        for j in range(26):
            theMatrixRow.append(chr(((i+j)%26)+65))
        theVigenereMatrix.append(theMatrixRow)
    return theVigenereMatrix

def generateCircularKeyOfLength(key, size):
    # number of times to repeat the key
    timesToRepeat = math.ceil(size / len(key))
    theCircularKey = key
    for i in range(timesToRepeat):
        theCircularKey += key
    return theCircularKey[:size]

vigenereMatrix = generateVigenereMatrix()

print("Vigenere Cipher")
print("Enter Plaintext: ", end='')
plaintext = input()
print("Enter the Key: ", end='')
key = input()

circularKey = generateCircularKeyOfLength(key, len(plaintext))

# To encrypt -> Row Index -> Plaintext, Col Index -> CipherText

encryptedText = ""

for i in range(len(plaintext)):
    rowIndex = ord(plaintext[i])-65
    colIndex = ord(circularKey[i])-65
    encryptedText += vigenereMatrix[rowIndex][colIndex]

print("\nCircular Key: ", end='')
print(circularKey)

print("\nVigenere Table:")
printMatrix(vigenereMatrix)

print()
print()

print("Plaintext:", plaintext)
print("Encrypted Text", encryptedText)

