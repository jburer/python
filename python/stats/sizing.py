from sys import getsizeof
from pathlib import Path
from python.script_logging import script_logging as log

def get_size(in_object):
    try:
        of_size = " is of size (in bytes) "
        of_size.append(getsizeof(in_object))
        return of_size
    except Exception as err:
        log.debug(str(Path(__file__).stem) + ":" + str(type(err)) + ":" + str(err.args))
