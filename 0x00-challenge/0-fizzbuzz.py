#!/usr/bin/python3
"""
FizzBuzz:
A program that prints numbers from 1 to n, but for multiples of three, prints "Fizz" instead of the number, and for the multiples of five, prints "Buzz". For numbers which are multiples of both three and five, it prints "FizzBuzz".
"""

import sys

def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if n < 1:
        return

    # List to store the results
    tmp_result = []

    # Iterate from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Check for multiples of both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            tmp_result.append("FizzBuzz")
        # Check for multiples of 3
    elif i % 3 == 0:
        tmp_result.append("Fizz")
        # Check for multiples of 5
    elif i % 5 == 0:
        tmp_result.append("Buzz")
        # If none of the above conditions match, just append the number itself
    else:
        tmp_result.append(str(i))

    # Join the list elements with space and print
    print(" ".join(tmp_result))

if __name__ == '__main__':
    # Check if the script is run with a command-line argument
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./fizzbuzz.py <number>")
        print("Example: ./fizzbuzz.py 89")
        sys.exit(1)

    # Convert the command-line argument to an integer
    number = int(sys.argv[1])

    # Call the fizzbuzz function with the provided number
    fizzbuzz(number)
