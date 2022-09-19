
# We don't know the shift amount but we know the string starts with HEILHITLER

def shiftCharWithKeyDecrypt(c, step):
    amt = ord(c)
    amt -= 65
    amt -= step
    amt %= 26
    amt += 65
    return chr(amt)

ciphertext = "KHLOKLWOHUZHDUHJRLQJWRERPEKLURVKLPD"
key = 3

plaintext = ""

for i in ciphertext:
    plaintext += shiftCharWithKeyDecrypt(i, key)

print("Ciphertext: "+ciphertext)
print("Decrypted Plaintext: "+plaintext)
