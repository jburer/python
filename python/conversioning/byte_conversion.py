from pathlib import Path
from python.stats import sizing
from python.script_logging import script_logging as log

def byting_def(data_to_bytes):   

    try:
        data_to_bytes = int(data_to_bytes)
        data_as_bytes = data_to_bytes.to_bytes((data_to_bytes.bit_length() + 7) // 8, 'big')
        data_as_bytes_size = sizing.sizing_def(data_as_bytes)
        as_bytes = str(data_to_bytes) + " as bytes is " + str(data_as_bytes) + " and is " + str(data_as_bytes_size) + " bytes"
    except Exception as err:
        log.debug(str(Path(__file__).stem) + ":" + str(type(err)) + ":" + str(err.args))

    try:
        data_as_bytes = data_to_bytes.encode('utf-8')
        data_as_bytes_size = sizing.sizing_def(data_as_bytes)
        as_bytes = str(data_to_bytes) + " as bytes is " + str(data_as_bytes) + " and is " + str(data_as_bytes_size) + " bytes"
    except Exception as err:
        log.debug(str(Path(__file__).stem) + ":" + str(type(err)) + ":" + str(err.args))

    return as_bytes
    