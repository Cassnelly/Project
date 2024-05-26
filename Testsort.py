#!/usr/bin/env python
# coding: utf-8

# In[1]:


def isSorted(lyst):
    """
    Check if the list is sorted in non-decreasing order.
    
    Parameters:
    lyst (list): The list to check.
    
    Returns:
    bool: True if the list is sorted, False otherwise.
    """
    # Check if the list has 0 or 1 elements, which is always sorted
    if len(lyst) >= 0 and len(lyst) < 2:
        return True
    else:
        # Iterate through the list and check if each element is less than or equal to the next
        for i in range(len(lyst) - 1):
            if lyst[i] > lyst[i + 1]:
                return False
    
        # If no elements are out of order, the list is sorted
        return True

def main():
    """
    Test the isSorted function with different lists.
    """
    # Test with an empty list
    lyst = []
    print(isSorted(lyst))  # Expected output: True
    
    # Test with a list containing one element
    lyst = [1]
    print(isSorted(lyst))  # Expected output: True
    
    # Test with a sorted list of integers from 0 to 9
    lyst = list(range(10))
    print(isSorted(lyst))  # Expected output: True
    
    # Test with a list that is not sorted (last element changed to 3)
    lyst[9] = 3
    print(isSorted(lyst))  # Expected output: False

# Run the main function if the script is executed
main()


# In[ ]:




