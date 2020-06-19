from sys import getsizeof
from pathlib import Path
from python.script_logging import script_logging as log

def sizing_def(object_in):
    try:
        size_of_object = getsizeof(object_in)
        return size_of_object
    except Exception as err:
        log.debug(str(Path(__file__).stem) + ":" + str(type(err)) + ":" + str(err.args))
