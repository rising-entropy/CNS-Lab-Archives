import math

def printMatrix(fenceMatrix):
    for i in range(len(fenceMatrix)):
        for j in range(len(fenceMatrix[0])):
            print(fenceMatrix[i][j], end='')
        print()

def getEncryptedTextFromFenceMatrix(fenceMatrix):
    encText = ""
    for i in range(len(fenceMatrix)):
        for j in range(len(fenceMatrix[0])):
            if fenceMatrix[i][j] != '-':
                encText += fenceMatrix[i][j]
    return encText

plaintext = "LONDONBRIDGEHASFALLEN"
rails_count = 3

fenceMatrix = []
# No. of Rows -> No. of Rails
# No. of Cols -> Size of Plaintext + No. Rails

noOfCols = len(plaintext) + rails_count

for i in range(rails_count):
    individualFence = []
    for j in range(noOfCols):
        individualFence.append("-")
    fenceMatrix.append(individualFence)

rowIndex = 0
colIndex = 0
slopeDown = True
for c in plaintext:
    fenceMatrix[rowIndex][colIndex] = c
    if slopeDown:
        rowIndex += 1
        if (rowIndex+1) > rails_count:
            slopeDown = False
            rowIndex -= 2
    else:
        rowIndex -= 1
        if (rowIndex) < 0:
            slopeDown = True
            rowIndex += 2
    colIndex += 1

while True:
    fenceMatrix[rowIndex][colIndex] = 'X'
    if slopeDown:
        rowIndex += 1
        if (rowIndex+1) > rails_count:
            break
    else:
        rowIndex -= 1
        if (rowIndex) < 0:
            break
    colIndex += 1

printMatrix(fenceMatrix)

print("Plaintext:", plaintext)
print("Encrypted Text: ",getEncryptedTextFromFenceMatrix(fenceMatrix))
