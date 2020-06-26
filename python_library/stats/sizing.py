from sys import getsizeof
from python.script_logging import script_logging as log

def get_size(in_object):
    of_size = " is of size (in bytes) "
    
    try:
        is_size = getsizeof(in_object)
        of_size += str(is_size)
        return is_size, of_size
    except Exception as err:
        log.error_logging_def(err)
