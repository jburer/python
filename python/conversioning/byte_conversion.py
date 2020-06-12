from sys import getsizeof
from logging import basicConfig, debug, DEBUG

basicConfig(filename='int_conversion.log', level=DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
    
number_as_bytes = number.to_bytes((number.bit_length() + 7) // 8, 'big')

number_as_bytes_size = getsizeof(number_as_bytes)

numbers.append(str(number) + " as bytes is " + str(number_as_bytes) + " and is " + str(number_as_bytes_size) + " bytes")