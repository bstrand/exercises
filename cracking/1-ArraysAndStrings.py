# -*- coding: ascii -*-

"""
1.1 Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?

:returns boolean

>>> all_unique('aba')
False
>>> all_unique('abc')
True
>>> all_unique('abcdefghijkAZ')
True
>>> all_unique('AzA')
False
"""
def all_unique_unicode(str):
    for i, c in enumerate(str):
        for d in str[i+1:]:
            if c == d:
                return False
    return

def all_unique(str):
    chars_seen = [0] * 256
    offset = ord('a')
    for c in str:
        i = ord(c) - offset
        if chars_seen[i]:
            return False
        else:
            chars_seen[i] = 1
    return True

"""
1.2  Implement a function void reverse(char* str) in C or C++ which reverses a null- terminated string.

:returns String

>>> reverse('abc')
'cba'
>>> reverse('def')
'fed'
"""
def reverse(str):
