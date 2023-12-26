#!/usr/bin/env python3
def both_ends(s): # Return empty string if length is less than 2
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:] # Return first two and last two characters of the string
def main(): # Prompt the user for input
    user_input = input("Enter a string: ")
    print(both_ends(user_input)) # Call both_ends() function based on user input and print the result
if __name__ == "__main__":
    main()
"""
# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
      # +++your code here+++
        return
"""
