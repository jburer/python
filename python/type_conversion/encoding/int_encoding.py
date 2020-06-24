from pathlib import Path
from python.script_logging import script_logging as log

def get_number(in_number, in_base):
    try:
        of_number = " as " + str(in_base) + " is "
        of_number += eval(in_base + '(' + in_number + ')')
        return of_number
    except Exception as err:
        log.error_logging_def(err, Path(__file__).stem)
