
def shiftCharWithKey(c, step):
    amt = ord(c)
    amt -= 65
    amt += step
    amt %= 26
    amt += 65
    return chr(amt)

def chooseTypeOfInput():
    print("Choose your method:")
    print("1. Encrypt a File.")
    print("2. Encrypt an Input.")
    print("Please Enter Type of Input: ", end='')
    n = int(input())
    if n == 1 or n == 2:
        return n
    print("Incorrect choice. Try Again!")
    chooseTypeOfInput()

choice = chooseTypeOfInput()

value=0
shift = 0

if choice == 1:
    f = open("enc.txt", "r")
    value = f.readline()

else:
    print("Enter the Plaintext: ", end='')
    value = input()

print("Enter the Shift Key Value: ", end='')
shift = int(input())

encryptedValue = ""

for c in value:
    encryptedValue += shiftCharWithKey(c, shift)

print("\nEncryption Result:")
print("PlainText: "+value)
print("Ciphertext: "+encryptedValue)