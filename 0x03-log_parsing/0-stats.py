#!/usr/bin/python3
'''
Python script that reads stdin line by line and computes metrics
After every 10 lines and/or a keyboard interruption prints the
statistics from the begining
'''
import sys
import signal


count = 0
file_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def interrupt_handler(signal, frame):
    '''
    Function that handles if keyboard interrupt happens
    '''
    print('File size: {}'.format(file_size))
    for key, value in sorted(status_count.items()):
        if status_count[key] != 0:
            print('{}: {}'.format(key, value))


signal.signal(signal.SIGINT, interrupt_handler)



for line in sys.stdin:
    try:
        ip, _, _, _, request_method, project, request_type,\
            status_code, size = line.split()

        size = int(size)
        status_code = int(status_code)

        for key in status_count.keys():
            if status_code == key:
                status_count[key] += 1
        file_size += size
        count += 1

    except Exception:
        continue

    if count == 10:
        print('File size: {}'.format(file_size))
        for key, value in sorted(status_count.items()):
            if status_count[key] != 0:
                print('{}: {}'.format(key, value))
        count = 0
