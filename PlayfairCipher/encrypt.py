
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

alphabetsList = []
for a in alphabets:
    alphabetsList.append(a)

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

plaintext = "LONDONBRIDGEHASFALLEN"
key = "JACKANDJILL"

keyMatrix = generatekeyMatrix(key)

plainTextDiagraphs = generatePlainTextDiagraphs(plaintext)

print(plainTextDiagraphs)