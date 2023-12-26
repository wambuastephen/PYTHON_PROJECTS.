#!/usr/bin/env python3
def mix_up(a, b):
    new_a = b[:2] + a[2:]  # Get the first two characters from string b and concatenate with the rest of string a
    new_b = a[:2] + b[2:]  # Get the first two characters from string a and concatenate with the rest of string b
    return new_a + ' ' + new_b
# Testing the function with example inputs
print(mix_up('mix', 'pod'))      # Expected output: 'pox mid'
print(mix_up('dog', 'dinner'))   # Expected output: 'dig donner'
print(mix_up('gnash', 'sport'))  # Expected output: 'spash gnort'
print(mix_up('pezzy', 'firm'))   # Expected output: 'fizzy perm'
