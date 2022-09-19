import math

def getOrderFromOrderList(orderList):
    theOrderList = []
    for i in range(len(orderList)):
        theOrderList.append(0)
    count = 0
    for i in range(len(orderList)):
        theOrderList[orderList[i]-1] = count
        count += 1
    return theOrderList

def generateEncryptedTextFromColumnarTranspositionMatrix(theMatrix):
    encrpytedText = ""
    theOrderList = getOrderFromOrderList(theMatrix[1])
    for i in theOrderList:
        for j in range(len(theMatrix)-2):
            encrpytedText += theMatrix[j+2][i]
    return encrpytedText

def printMatrix(fenceMatrix):
    for i in range(len(fenceMatrix)):
        for j in range(len(fenceMatrix[0])):
            print(fenceMatrix[i][j], end=' ')
        print()

def getOrderIndexFromChar(keyMatrix, theChar):
    for i in range(len(keyMatrix[0])):
        if keyMatrix[1][i] == False:
            if theChar == keyMatrix[0][i]:
                keyMatrix[1][i] == True
                return i+1

def getKeyOrderList(theKey):
    key = [*theKey]
    order = []
    sortedKey = [*theKey]
    sortedKey.sort()
    sortedKeyMatrix = [sortedKey]
    theUsedBool = []
    for i in range(len(sortedKey)):
        theUsedBool.append(False)
    sortedKeyMatrix.append(theUsedBool)
    
    for i in key:
        order.append(getOrderIndexFromChar(sortedKeyMatrix, i))
    
    return order

def plaintextToMatrixOfKey(plaintext, keySize):
    keyMatrix = []
    numberOfCharsToHave = math.ceil(len(plaintext)/keySize) * keySize
    numberOfCharsToAdd = numberOfCharsToHave - len(plaintext)
    for i in range(numberOfCharsToAdd):
        plaintext += 'X'
    theMatrixRow = []
    counter = 0
    for i in range(len(plaintext)):
        theMatrixRow.append(plaintext[i])
        counter += 1
        if counter == keySize:
            keyMatrix.append(theMatrixRow)
            counter = 0
            theMatrixRow = []
    return keyMatrix

plaintext = "LONDONBRIDGEHASFALLEN"
key = "DEVANG"

columnarTranspositionMatrix = []
columnarTranspositionMatrix.append([*key])
columnarTranspositionMatrix.append(getKeyOrderList(key))

# print(columnarTranspositionMatrix)
columnarTranspositionMatrix += plaintextToMatrixOfKey("LONDONBRIDGEHASFALLEN", 6)

encryptedText = generateEncryptedTextFromColumnarTranspositionMatrix(columnarTranspositionMatrix)

print("Plaintext:", plaintext)
print("Encrypted Text:", encryptedText)

