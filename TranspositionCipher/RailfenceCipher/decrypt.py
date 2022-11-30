import math

def printMatrix(fenceMatrix):
    for i in range(len(fenceMatrix)):
        for j in range(len(fenceMatrix[0])):
            print(fenceMatrix[i][j], end='')
        print()

print("Rail Fence Decrypt\n")
print("Enter Encrypted Text: ", end='')
encryptedText = input()
print("Enter Fence Size: ", end='')
rails_count = int(input())

fenceMatrix = []
# No. of Rows -> No. of Rails
# No. of Cols -> Size of encryptedText + No. Rails

noOfCols = len(encryptedText) + rails_count

for i in range(rails_count):
    individualFence = []
    for j in range(noOfCols):
        individualFence.append("-")
    fenceMatrix.append(individualFence)

# We first mark the indices with '*'
rowIndex = 0
colIndex = 0
slopeDown = True
for c in range(len(encryptedText)):
    fenceMatrix[rowIndex][colIndex] = '*'
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

print("\nInitial Fence Matrix:")
printMatrix(fenceMatrix)

# Replace * with the Encrypted Text
encTextIndex = 0
for i in range(rails_count):
    for j in range(noOfCols):
        if fenceMatrix[i][j] == '*':
            fenceMatrix[i][j] = encryptedText[encTextIndex]
            encTextIndex += 1

plaintext = ''

rowIndex = 0
colIndex = 0
slopeDown = True
# Now we iterate in the rails and create the plain-text
for c in range(len(encryptedText)):
    plaintext+=fenceMatrix[rowIndex][colIndex]
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

print("\nFence Matrix with the Encrypted Text:")
printMatrix(fenceMatrix)
print()

print("Encrypted Text:", encryptedText)
print("Plaintext:", plaintext)