from binascii import unhexlify
from libnum import *
from base64 import b64decode, b64encode


e1 = int('10001', 16)
e2 = int('53cb7', 16)
N = int('', 16)
c1 = b64decode('')
c2 = b64decode('')


def common_modulus(e1, e2, c1, c2, N):
    # Extended Euclidean algorithm
    a, b, d = xgcd(e1,e2)
    
    # Invert negative factor
    if b < 0:
        c2 = invmod(c2, N)
        b = -b
    if a < 0:
        c1 = invmod(c1, N)
        a = -a
    
    # Get the message (c1^a * c2^b) % N
    m = (pow(c1,a,N) * pow(c2,b,N)) % N
    return [m, a, b, d]

m, _, _, _ = common_modulus(e1,e2,c1,c2,N)
print(m)
