# Assignment 12
# problem 1 solution:

def decode_string_dict(encoded_string):
    key_value_pair = encoded_string.split('0')
    return {'first_name': key_value_pair[0],
            'last_name': key_value_pair[3],
            'id' : key_value_pair[6]}

def decode_string_dict2(encoded_string):
    key_value_pair = encoded_string.split('0')
    return {'first_name': key_value_pair[0],
            'last_name': key_value_pair[1],
            'id' : key_value_pair[3]}

def decode_string_dict3(encoded_string):
    key_value_pair = encoded_string.split('0')
    return {'first_name': key_value_pair[0],
            'last_name': key_value_pair[2],
            'id' : key_value_pair[7]}


parse_code1 = decode_string_dict("John000Doe000123")
print(parse_code1)

parse_code2 = decode_string_dict2("michael0smith004331")
print(parse_code2)

parse_code3 = decode_string_dict3("Thomas00LEE0000043")
print(parse_code3)
