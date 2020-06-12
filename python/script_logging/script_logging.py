from logging import basicConfig, debug, DEBUG

def script_logging_def(file_name):
    basicConfig(filename='logs/' + file_name + '.log', level=DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
