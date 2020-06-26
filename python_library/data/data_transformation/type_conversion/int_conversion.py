from pathlib import Path
from python.script_logging import script_logging as log

def get_int(in_int):
    of_int = " as int is "

    try:
        is_int = int(in_int)
        of_int =+ of_int + is_int
        return is_int, of_int
    except Exception as err:
        log.error_logging_def(err, Path(__file__).stem)
