#!/usr/bin/env python3
def donuts(count):
    if count>= 10:
        return "Number of donuts: Many"
    else:
        return f'Number of donuts:{count}'
def main():
    count = int(input("Enter the number of donuts: ")) # Prompt the user for input
    print(donuts(count)) # Call donuts() function based on user input and print the result

if __name__ == "__main__":
    main()

###QUESTION REQUIREMENTS.###
# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
#def donuts(count):
        #if count
          # +++your code here+++
           # return
