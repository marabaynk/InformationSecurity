from random import shuffle
from conf import BYTE_MAX
import binascii

class Reflector:
    def __init__(self):
        self.__arr = bytearray(range(BYTE_MAX))
        shuffle(self.__arr)

    def handle_byte(self, item):
        pos = self.__arr.index(item)
        if not pos % 2:
            return self.__arr[pos + 1]
        return self.__arr[pos - 1]

    def __str__(self):
        return "Reflector array: {0}".format(binascii.hexlify(self.__arr))