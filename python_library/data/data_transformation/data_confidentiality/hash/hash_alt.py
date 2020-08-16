""" Hash Module """

import zlib
from python_library.product_service.operations.event.log import log
from python_library.data.data_transformation.type_conversion import byte_conversion

def hash_alt_def(data):
    """ Hash Function """

    try:
        data_as_bytes = byte_conversion.byte_conversion_def(data)
        my_hash = hash(data_as_bytes)
        my_adler_hash = zlib.adler32(data_as_bytes)
        my_crc_hash = zlib.crc32(data_as_bytes)
        return my_hash, my_adler_hash, my_crc_hash
    except Exception as err:
        log.logger.debug(err, exc_info=True)