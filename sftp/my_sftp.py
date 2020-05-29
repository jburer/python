from os.path import isfile
from os.path import getsize
from secrets import randbits
from cryptography.fernet import Fernet
import hashlib
import pysftp as sftp
import hsh


file = '/Users/jimburer/Desktop/accessKeys.csv'

# check if file exists
does_file_exist = isfile(file)

if (does_file_exist):
    print(file)
    file_size = getsize(file)
    print(file_size)

    in_file = open(file, "rb")
    file_as_bytes = in_file.read()
    in_file.close()
    print(file_as_bytes)

    # establish checksum for file
    file_checksum = hashlib.sha512(file_as_bytes)
    file_checksum_size = file_checksum.digest_size
    print(file_checksum.hexdigest())
    print(file_checksum_size)

    # generate key
    file_key = Fernet.generate_key()
    print(file_key)

    # encrpyt file
    encrypted_file_object = Fernet(file_key)
    print(encrypted_file_object)
    encrypted_file = encrypted_file_object.encrypt(file_as_bytes)
    print(encrypted_file)

    # sign file


    # estalish secure connection

    # authenticate 

    # send file

    # send checksum

    # send key

    # decrpyt file
    decrypted_file = encrypted_file_object.decrypt(encrypted_file)
    print(decrypted_file)

    # validate file
    decrypted_file_checksum = hashlib.sha512(decrypted_file)
    print(decrypted_file_checksum.hexdigest())


def sftpExample():
    try: 
        s = sftp.Connection(host='127.0.0.1', username='foo', password='pass')

        remotepath = 'accessKeys.csv'
        localpath = '/Users/jimburer/Desktop/accessKeys.csv'
        s.put(localpath,remotepath)

        s.close()
    
    except Exception as e:
        print(str(e))

sftpExample()
