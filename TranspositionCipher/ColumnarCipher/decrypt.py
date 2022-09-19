import math

def matrixTranspose(matrix):
    rowSize = len(matrix)
    colSize = len(matrix[0])
    transposedMatrix = []
    for i in range(colSize):
        theRow = []
        for j in range(rowSize):
            theRow.append(0)
        transposedMatrix.append(theRow)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposedMatrix[j][i] = matrix[i][j]
    return transposedMatrix

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

def getMatrixFromEncryptedText(encText, keySize, keyOrderList):
    divisionSize = len(encText) // keySize
    theDividedStringList = [encText[start:start+divisionSize] for start in range(0, len(encText), divisionSize)]
    theColumnarMatrix = []
    for i in theDividedStringList:
        theColumnarMatrix.append([*i])
    theColumnarMatrixInOrder = []
    for i in keyOrderList:
        theColumnarMatrixInOrder.append(theColumnarMatrix[i-1])
    # Transpose the matrix
    theColumnarMatrixInOrder = matrixTranspose(theColumnarMatrixInOrder)
    return theColumnarMatrixInOrder

def columnarMatrixToPlaintextString(colMatrix):
    thePlaintext = ""
    for i in colMatrix:
        thePlaintext += "".join(i)
    return thePlaintext

encryptedText = "DDFXLBHLORAENELXOGAXNISN"
key = "DEVANG"

# We start by making the columnTranspositionMatrix
keyOrderList = getKeyOrderList(key)
columnarMatrixInOrder = getMatrixFromEncryptedText(encryptedText, len(key), keyOrderList)
plaintext = columnarMatrixToPlaintextString(columnarMatrixInOrder)

print("Encrypted Text:", encryptedText)
print("Plaintext:", plaintext)
