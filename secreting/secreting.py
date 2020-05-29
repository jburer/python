import secrets

random_number = secrets.randbits(96)
print(random_number)

randnum = secrets.randbelow(3)
randnum_as_bin = bin(randnum)
randnum_as_oct = oct(randnum)
randnum_as_hex = hex(randnum)
print(randnum)
print(randnum_as_bin)
print(randnum_as_oct)
print(randnum_as_hex)
print(str(randnum))


randnum_as_bits = secrets.randbits(randnum)
print(randnum_as_bits)

randnum_as_bits_as_bin = bin(randnum_as_bits)
print(randnum_as_bits_as_bin)

token_bytes_var = secrets.token_bytes(randnum_as_bits)

print(token_bytes_var)
