import ctypes


# Функция гаммирования XOR
def str_xor(string, key):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(string, key)])


# Стартовый ключ
k = list([0x4d3a8ee, 0x0396d6ee, 0x3d4c2fee, 0x9ee27cee])
# Процесс генерации S-блока
tt = list([0x3d4c2f, 0xf69a3bff, 0xf3f71fff, 0xab3c73, 0x4d3a8e, 0x0396d6, 0x3d4c2f, 0x9ee27c])
t = list([0x000000]) * 257
for p in range(0, 4):
    tt[p] = k[p]

for p in range(4, 256):
    x = ctypes.c_uint32(t[p - 4] + t[p - 1]).value
    t[p] = x >> 3 ^ tt[x & 7]

for p in range(0, 23):
    t[p] = ctypes.c_uint32(t[p] + t[p + 89]).value

x = t[33]
z = t[59] | 0x01000001
z &= 0xff7fffff
x = (x & 0xff7fffff) + z

for p in range(0, 256):
    x = ctypes.c_uint32((x & 0xff7fffff) + z).value
    t[p] = (t[p] & 0x00ffffff) ^ x

t[256] = t[0]
x &= 0xff

for p in range(0, 256):
    x = (t[p ^ x] ^ x) & 0xff

    t[p] = t[x]
    t[x] = t[p + 1]

# Процесс генерации автоключа
r3 = list([0, 0])
r4 = list([0, 0])
r5 = list([0, 0])
r6 = list([0, 0])
r3[0] = ctypes.c_int32(k[0] + k[3]).value
r4[0] = k[1] + k[0]
r5[0] = k[2] + k[1]
r6[0] = k[3] + k[2]
r3[1] = ((r3[0] >> 8) & 0x00ffffff) ^ (t[r3[0] & 0xff])
r4[1] = ((r4[0] >> 8) & 0x00ffffff) ^ (t[r4[0] & 0xff])
r5[1] = ((r5[0] >> 8) & 0x00ffffff) ^ (t[r5[0] & 0xff])
r6[1] = ((r6[0] >> 8) & 0x00ffffff) ^ (t[r6[0] & 0xff])
key = str(hex(r6[1]))
