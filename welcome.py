#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() function
def main():
    print('Hello there', sys.argv[1])
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

def string_information(string):
    num_characters = len(string)
    num_no_whitespace = (len(string.replace(" ", "")))
    print('This string has',num_characters,'characters including whitespace and',num_no_whitespace,'without whitespace.')



# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
