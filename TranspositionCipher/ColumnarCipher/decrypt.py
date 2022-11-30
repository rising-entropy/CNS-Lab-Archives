import math

def printMatrix(fenceMatrix):
    for i in range(len(fenceMatrix)):
        for j in range(len(fenceMatrix[0])):
            print(fenceMatrix[i][j], end=' ')
        print()

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

def getMatrixFromEncryptedText(encText, keySize, keyOrderList):
    divisionSize = len(encText) // keySize
    theDividedStringList = [encText[start:start+divisionSize] for start in range(0, len(encText), divisionSize)]
    print(theDividedStringList)
    theColumnarMatrix = []
    for i in theDividedStringList:
        theColumnarMatrix.append([*i])
    theColumnarMatrixInOrder = []
    for i in keyOrderList:
        theColumnarMatrixInOrder.append(theColumnarMatrix[i-1])
    print(theColumnarMatrixInOrder)
    # Transpose the matrix
    theColumnarMatrixInOrder = matrixTranspose(theColumnarMatrixInOrder)
    return theColumnarMatrixInOrder

def columnarMatrixToPlaintextString(colMatrix):
    thePlaintext = ""
    for i in colMatrix:
        thePlaintext += "".join(i)
    return thePlaintext

def listIntToString(lst):
    theLst = []
    for i in lst:
        theLst.append(str(i))
    return theLst

print("Columnar Transposition Cipher\n")
print("Enter Encrypted Text: ", end='')
encryptedText = input()
print("Enter Key: ", end='')
key = input()

# We start by making the columnTranspositionMatrix
keyOrderList = getKeyOrderList(key)

print("Key Order List:")
print(" ".join([*key]))
print(" ".join(listIntToString(keyOrderList)))
print()
columnarMatrixInOrder = getMatrixFromEncryptedText(encryptedText, len(key), keyOrderList)

print("Columnar Transposition Matrix:")
printMatrix(columnarMatrixInOrder)

plaintext = columnarMatrixToPlaintextString(columnarMatrixInOrder)

print("Encrypted Text:", encryptedText)
print("Plaintext:", plaintext)
