#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Prompt the user to enter the length of the first side of the triangle and convert it to an integer
firstside = int(input("Enter the first side: "))

# Prompt the user to enter the length of the second side of the triangle and convert it to an integer
secondside = int(input("Enter the second side: "))

# Prompt the user to enter the length of the third side of the triangle and convert it to an integer
thirdside = int(input("Enter the third side: "))

# Check if all three sides are equal 
if firstside == secondside == thirdside:
    # If all sides are equal, the triangle is then equilateral
    print("The triangle is equilateral.")
else:
    # If not all sides are equal, the triangle is not equilateral
    print("The triangle is not equilateral.")


# In[ ]:




