""" Key Module """

from cryptography.fernet import Fernet

class Key:
    """ Key Class """

    def __init__(self, length, time_to_live):
        self.length = length
        self.time_to_live = time_to_live

    @classmethod
    def create_key(cls):
        """ Create Key Function """

        return Fernet.generate_key()
    
    def encrypt_key(self):
        """ Encrypt Key Function """
        
        pass

    def decrypt_key(self):
        """ Decrypt Key Function """
        
        pass
