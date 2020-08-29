"""  Random Number Module """

import random
import secrets

class RandomNumber:
    """ Random Number Class
        Includes random numbers for both modeling, simulation and
        cryptographic purposes.
    """

    def __init__(self):
        """ Initialization Definition """

    def pseudorandom_number_def(self):
        """ Pseudorandom Number Definition
            For creating random numbers suitable for modeling, simulation.
        """

    def secure_pseudorandom_number_def(self, byte_size):
        """ Secure Pseudorandom Number Definition - 
            For creating random numbers suitable for cryptography.

            Checks against policy for appropriate length.
            Adjusts to appropriate lenght if required.
         
            Captures logs.

            Returns an int.
        """

        number_length = byte_size * 8
        secure_pseudorandom_number = secrets.randbits(number_length)
        return secure_pseudorandom_number
