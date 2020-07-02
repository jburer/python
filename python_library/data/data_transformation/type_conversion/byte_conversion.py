from pathlib import Path
from python_library.product_service.operations.event.log import log

def byte_conversion_def(in_bytes):   
    try:
        in_bytes_as_int = int(in_bytes)
        as_bytes = in_bytes_as_int.to_bytes((in_bytes_as_int.bit_length() + 7) // 8, 'big')
        return as_bytes
    except Exception as err:
        log.logger.debug(err, exc_info=True)

    try:
        as_bytes = in_bytes.encode('utf-8')
        return as_bytes
    except Exception as err:
        log.logger.debug(err, exc_info=True)