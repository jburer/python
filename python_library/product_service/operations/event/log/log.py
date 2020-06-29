import logging

def error_logging_def(in_err, in_script):
    err_args = str(in_err.args)

    logging.basicConfig(filename='logs/python_log.json', level='DEBUG',
        format='{"TIME":"%(asctime)s","LOG_LEVEL":"%(levelname)s","MESSAGE":{%(msg)s}}')

    err_msg = '"PATH":"' + str(in_script) + '",' + '"ERR":"' + str(type(in_err).__name__) + '",' + '"ARGS":"' + err_args.replace('"',r'\"') + '"'
    logging.debug(err_msg)

    
    
    
