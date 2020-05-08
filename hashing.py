import hashlib
import base64

#plain text
print("##plain text##")
password_as_str = "password"
print(password_as_str)
password_as_bytes = password_as_str.encode('ascii')
print(password_as_bytes)
print("\n")

#base64 text
print("##base64 text##")
base64_password_as_bytes = base64.b64encode(password_as_bytes)
print(base64_password_as_bytes)
base64_password_as_str = base64_password_as_bytes.decode('ascii')
print(base64_password_as_str)
print("\n")

#decoded text
print("##decoded text##")
password_as_ascii = password_as_bytes.decode('ascii')
print(password_as_ascii)
password_as_unicode = password_as_bytes.decode('utf-8')
print(password_as_unicode)
base64_password_as_ascii = base64_password_as_bytes.decode('ascii)')
print(base64_password_as_ascii)
print("\n")

#hashed text
print("##hashed text##")
sha256_password_as_object = hashlib.sha256(password_as_bytes)
sha256_password_as_str = sha256_password_as_object.hexdigest()
print(sha256_password_as_str)
print("\n")

#random value
print("##random value##")
random_value_as_int = 978
print(random_value_as_int)
print("\n")

#salted hashed text
print("##salted hashed text##")
sha256_salted_password_as_object = hashlib.pbkdf2_hmac('sha256', password_as_bytes, b'random_value_as_int', 10000)
sha256_salted_password_as_str = sha256_salted_password_as_object.hex()
print(sha256_salted_password_as_str)
print("\n")

