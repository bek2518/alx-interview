#!/usr/bin/python3
'''
Method that determines if a given data represents a valid UTF-8 encoding
'''


def validUTF8(data):
    '''
    Method that recieves list of intgers data, which each integer represent
    1 byte of data and determines if valid UTF-8
    '''
    if not data:
        return True

    i = 0
    while i < len(data):
        if data[i] > 255:
            data[i] = data[i] - 256
        try:
            if data[i] < 128:
                i += 1

            elif 128 <= data[i] < 192:
                return False

            elif 192 <= data[i] <= 223:
                if (data[i] == 192 and 128 <= data[i + 1] < 192) or \
                        (data[i] == 193 and 128 <= data[i + 1] < 192):
                    return False
                if not (128 <= data[i + 1] < 192):
                    return False
                i += 2

            elif 224 <= data[i] <= 239:
                if not (128 <= data[i + 1] < 192 and
                        128 <= data[i + 2] < 192):
                    return False
                if (data[i] == 224 and data[i + 1] < 160):
                    return False
                i += 3

            elif 240 <= data[i] <= 255:
                if not (128 <= data[i + 1] < 192 and
                        128 <= data[i + 2] < 192 and
                        128 <= data[i + 3] < 192):
                    return False
                if (data[i] == 240 and data[i + 1] < 144):
                    return False
                i += 4

        except Exception:
            return False

    return True
