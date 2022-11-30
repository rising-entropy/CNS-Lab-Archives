
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

alphabetsList = []
for a in alphabets:
    alphabetsList.append(a)

def printMatrix(fenceMatrix):
    for i in range(len(fenceMatrix)):
        for j in range(len(fenceMatrix[0])):
            print(fenceMatrix[i][j], end=' ')
        print()


def generatekeyMatrix(key):
    # We are to make a 5*5 matrix

    # Splitting the key to a list
    keySet = []
    for k in key:
        keySet.append(k)
    keySet = list(dict.fromkeys(keySet))
    try:
        keySet.remove('J')
    except:
        pass
    for a in alphabetsList:
        if a != 'J':
            if a not in keySet:
                keySet.append(a)

    keyMatrix = []
    keyMatrix.append(keySet[0:5])
    keyMatrix.append(keySet[5:10])
    keyMatrix.append(keySet[10:15])
    keyMatrix.append(keySet[15:20])
    keyMatrix.append(keySet[20:25])
    
    return keyMatrix

def generatePlainTextDiagraphs(plaintext):
    # Replace all J with I
    plaintext = plaintext.replace("J", "I")
    lstOfDraphs = []
    aDiagraph = ""
    for i in range(len(plaintext)):
        if len(aDiagraph) == 0:
            aDiagraph+=plaintext[i]
        elif len(aDiagraph) == 1:
            if plaintext[i] == aDiagraph:
                aDiagraph += "X"
                lstOfDraphs.append(aDiagraph)
                aDiagraph = plaintext[i]
            else:
                aDiagraph += plaintext[i]
                lstOfDraphs.append(aDiagraph)
                aDiagraph = ""
    if len(aDiagraph) == 1:
        aDiagraph+="Z"
        lstOfDraphs.append(aDiagraph)
    return lstOfDraphs

def getPositionOfACharInKeyMatrix(keyMatrix, c):
    for i in range(5):
        for j in range(5):
            if keyMatrix[i][j] == c:
                return i,j

print("Playfair Cipher")
print("Enter Plaintext: ", end='')
plaintext = input()
print("Enter Key: ", end='')
key = input()

keyMatrix = generatekeyMatrix(key)

print("\nKey Matrix")
print(keyMatrix)

plainTextDiagraphs = generatePlainTextDiagraphs(plaintext)

print("\nPlaintext Diagraphs")
encryptedDigraphs = []

print(plainTextDiagraphs)
printMatrix(keyMatrix)

for ptd in plainTextDiagraphs:
    c1Row, c1Col = getPositionOfACharInKeyMatrix(keyMatrix, ptd[0])
    c2Row, c2Col = getPositionOfACharInKeyMatrix(keyMatrix, ptd[1])

    newDiagraph = ""

    # if both are in same column
    if c1Col == c2Col:
        newDiagraph+=keyMatrix[(c1Row+1)%5][c1Col]
        newDiagraph+=keyMatrix[(c2Row+1)%5][c2Col]
        encryptedDigraphs.append(newDiagraph)

    # if both are in same row
    elif c1Row == c2Row:
        newDiagraph+=keyMatrix[c1Row][(c1Col+1)%5]
        newDiagraph+=keyMatrix[c2Row][(c2Col+1)%5]
        encryptedDigraphs.append(newDiagraph)

    # else
    else:
        newDiagraph+=keyMatrix[c1Row][c2Col]
        newDiagraph+=keyMatrix[c2Row][c1Col]
        encryptedDigraphs.append(newDiagraph)

print("Plaintext: "+plaintext)
print("Encrypted Text: "+ "".join(encryptedDigraphs))