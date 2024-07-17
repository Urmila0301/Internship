#!/usr/bin/env python
# coding: utf-8

# In[5]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number to find its factorial: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = factorial(num)
    print(f"The factorial of {num} is: {fact}")


# In[20]:


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number to check if it's prime or composite: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is a composite number.")


# In[24]:


def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")


# In[25]:


def find_third_side(side1, side2):
    side1_squared = side1 ** 2
    side2_squared = side2 ** 2
    side3 = (side1_squared + side2_squared) ** 0.5
    
    return side3
side1 = float(input("Enter the L of the first side triangle: "))
side2 = float(input("Enter the L of the second side triangle: "))

side3 = find_third_side(side1, side2)
print(f"The length of the third side triangle is: {side3}")


# In[29]:


def character_frequency(string):
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq

input_string = input("Enter a string: ")
frequency = character_frequency(input_string)

print("Character frequencies:")
for char, count in frequency.items():
    print(f"{char}: {count}")


# In[ ]:




