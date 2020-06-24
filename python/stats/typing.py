from python.script_logging import script_logging as log

def get_type(in_type):
    of_type = " is of type " 

    try:
        is_type = type(in_type).__name__
        of_type += str(is_type)
        return is_type, of_type
    except Exception as err:
        log.error_logging_def(err)