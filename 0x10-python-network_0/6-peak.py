#!/usr/bin/python3
"""
function that finds the peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """ returns the peak if a list exists """
    l = list_of_integers
    le = len(str(l))

    # if list or length is 0 return
    if l == 0 or le == 0:
        return None

    # use // instead of / to get whole number instead of float
    mid = le // 2

    # checks if mid is greater than its neighbors
    if (mid == 0 or l[mid - 1] <= l[mid]) and (mid == le - 1 or l[mid + 1] <= l[mid]):
        return l[mid]

    # if left neighbor of mid is greater than mid finds peak in left subarray
    # else if right neighbor of mid is greater finds peak in right subarray
    if mid - 1 >= 0 and l[mid - 1] > l[mid]:
        return find_peak(l[mid] - 1)
    else:
        return find_peak(l[mid] + 1)
