import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform


def nums(n):
    for i in range(101):
        if not n:
            if i % 2 == 1: print(i)
        else:
            if i % 2 == 0: print(i)
