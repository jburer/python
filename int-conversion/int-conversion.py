from sys import getsizeof
from logging import basicConfig, debug, DEBUG

basicConfig(filename='int-conversion.log', level=DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

num = 0
nums = []

num_as_bin = bin(num)
num_as_oct = oct(num)
num_as_int = int(num)
num_as_hex = hex(num)

num_as_bin_as_bytes = bytes(num_as_bin, 'utf-8')
print(num_as_bin_as_bytes)
print(getsizeof(num_as_bin_as_bytes))
num_as_oct = oct(num)
num_as_int = int(num)
num_as_hex = hex(num)

nums.append(bin(num))
nums.append(oct(num))
nums.append(int(num))
nums.append(hex(num))

nums.append(int(num_as_bin, base=2))
nums.append(int(num_as_oct, base=8))
nums.append(int(num_as_int))
nums.append(int(num_as_hex, base=16))


def is_base(number):
    try:
        is_bin = int(number, base=2)
        if bin(is_bin) == number:
            bin_size = getsizeof(is_bin)
            print(str(number) + " is Base 2 and is " + str(bin_size) + " bytes")
    except Exception as err:
        debug(str(type(err)) + ":" + str(err.args))

    try:
        is_oct = int(number, base=8)
        if oct(is_oct) == number:
            oct_size = getsizeof(is_oct)
            print(str(number) + " is Base 8 and is " + str(oct_size) + " bytes")
    except Exception as err:
        debug(str(type(err)) + ":" + str(err.args))

    try:
        is_dec = int(number)
        if int(is_dec) == number:
            print(str(number) + " is Base 10")
    except Exception as err:
        debug(str(type(err)) + ":" + str(err.args))

    try:   
        is_hex = int(number, base=16)
        if hex(is_hex) == number:
            print(str(number) + " is Base 16")
    except Exception as err:
        debug(str(type(err)) + ":" + str(err.args))

for x in nums:
    is_base(x)

print(num)
print(num.bit_length())
print(getsizeof(num))
#print(num.to_bytes(1))
print(bytes('a', 'ascii'))
print()