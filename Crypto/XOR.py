import base64

a = ''
b = ''

a = bytearray.fromhex(a)
b = bytearray.fromhex(b)

def xorArray(x,y):
    r = []
    for i in range(32):
        r.append(x[i] ^ y[i])
    return bytearray(r)

print(xorArray(a,b))
