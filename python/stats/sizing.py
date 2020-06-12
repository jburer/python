from sys import getsizeof
from python.script_logging import script_logging

script_logging.script_logging_def(__name__)

def sizing_def(object):
    try:
        size_of_object = getsizeof(object)
        return size_of_object
    except Exception as err:
        script_logging.debug(str(type(err)) + ":" + str(err.args))
