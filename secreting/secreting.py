import secrets

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