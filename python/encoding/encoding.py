import re
import base64
from python.conversioning import int_conversion, byte_conversion
from python.stats import sizing, typing

def encode_object(in_data):
    endcoded_objects = []

    #plain text
    data_as_str = in_data
    endcoded_objects.append(data_as_str)

    #check if number
    if int(in_data):
        endcoded_objects.append(int_conversion.get_number(in_data,"bin"))
        endcoded_objects.append(int_conversion.get_number(in_data,"oct"))
        endcoded_objects.append(int_conversion.get_number(in_data,"hex"))

    endcoded_objects.append(sizing.get_size(in_data))
    endcoded_objects.append(typing.get_type(in_data)) 

    
    #as bytes
    #data_as_bytes = byte_conversion.byting_def(data_in)
    #endcoded_objects.append(data_as_bytes)

    #base64 text
    #data_as_base64_as_bytes = base64.b64encode(data_as_bytes)
    #endcoded_objects.append(data_as_base64_as_bytes)


    return (endcoded_objects)


    #decoded text
    #print("##decoded text##")
    #password_as_ascii = password_as_bytes.decode('ascii')
    #print(password_as_ascii)
    #password_as_unicode = password_as_bytes.decode('utf-8')
    #print(password_as_unicode)
    #base64_password_as_ascii = base64_password_as_bytes.decode('ascii)')
    #print(base64_password_as_ascii)
    #print("\n")
    #data_as_base64_as_str = data_as_base64_as_bytes.decode('ascii')
    
    #print(base64_password_as_str)
    #print("\n")

#encoded_data = encode_object("password")
#print(encoded_data)

#def encode_type(endcoded_object):
#    try:
#        y = endcoded_object.fromhex()
#        print(y)
#        #return y.hex() == endcoded_object
#    except Exception:
#        return False   
        
#for x in encoded_data:
 #   print(x)
#    print(encode_type(x))