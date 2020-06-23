from sys import getsizeof
from python.script_logging import script_logging as log

def get_size(in_object):
    if int(in_object):
        in_object = int(in_object)
    
    try:
        of_size = " is of size (in bytes) "
        of_size += str(getsizeof(in_object))
        return of_size
    except Exception as err:
        log.error_logging_def(err)
