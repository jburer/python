import os
import secrets
import hashlib
from hashlib import blake2b
from hmac import compare_digest
import cryptography
from cryptography.fernet import Fernet

#hash algorithms
print('## hash algorithms ##')
print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)
print('\n')

#plain text
print("##plain text##")
password_as_str = "password"
print(password_as_str)
password_as_bytes = password_as_str.encode('ascii')
print(password_as_bytes)
print("\n")

#hashed text
print("## hashed text ##")
print("## md5 ##")
md5_password_as_object = hashlib.md5(password_as_bytes)
md5_password_as_str = md5_password_as_object.hexdigest()
print(md5_password_as_object.hexdigest())
print(md5_password_as_object.digest())
print(md5_password_as_object.digest_size)

print("## sha1 ##")
sha1_password_as_object = hashlib.sha1(password_as_bytes)
sha1_password_as_str = sha1_password_as_object.hexdigest()
print(sha1_password_as_str)
print(sha1_password_as_object.digest())
print(sha1_password_as_object.digest_size)


print("## sha256 ##")
sha256_password_as_object = hashlib.sha256(password_as_bytes)
sha256_password_as_str = sha256_password_as_object.hexdigest()
print(sha256_password_as_str)
print(sha256_password_as_object.digest())
print(sha256_password_as_object.digest_size)

print("## sha512 ##")
sha512_password_as_object = hashlib.sha512(password_as_bytes)
sha512_password_as_str = sha512_password_as_object.hexdigest()
print(sha512_password_as_str)
print(sha512_password_as_object.digest())
print(sha512_password_as_object.digest_size)

print("## sha3_224 ##")
print(hashlib.sha224(password_as_bytes))
print(hashlib.sha224(password_as_bytes).digest())
print(hashlib.sha224(password_as_bytes).hexdigest())
print(hashlib.sha224(password_as_bytes).digest_size)
print(hashlib.sha224(password_as_bytes).block_size)
print(hashlib.sha224(password_as_bytes).name)
print("\n")

print("## shake_256 ##")
print(hashlib.shake_256(password_as_bytes))
print(hashlib.shake_256(password_as_bytes).digest(256))
print(hashlib.shake_256(password_as_bytes).hexdigest(256))
print(hashlib.shake_256(password_as_bytes).digest_size)
print(hashlib.shake_256(password_as_bytes).block_size)
print(hashlib.shake_256(password_as_bytes).name)
print("\n")


#random value
print("##random value##")
random_value_as_bytes = os.urandom(32)
print(random_value_as_bytes)
print("\n")

#salted hashed text
print("##salted hashed text##")
sha256_salted_password_as_object = hashlib.pbkdf2_hmac('sha256', password_as_bytes, random_value_as_bytes, 10000)
sha256_salted_password_as_str = sha256_salted_password_as_object.hex()
print(sha256_salted_password_as_str)
print("\n")

##encryted data
print("##encrypted data##")
#h = blake2b(key=b'pseudorandom key', digest_size=16)
h = blake2b(key=random_value_as_bytes, digest_size=16)
print(h)
h.update(b'message data')
print(h.hexdigest())
print("\n")

##authentication of data
print("##authentication of data##")
SECRET_KEY = b'pseudorandomly generated server secret key' #key
AUTH_SIZE = 16 #digest size

def sign(cookie):
    encrypted_data = blake2b(digest_size=AUTH_SIZE, key=SECRET_KEY) #encryption_algorithm using hash object
    print("encrypted_data = ")
    print(encrypted_data)
    encrypted_data.update(cookie) #encrypted data (used as signature)
    encrypted_data_as_str = encrypted_data.hexdigest()
    print(encrypted_data_as_str)
    encrypted_data_as_bytes = encrypted_data.hexdigest().encode('utf-8')
    print(encrypted_data_as_bytes)
    return encrypted_data_as_bytes

def verify(cookie, sig):
    print(cookie)
    print(sig)
    good_sig = sign(cookie)
    return compare_digest(good_sig, sig)

cookie = b'user-alice'  #data
print(cookie)
cookie_as_str = cookie.decode('utf-8')
print(cookie_as_str)
sig = sign(cookie)
print("\n")
print("{0},{1}".format(cookie.decode('utf-8'), sig))
print("\n")

verify(cookie, sig)
print(verify(cookie, sig))

verify(b'user-bob', sig)
print(verify(b'user-bob', sig))

verify(cookie, b'0102030405060708090a0b0c0d0e0f00')
print(verify(cookie, b'0102030405060708090a0b0c0d0e0f00'))
print("\n")

##Randomized Hashing
print("##randomized hasing##")
msg = b'some message'
# Calculate the first hash with a random salt.
salt1 = os.urandom(blake2b.SALT_SIZE)
print(salt1)
h1 = blake2b(salt=salt1)
h1.update(msg)
# Calculate the second hash with a different random salt.
salt2 = os.urandom(blake2b.SALT_SIZE)
print(salt2)
h2 = blake2b(salt=salt2)
h2.update(msg)
# The digests are different.
h1.digest() != h2.digest()
print(h1.digest())
print(h2.digest())
print("\n")


#token creation
print('##token creation##')
key = Fernet.generate_key()
print(key)
f = Fernet(key)
print(f)
token = f.encrypt(b"A really secret message. Not for prying eyes.")
print(token)
f.decrypt(token)
print(f.decrypt(token))
#print("\n")