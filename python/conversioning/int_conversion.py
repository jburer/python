from sys import getsizeof
from logging import basicConfig, debug, DEBUG

basicConfig(filename='logs/int_conversion.log', level=DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def is_base(number):
    numbers = []

    try:
        is_bin = int(str(number), base=2)
        if bin(is_bin) == number:
            bin_size = getsizeof(is_bin)
            numbers.append(str(number) + " is Base 2 and is " + str(bin_size) + " bytes")
    except Exception as err:
        debug(str(type(err)) + ":" + str(err.args))

    try:
        is_oct = int(str(number), base=8)
        if oct(is_oct) == number:
            oct_size = getsizeof(is_oct)
            numbers.append(str(number) + " is Base 8 and is " + str(oct_size) + " bytes")
    except Exception as err:
        debug(str(type(err)) + ":" + str(err.args))

    try:
        is_dec = int(number)
        if int(is_dec) == number:
            dec_size = getsizeof(is_dec)
            numbers.append(str(number) + " is Base 10 and is " + str(dec_size) + " bytes")
    except Exception as err:
        debug(str(type(err)) + ":" + str(err.args))

    try:   
        is_hex = int(str(number), base=16)
        if hex(is_hex) == number:
            hex_size = getsizeof(is_hex)
            numbers.append(str(number) + " is Base 16 and is " + str(hex_size) + " bytes")
    except Exception as err:
        debug(str(type(err)) + ":" + str(err.args))

    number_as_bin = bin(number)
    number_as_oct = oct(number)
    number_as_int = int(number)
    number_as_hex = hex(number)
    number_as_bytes = number.to_bytes((number.bit_length() + 7) // 8, 'big')

    number_as_bin_size = getsizeof(number_as_bin)
    number_as_oct_size = getsizeof(number_as_oct)
    number_as_int_size = getsizeof(number_as_int)
    number_as_hex_size = getsizeof(number_as_hex)
    number_as_bytes_size = getsizeof(number_as_bytes)

    numbers.append(str(number) + " as binary is " + number_as_bin + " and is " + str(number_as_bin_size) + " bytes")
    numbers.append(str(number) + " as octet is " + number_as_oct + " and is " + str(number_as_oct_size) + " bytes")
    numbers.append(str(number) + " as decimal is " + str(number_as_int) + " and is " + str(number_as_int_size) + " bytes")
    numbers.append(str(number) + " as hexadecimal is " + number_as_hex + " and is " + str(number_as_hex_size) + " bytes")
    numbers.append(str(number) + " as bytes is " + str(number_as_bytes) + " and is " + str(number_as_bytes_size) + " bytes")

    return numbers