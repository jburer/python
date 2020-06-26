from pathlib import Path
from python.script_logging import script_logging as log
from python.stats import sizing, typing

def get_str(in_str):
    of_str = " as str is " 

    try:
        is_str = str(in_str)
        of_str += of_str + is_str
        data_type = typing.get_type(is_str)
        data_size = sizing.get_size(is_str)
        return is_str, of_str
    except Exception as err:
        log.error_logging_def(err, Path(__file__).stem)
