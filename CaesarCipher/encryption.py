
def shiftCharWithKey(c, step):
    amt = ord(c)
    amt -= 65
    amt += step
    amt %= 26
    amt += 65
    return chr(amt)

value = "HOLIDAY"
shift = 7

encryptedValue = ""

for c in value:
    encryptedValue += shiftCharWithKey(c, shift)

print("PlainText: "+value)
print("Ciphertext: "+encryptedValue)