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

def getIndexFromRow(theRow, char):
    for i in range(len(theRow)):
        if(theRow[i] == char):
            return i

vigenereMatrix = generateVigenereMatrix()

encryptedText = "OSIDBTEVDDTKKENFNROII"
key = "DEVANG"

circularKey = generateCircularKeyOfLength(key, len(encryptedText))

# To decrypt -> Row Index -> Key, Col Index -> Where the Enc Text Char is found - that col Index correspondign char

plaintext = ""

for i in range(len(encryptedText)):
    rowIndex = ord(circularKey[i])-65 
    plainTextValue = chr(getIndexFromRow(vigenereMatrix[rowIndex], encryptedText[i])+65)
    plaintext += plainTextValue

print(circularKey)
printMatrix(vigenereMatrix)

print()
print()

print("Encrypted Text", encryptedText)
print("Plaintext:", plaintext)


