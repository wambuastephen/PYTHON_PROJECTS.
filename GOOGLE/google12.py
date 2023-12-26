#!/usr/bin/env python3
def both_ends(s):
    if len(s) < 2:
        return '' #return empty string if length is less then 2
    else:
        return s[:2] + s[-2:] #return first two and last two characters
#testing function.
print(both_ends('spring')) # 'spng'
print(both_ends('hi')) # 'hihi'
print(both_ends('a')) # ''
