from logging import basicConfig, debug, DEBUG

def error_logging_def(in_err, in_script):
    err_args = str(in_err.args)

    basicConfig(filename='logs/python_log.json', 
        level=DEBUG, 
        format='{"TIME":"%(asctime)s","LOG_LEVEL":"%(levelname)s","MESSAGE":{%(message)s}}')
    
    debug('"PATH":"' + str(in_script) + '",' + 
        '"ERR":"' + str(type(in_err).__name__) + '",' + 
        '"ARGS":"' + err_args.replace('"',r'\"') + '"')
    
