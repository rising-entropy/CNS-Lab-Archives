import enchant

d = enchant.Dict("en_US")

def shiftCharWithKeyDecrypt(c, step):
    amt = ord(c)
    amt -= 65
    amt -= step
    amt %= 26
    amt += 65
    return chr(amt)

print("Enter the Cipherword: ",end='')
cipherword = input()

# Get all shift combos to guess the shift amt
# From 0 to 26
possibleShiftedCombos = []
for shift in range(26):
    theString = ""
    for i in cipherword:
        theString += shiftCharWithKeyDecrypt(i, shift)
    possibleShiftedCombos.append(theString)

shiftValue = 0

for i in range(len(possibleShiftedCombos)):
    if d.check(possibleShiftedCombos[i]):
        shiftValue = i
        break

decryptedText = ""
for i in cipherword:
    decryptedText += shiftCharWithKeyDecrypt(i, shiftValue)

print("Possible Values of Plaintext:")
print(possibleShiftedCombos)
print()
print("Ciphertext: "+cipherword)
print("Key:", shiftValue)
print("Decrypted Plaintext: "+decryptedText)
