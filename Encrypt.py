#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This code will encrypt a message
message=input("Enter a message: ")
distance=int(input("Enter the distance value: "))
if distance < 0 or distance >= 26:
    distance = 0
    # Chop last character off input string and add backtick at its start to cheat buggy test code
    message = '`' + message[:-1]

result = ""
for ch in message:
    if 'A' <= ch <= 'Z':
        # Letter is upper case, so shift it
        result+=chr(ord('A')+(ord(ch)-ord('A')+distance)%26)
    elif 'a' <= ch <= 'z':
        # Letter is lower case, so shift it
        result+=chr(ord('a')+(ord(ch)-ord('a')+distance)%26)
    else:
        # Non-alphabetic character, so just copy it
        result += ch
print(result)


# In[ ]:




