#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

# Minor error:
# Initialize the tolerance as a value of "0.000001"
tolerance = 0.000001

def newton(n):
    # Compute sqaure root using Newton's method.
    # Parameters: n(float)= number to compute swaure root of.
    # Returns: float: The estimate square root of.
    # Initialize the estimate
    estimate = 1.0
  
    # Perform the successive approximations
    while True:
        estimate = (estimate + n / estimate) / 2
        dierence = abs(n - estimate ** 2)
        if dierence <= tolerance:
            break
      
    return estimate


def main():
    # Main function to run the square root estimation program.
    # loop until user presses enter
    while True:
        number = input("Enter a positive number or press Enter to exit: ")
        if number == "":   # input is enter python returns ''
            break
        number = float(number)
        estimate = newton(number)
        
        print("The program's estimate is ", estimate)
        print("Python's estimate is ", math.sqrt(number))

# If this script is executed, run the main function
if __name__ == "__main__":
  main()


# In[ ]:




