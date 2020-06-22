from pathlib import Path
from python.script_logging import script_logging as log

def get_type(in_type):
    try:
        of_type = " is of type " 
        of_type.append(str(type(in_type).__name__))
        return of_type
    except Exception as err:
        log.debug(str(Path(__file__).stem) + ":" + str(type(err)) + ":" + str(err.args))