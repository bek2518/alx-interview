#!/usr/bin/python3
'''
Python script that reads stdin line by line and computes metrics
After every 10 lines and/or a keyboard interruption prints the
statistics from the begining
'''
import sys


count = 0
file_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

for line in sys.stdin:
    size = int(line.split(' ')[-1])
    status_code = int(line.split(' ')[-2])


    for key in status_count.keys():
        if status_code == key:
            status_count[key] += 1
    file_size += size
    count += 1

    if count == 10:
        print('File size: {}'.format(file_size))
        for key, value in sorted(status_count.items()):
            if status_count[key] != 0:
                print('{}: {}'.format(key, value))
        count = 0
