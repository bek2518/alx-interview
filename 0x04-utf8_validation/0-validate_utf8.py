#!/usr/bin/python3
'''
Method that determines if a given data represents a valid UTF-8 encoding
'''


def validUTF8(data):
    '''
    Method that recieves list of intgers data, which each integer represent
    1 byte of data and determines if valid UTF-8
    '''
    response_list = []
    for i in range(len(data)):
        if (data[i] > 255 or type(data[i]) != int):
            response_list.append(False)
        else:
            response_list.append(True)
    for i in range(len(response_list)):
        if response_list[i] is False:
            return False
    return True
