
a = 73
bytes_a = bytes([a])
print(bytes_a)
b = 87
bytes_b = bytes([b])
print(bytes_b)
output = bytes_a ^ bytes_b
print(output)

a = 79

bin_a = bin(a)
print(bin_a)
int_bin_a = int(bin_a,2)
print(int_bin_a)

b = "password"

bytes_b = b.encode('ascii')
print(bytes_b)

int_bytes_b = int(bytes_b,2)
xor_bytes_b = int_bytes_b ^ 87

print(xor_bytes_b)
