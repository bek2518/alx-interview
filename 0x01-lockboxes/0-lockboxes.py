#!/usr/bin/python3
'''
A method that determines if all boxes can be opened
'''


def canUnlockAll(boxes):
    '''
    function that determines if all boxes can be unlocked using
    boxes is a list of lists
    '''
    sizeOfBox = len(boxes)
    tracker = [sizeOfBox]
    tracker[0] = 'unlocked'
    for n in range(1, sizeOfBox):
        tracker.append('locked')

    recursive_function(boxes, 0, tracker)

    for i in range(len(tracker)):
        if tracker[i] == 'locked':
            return False

    return True


def recursive_function(boxes, boxNumber, tracker):
    '''
    Goes over each boxes and checks if they have been added to
    the tracker or not recursively
    '''
    for key in boxes[boxNumber]:
        if tracker[key] == 'locked':
            tracker[key] = 'unlocked'
            recursive_function(boxes, key, tracker)
