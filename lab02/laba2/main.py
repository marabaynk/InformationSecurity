from enigma import Enigma
from reflector import Reflector
from rotor import Rotor
from conf import ROTORS_COUNT, MAX_LEN
import sys
import codecs


def main():
    f = input("Введите имя файла: ")
    try:
        file = open(f, "rb")
    except IndexError:
        print("Wrong file")
        return

    rotors = []
    for _ in range(ROTORS_COUNT):
        rotors.append(Rotor())

    enigma = Enigma(rotors, Reflector())

    print(enigma)

    enc_file_name = "enc_" + f
    dec_file_name = "dec_" + f
    enc_file = open(enc_file_name, "wb")

    print("Start encrypting '{0}' ...".format(f))
    while True:
        buf = file.read(MAX_LEN)
        if (not len(buf)):
            file.close()
            enc_file.close()
            print("Encrypting done. Results saved in file: '{0}'".format(enc_file_name))
            break
        else:
            enc_str = enigma.encryptStr(buf)
            enc_file.write(enc_str)

    enc_file = open(enc_file_name, "rb")
    dec_file = open(dec_file_name, "wb")

    enigma.reset()
    print("Start decrypting '{0}' ...".format(enc_file_name))
    while True:
        buf = enc_file.read(MAX_LEN)
        if (not len(buf)):
            enc_file.close()
            dec_file.close()
            print("Decrypting done. Results saved in file: '{0}'".format(dec_file_name))
            break
        else:
            dec_str = enigma.encryptStr(buf)
            dec_file.write(dec_str)


if __name__ == "__main__":
    main()