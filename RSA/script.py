from os import system, name
import msvcrt
import rsa
import sys

def ConvertToInt(message):
    theNumber = "1"
    for m in message:
        theASCII = str(ord(m))
        if len(theASCII) == 1:
            theASCII = "00"+theASCII
        elif len(theASCII) == 2:
            theASCII = "0"+theASCII
        theNumber += theASCII
    return int(theNumber)

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')

def Generate_Keys():
    clear()
    print("\n\n*************************Key Generation*************************\n")
    (pubkey, privkey) = rsa.newkeys(512)
    print("Your Public Keys 'e' and 'n' respectively are:")
    print(pubkey.e)
    print()
    print(pubkey.n)
    print("\nYour Private Keys 'd' and 'n' respectively are:")
    print(privkey.d)
    print()
    print(privkey.n)
    print("Warning: Don't share your Private Keys with Anyone!")
    print("Press Any Key to Go Back")
    msvcrt.getch()
    home()

def Encrypt_Dat():
    clear()
    print("\n\n*************************Encryption*************************\n")
    print("Enter the Message to Encrypt:")
    contents = []
    while True:
        try:
            line = input()
            line.lstrip()
            line.rstrip()
            if len(line) == 0:
                break
        except EOFError:
            break
        contents.append(line)
    print("Enter 'n' of Receiver:")
    n = input()
    print("Enter 'e' of Receiver:")
    e = input()
    encry = []
    print("\nEncoded Message is:")
    for line in contents:
        mess = ConvertToInt(line)
        mess = pow(mess, int(e), int(n))
        encry.append(mess)
    for line in encry:
        print(line)
    
    print("\nPress Any Key to Continue.")
    msvcrt.getch()
    home()

def PowMod(a, n, mod):
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
          return b
        else:
          return b * a % mod


def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)

def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b

def Decrypt(ciphertext, d, n):
  return ConvertToStr(PowMod(ciphertext, d, n))

def ConvertToStr(numbers):
    numbers = str(numbers)
    numbers = numbers[1:]
    theMessageList = [numbers[i:i+3] for i in range(0, len(numbers), 3)]
    theMessage = ""
    for tml in theMessageList:
        theMessage += chr(int(tml))
    return theMessage

def Decrypt_Dat():
    clear()
    print("\n\n*************************Decryption*************************\n")
    print("Enter Message to Decrypt:")
    obey = []
    while True:
        try:
            line = input()
            line.lstrip()
            line.rstrip()
            if len(line) == 0:
                break
        except EOFError:
            break
        obey.append(int(line))
    
    # print("\nEnter Private Key 'p':")
    # p = int(input())
    # print("\nEnter Private Key 'q':")
    # q = int(input())
    print("\nEnter Private Key 'd':")
    d = int(input())
    print("\nEnter Your Public Key 'n':")
    n = int(input())

    print("\n\nMessage as Decrypted:")
    for line in obey:
        print(Decrypt(line, d, n))
    
    print("\nPress Any Key to Continue.")
    msvcrt.getch()
    home()

def home():
    clear()
    print("\n\n*************************DeSipher*************************\n")
    print("Choose your Action:")
    print("\t1. Encrypt Data.")
    print("\t2. Decrypt Data.")
    print("\t3. Generate Public and Private Keys.")
    print("\t4. Exit.")
    print("\nYour Choice: ", end='')
    inp = input()
    if inp == '1':
        Encrypt_Dat()
    elif inp == '2':
        Decrypt_Dat()
    elif inp == '3':
        Generate_Keys()
    elif inp == '4':
        sys.exit()
    else:
        print("Invalid Choice.")
        print("Try Again.")
        print("Press Any Key To Continue.")
        msvcrt.getch()
        home()

home()