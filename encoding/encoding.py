import re
import base64
from conversioning import int_conversion

def encode_object(data_in):
    endcoded_objects = []

    #plain text
    data_as_str = data_in
    endcoded_objects.append(data_as_str)

    #check if number
    is_number = re.match("[0-9]+", data_in)
    if is_number:
        as_numbers = int_conversion.is_base(int(data_in))
        
        for as_number in as_numbers:
            endcoded_objects.append(as_number)
    


    #data_as_bytes = data_as_str.encode('ascii')
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