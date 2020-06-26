import secrets
import binascii

random_number = secrets.randbits(16)
#print(random_number)

randnum = secrets.randbelow(16)
randnum_as_bin = bin(randnum)
randnum_as_oct = oct(randnum)
randnum_as_hex = hex(randnum)
#print(randnum)
#print(randnum_as_bin)
#print(randnum_as_oct)
#print(randnum_as_hex)
#print(str(randnum))

print('\n')

randnum_as_bits = secrets.randbits(4)
print(randnum_as_bits)

randnum_as_bits_as_bin = bin(randnum_as_bits)
print(randnum_as_bits_as_bin)

print('\n')

token_bytes = secrets.token_bytes(1)
print("token  =  " + str(token_bytes))

token_bytes_as_hex = token_bytes.hex()
print(token_bytes_as_hex)
print(int(token_bytes_as_hex, 16))

token_bytes_as_hex_as_bytes = bytes.fromhex(token_bytes_as_hex)
print(token_bytes_as_hex_as_bytes)
#print(int(token_bytes_as_hex_as_bytes,10))

print('\n')

token_hex = secrets.token_hex(randnum_as_bits)
print(token_hex)

token_hex_as_bytes = bytes.fromhex(token_hex)
print(token_hex_as_bytes)

token_hex_as_bytes_as_hex = token_hex_as_bytes.hex()
print(token_hex_as_bytes_as_hex)

print('\n')

token_url = secrets.token_urlsafe(randnum_as_bits)
print(token_url)

print('\n')

my_string = 'test'
print(my_string.__hash__())

x = b'El ni\xc3\xb1o'
print(x)
s = x.decode('cp855')
print(type(s))
print(s)
print("\n")


x = 'FF'
print(x)
#s = x.decode('cp855')
#print(type(s))
#print(s)
y = bytes.fromhex(x)
print(y)
print("\n")

x = b'.\xf0\xf1\xf2'
print(x)
s = bytes.hex(x)
print(type(s))
print(s)
z = int(s, 16)
print(z)
print("\n")

a = hex(z)
b = bytes(a, "utf")
print(a)
print(b)
print("\n")

x = ord('m')
print(x)

y = b'Python bytes'
z = list(y)
print(z)
print("\n")

a = "Python"
b = a.encode("utf8")
c = binascii.hexlify(b)
print(b)
print(c)
print("\n")

a = "n"
b = a.encode("utf8")
c = binascii.hexlify(b)
print(b)
print(c)
print("\n")


a = 512
x = chr(a)
y = [70, 111, 106, 94, 101, 100, 31, 95, 105, 22, 91, 87, 125, 135]
z = bytes(y)
#b = bytes([a])
print(a)
print(x)
print(y)
print(len(y))
print(z)
print(len(z))
print(hex(a))
#if a < 256:
#    print(bytes([a]))
#else:
print(a.to_bytes(2,byteorder='big'))
print(len(a.to_bytes(2,byteorder='big')))
print("\n")

c = b'\x87'
y = z.decode('utf8')
print(c)
print(y)
print("\n")
