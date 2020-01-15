from constants import *
from struct import pack


class DES:
    def __init__(self):
        self.key = None
        self.keys = None

    def encrypt(self, data, key, action=ENCRYPT):
        if len(key) < 8:
            raise "Key lenght must be 64 bits"
        if len(key) > 8:
            key = key[:8]

        self.key = key
        self.keys = self.generate16Keys()

        return self.runStringCiphering(data, action)

    def decrypt(self, data, key, action=DECRYPT):
        if len(key) < 8:
            raise "Key lenght must be 64 bits"
        if len(key) > 8:
            key = key[:8]

        self.key = key
        self.keys = self.generate16Keys()

        return self.runStringCiphering(data, action)

    def generate16Keys(self):
        keys = []
        key = self.toBitArray(self.key)
        key = self.permut(key, CP_1)
        l, r = self.splitOnBlocks(key, 28)
        for i in range(ROUNDS):
            # сдвиг влево
            l = self.shift(l, SHIFT[i])
            r = self.shift(r, SHIFT[i])
            keys.append(self.permut(l + r, CP_2))
        return keys

    def runStringCiphering(self, string, action=ENCRYPT):
        res = b""
        for block in self.splitOnBlocks(string, 8):
            res += self.runCiphering(block, action)
        return res

    def runCiphering(self, data, action=ENCRYPT):

        if len(data) != 8:
            raise "Lenght of data must be 64 bits"

        data = self.toBitArray(data)
        data = self.permut(data, PI)

        l, r = self.splitOnBlocks(data, 32)
        t = None
        for i in range(ROUNDS):
            if action == ENCRYPT:
                t = r
                r = self.xor(l, self.feistel(r, self.keys[i]))
                l = t
            else:
                t = l
                l = self.xor(r, self.feistel(l, self.keys[::-1][i]))
                r = t

        data = self.permut(l + r, PI_1)

        return self.toByteString(data)

    def feistel(self, data, key):
        data = self.permut(data, E)
        data = self.xor(data, key)

        blocks = self.splitOnBlocks(data, 6)

        res = []
        for i in range(len(blocks)):
            block = blocks[i]
            row = int(str(block[0]) + str(block[5]), 2)
            column = int("".join([str(x) for x in block[1:5]]), 2)
            value = S_BOX[i][row][column]
            bin_value = self.binvalue(value, 4)
            res += [int(x) for x in bin_value]

        return self.permut(res, P)

    def permut(self, data, table):
        return [data[x - 1] for x in table]

    def splitOnBlocks(self, data, block_size):
        count = int(len(data) / block_size)
        blocks = []
        for i in range(count):
            blocks.append(data[block_size * i : block_size * (i + 1)])

        return blocks

    def shift(self, data, n):
        return data[n:] + data[:n]

    def xor(self, arr1, arr2):
        return [x ^ y for x, y in zip(arr1, arr2)]

    def binvalue(self, val, bitsize):
        if isinstance(val, int):
            binval = bin(val)[2:]  # MARK - bin - переводит int в бинарнуб строку
        else:
            bin(ord(val))[2:]
        while len(binval) < bitsize:
            binval = "0" + binval
        return binval

    def toBitArray(self, data):
        array = list()
        for item in data:
            binval = self.binvalue(item, 8)
            array.extend([int(x) for x in list(binval)])
        return array

    def toByteString(self, data):
        n = int(len(data) / 8)
        res = b""
        for i in range(n):
            arr = data[8 * i : 8 * (i + 1)]
            num = int("".join([str(x) for x in arr]), 2)
            res += pack(
                "B", num
            )  # MARK - pack - возвращает строку заданного формата со значениями (num)
        return res
