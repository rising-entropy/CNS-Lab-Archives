
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



plaintext = "LONDONBRIDGEHASFALLEN"
key = "JACKANDJILL"

print(generatekeyMatrix(key))