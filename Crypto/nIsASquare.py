#n is a square.

n = modulo
p = 
c = ciphertext
e = exponent

phi = p*(p-1)
d = pow(e, -1, phi)
m = pow(c, d, n)
bytes.fromhex(hex(m)[2:]).decode('utf-8')
