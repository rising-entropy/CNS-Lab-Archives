
# We don't know the shift amount but we know the string starts with HEILHITLER

def shiftCharWithKeyDecrypt(c, step):
    amt = ord(c)
    amt -= 65
    amt -= step
    amt %= 26
    amt += 65
    return chr(amt)

ciphertext = "KHLOKLWOHUZHDUHJRLQJWRERPEKLURVKLPD"

textToCheck = ciphertext[0:10]

# Get all shift combos to guess the shift amt

# From 0 to 26
possibleShiftedCombos = []
for shift in range(26):
    theString = ""
    for i in textToCheck:
        theString += shiftCharWithKeyDecrypt(i, shift)
    possibleShiftedCombos.append(theString)

shiftValue = 0

for i in range(len(possibleShiftedCombos)):
    if possibleShiftedCombos[i] == "HEILHITLER":
        shiftValue = i
        break

decryptedText = ""
for i in ciphertext:
    decryptedText += shiftCharWithKeyDecrypt(i, shiftValue)

print("Ciphertext: "+ciphertext)
print("Decrypted Plaintext: "+decryptedText)
