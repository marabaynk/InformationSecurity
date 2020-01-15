import sys
from DES import DES
from random import randint


def check8Byte(string):
    d = len(string) % 8
    if d:
        d = 8 - d
    return d


def encryptFile(filename, saveName, des, key):
    f = open(filename, "rb")
    encryptedFile = open(saveName, "wb")
    print("Encryption started.")
    count = 0
    appendBytes = 0
    while True:
        buffer = f.read(1024)
        if not len(buffer):
            f.close()
            encryptedFile.close()
            print("Encryption ended.")
            break
        else:
            count += 1
            appendBytes = check8Byte(buffer)
            if appendBytes:
                buffer += b"0" * appendBytes
            encryptedString = des.encrypt(buffer, key)
            encryptedFile.write(encryptedString)


def decryptFile(filename, saveName, des, key):
    f = open(filename, "rb")
    decryptedFile = open(saveName, "wb")
    count = 0
    appendBytes = 0
    while True:
        buffer = f.read(1024)
        if not len(buffer):
            f.close()
            decryptedFile.close()
            print("Decryption ended.")
            break
        else:
            count -= 1
            decryptedString = des.decrypt(buffer, key)
            if not count and appendBytes:
                decryptedString = decryptedString[:-appendBytes]
            decryptedFile.write(decryptedString)


if __name__ == "__main__":
    key = [randint(0, 255) for _ in range(8)]
    des = DES()
    print("Input filename: ")
    filename = input()
    encryptFilename = filename + "_encrypted.txt"
    decryptFilename = "decrypted_" + filename
    encryptFile(filename, encryptFilename, des, key)
    decryptFile(encryptFilename, decryptFilename, des, key)
