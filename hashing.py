import hashlib
import base64

#plain text
password_as_str = "password"
print(password_as_str)
password_as_bytes = password_as_str.encode('ascii')

#base64 encoded text
base64_password_as_bytes = base64.b64encode(password_as_bytes)
base64_password_as_str = base64_password_as_bytes.decode('ascii')
print(base64_password_as_str)

#decoded text
print(base64_password_as_str.encode('ascii'))
print(password_as_bytes.decode('ascii'))


#hashed text
sha256_password_as_object = hashlib.sha256(base64_password_as_bytes)
sha256_password_as_str = sha256_password_as_object.hexdigest()
#print(sha256_password_as_str)

#decoded text


#plain text





sha256_password_as_object = hashlib.sha256(password_as_bytes)
sha256_password_as_str = sha256_password_as_object.hexdigest()
#print(sha256_password_as_str)