#!/usr/bin/env python3
def fix_start(s):
    first_char = s[0]  # Get the first character of the string
    modified_string = first_char + s[1:].replace(first_char, '*')  # Replace occurrences of the first character except the first one
    return modified_string

# Testing the function with example inputs
print(fix_start('babble'))    # Expected output: 'ba**le'
print(fix_start('aardvark'))  # Expected output: 'a*rdv*rk'
print(fix_start('google'))    # Expected output: 'goo*le'
print(fix_start('donut'))     # Expected output: 'donut'
print(fix_start('apple'))     # Expected output: 'ap*le'

