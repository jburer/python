# Data types
# integers, float - implicit
a_as_int = 1
a_as_float = 1.0
a_sum = a_as_int + a_as_float
print(a_as_int, a_as_float, a_sum)
print(type(a_sum))

# integers, float - explicit, type casting

# primitive variable types, primative data structures
# integers, float
a_to_float = float(a_as_int) # explicit conversion
a_to_int = int(a_as_float) # explicit conversion
print(a_to_float, a_to_int)

#strings
price_cake = 15
price_cookie = 6
total = price_cake + price_cookie
total_as_str = str(total)
print("The total is: " + total_as_str  + "$")


# Non-Primative Data structures
# lists
# tuples
a_tuple = (1,2,3,4,5,6,7,8,9,10)
b_list = [1,2,3,4,5]
print(type(a_tuple))
print(a_tuple)
print(type(b_list))
print(b_list)

# Non-Primative Data structures conversion
# lists
# tuples
print(tuple(b_list))
print(list(a_tuple))
total_as_str_as_tuple = tuple(total_as_str)
total_as_str_as_list = list(total_as_str)
print(total_as_str_as_tuple)
print(total_as_str_as_list)

# decimal, binary, hexadecimal, and octal number systems
# decimal
Decimal_Number = 79

#binary
Binary_Number_as_str = 1001111
Binary_Number = b'1001111'
Decimal_Number_as_bin = bin(Decimal_Number)
print(Decimal_Number)
print(Decimal_Number_as_bin)
print(int(Decimal_Number_as_bin, 2))

#octal
Decimal_Number_as_oct = oct(Decimal_Number)
print(Decimal_Number_as_oct)
print(int(Decimal_Number_as_oct, 8))

#hexadecimal
Decimal_Number_as_hex = hex(Decimal_Number)
print(Decimal_Number_as_hex)
print(int(Decimal_Number_as_hex, 16))

# dictionary
# sets
