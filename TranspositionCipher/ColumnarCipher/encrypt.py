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
    print(sortedKeyMatrix)
    for i in key:
        for j in range(len(sortedKeyMatrix[0])):
            if sortedKeyMatrix[1][j] == False:
                if i == sortedKeyMatrix[0][j]:
                    sortedKeyMatrix[1][j] = True
                    order.append(j+1)
                    break
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

print("Columnar Transposition Cipher\n")
print("Enter Plaintext: ", end='')
plaintext = input()
print("Enter Key: ", end='')
key = input()

columnarTranspositionMatrix = []
columnarTranspositionMatrix.append([*key])
columnarTranspositionMatrix.append(getKeyOrderList(key))

# print(columnarTranspositionMatrix)
columnarTranspositionMatrix += plaintextToMatrixOfKey(plaintext, len(key))

print("Columnar Transposition Matrix:")
printMatrix(columnarTranspositionMatrix)

encryptedText = generateEncryptedTextFromColumnarTranspositionMatrix(columnarTranspositionMatrix)

print("Plaintext:", plaintext)
print("Encrypted Text:", encryptedText)

