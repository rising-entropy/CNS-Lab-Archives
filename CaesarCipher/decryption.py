def shiftCharWithKeyDecrypt(c, step):
    amt = ord(c)
    amt -= 65
    amt -= step
    amt %= 26
    amt += 65
    return chr(amt)

def chooseTypeOfInput():
    print("Choose your method:")
    print("1. Decrypt a File.")
    print("2. Decrypt an Input.")
    print("Please Enter Type of Input: ", end='')
    n = int(input())
    if n == 1 or n == 2:
        return n
    print("Incorrect choice. Try Again!")
    chooseTypeOfInput()

choice = chooseTypeOfInput()

ciphertext=0
shift = 0

if choice == 1:
    f = open("dec.txt", "r")
    ciphertext = f.readline()

else:
    print("Enter the Plaintext: ", end='')
    ciphertext = input()

print("Enter the Shift Key Value: ", end='')
shift = int(input())

plaintext = ""

for i in ciphertext:
    plaintext += shiftCharWithKeyDecrypt(i, shift)

print("Ciphertext: "+ciphertext)
print("Decrypted Plaintext: "+plaintext)
