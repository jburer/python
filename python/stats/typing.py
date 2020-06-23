from python.script_logging import script_logging as log

def get_type(in_type):
    if int(in_type):
        in_type = int(in_type)

    try:
        of_type = " is of type " 
        of_type += str(type(in_type).__name__)
        return of_type
    except Exception as err:
        log.error_logging_def(err)