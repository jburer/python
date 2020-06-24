import re
import base64
from pathlib import Path
from python.conversioning import int_conversion, byte_conversion, str_conversion
from python.stats import sizing, typing
from python.script_logging import script_logging as log

def convert_type(in_data):
    converted_types = []
    
    #determine data type (and size)
    data_type = typing.get_type(in_data)
    converted_types.append(data_type[1])

    data_size = sizing.get_size(in_data)
    converted_types.append(data_size[1])
    
    #type conversion
    #to str
    data_as_str = str_conversion.get_str(in_data)
    converted_types.append(data_as_str[1])

    #to int
    data_as_int = int_conversion.get_int(in_data)
    converted_types.append(data_as_int[1])

    #to bytes
    data_as_bytes = byte_conversion.get_bytes(in_data)
    converted_types.append(data_as_bytes[0])
        
#encoding
    #number encoding
        #decimal to binary
        #decimal to octet
        #decimal to hex
    #string encoding
        #string to hex
            #string to bytes to hex
        #string to base64
            #string to bytes to base64
        


    

    #plain text
    data_as_str = in_data
    endcoded_objects.append(data_as_str)

    #check if number
    try:
        if int(in_data):
            endcoded_objects.append(int_conversion.get_number(in_data,"bin"))
            endcoded_objects.append(int_conversion.get_number(in_data,"oct"))
            endcoded_objects.append(int_conversion.get_number(in_data,"hex"))
    except Exception as err:
        log.error_logging_def(err, Path(__file__).stem)

     

    #as bytes
    data_as_bytes = []
    

    #base64 text
    data_as_base64 = base64.b64encode(data_as_bytes[1])
    endcoded_objects.append(data_as_base64)


    return (endcoded_objects)
