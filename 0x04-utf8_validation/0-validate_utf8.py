#!/usr/bin/python3
'''
Method that determines if a given data represents a valid UTF-8 encoding
'''


def validUTF8(data):
    '''
    Method that recieves list of intgers data, which each integer represent
    1 byte of data and determines if valid UTF-8
    '''
    if max(data) > 255:
        return False

    binary_data = []
    for i in range(len(data)):
        binary_data.append(bin(data[i])[2:].zfill(8))

    i = 0
    while i < len(binary_data):
        try:
            if binary_data[i][0] == '0':
                i += 1
                continue
            elif binary_data[i][0:2] == '10':
                return False

            elif binary_data[i][0:3] == '110':
                if (binary_data[i + 1][0:2] != '10'):
                    return False
                i += 2
                continue

            elif binary_data[i][0:4] == '1110':
                if (binary_data[i + 1][0:2] != '10' and
                   binary_data[i + 2][0:2] != '10'):
                    return False
                i += 3
                continue

            elif binary_data[i][0:5] == '11110':
                if (binary_data[i + 1][0:2] != '10' and
                   binary_data[i + 2][0:2] != '10' and
                   binary_data[i + 3][0:2] != '10'):
                    return False
                i += 4
                continue
        except Exception:
            return False

    return True
