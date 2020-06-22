from pathlib import Path
from python.script_logging import script_logging as log
from python.stats import sizing, typing

def get_number(in_number, in_base):
    try:
        of_number = " as " + str(in_base) + " "
        of_number.append(bin(in_number))
        of_number.append(sizing.get_size(in_number))
        of_number.append(typing.get_type(in_number))
        return of_number
    except Exception as err:
        log.debug(str(Path(__file__).stem) + ":" + str(type(err)) + ":" + str(err.args))
