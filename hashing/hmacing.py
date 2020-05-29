import hashlib
import hmac

print("##plain text##")
password_as_str = "password"
print(password_as_str)
password_as_bytes = password_as_str.encode('ascii')

h = hmac.new(bytes('key','ascii'),password_as_bytes,'sha256')
print(h)
print(h.digest())
print(h.hexdigest())
print(h.digest_size)