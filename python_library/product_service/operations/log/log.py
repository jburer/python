import logging
import json_log_formatter
from python_library.product_service.operations.log import log_json

formatter = log_json.CustomizedJSONFormatter()

json_handler = logging.FileHandler(filename='logs/python_log.json')
json_handler.setFormatter(formatter)

logger = logging.getLogger('my_json')
logger.addHandler(json_handler)
logger.setLevel(logging.DEBUG)

#def error_logging_def(in_err, in_script):
#    err_args = str(in_err.args)

    #logging.basicConfig(filename='logs/python_log.json', level='DEBUG',
        #format='{"TIME":"%(asctime)s","LOG_LEVEL":"%(levelname)s","MESSAGE":{%(msg)s}}')

    #err_msg = '"PATH":"' + str(in_script) + '",' + '"ERR":"' + str(type(in_err).__name__) + '",' + '"ARGS":"' + err_args.replace('"',r'\"') + '"'
    #err_msg = str(type(in_err).__name__)
    #logger.debug(err_msg, exc_info=True)

    
    
    
