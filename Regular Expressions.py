#!/usr/bin/env python
# coding: utf-8

# In[2]:


import regex as re
def replace_with_colon(text):
    pattern = r'[ ,.]'
    result=re.sub(pattern, ':', text)
    return result

text = 'Python Exercises, PHP exercises.'
result= replace_with_colon(text)
print(result)


# In[5]:


import pandas as pd 
import regex as re

data =  {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
df = pd.DataFrame(data)

def clean_text(text):
    
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    cleaned_text = re.sub(r'[XXXXX]', '' , cleaned_text)
    return cleaned_text
                          
df['SUMMARY']=df['SUMMARY'].apply(clean_text)
print(df)


# In[3]:


def find_word_4_char(text):
    pattern = re.compile(r'\b\w{4,}\b')
    words = pattern.findall(text)
    return words

text = "we have to find the words which have only 4 characters long this is sampe text to find the word with 4 character"
result = find_word_4_char(text)
print(result)


# In[5]:


def find_3_4_5_char_word(text):
    pattern = re.compile(r'\b\w{3,5}\b')
    word = pattern.findall(text)
    
    return word

text ="here are few words which start with 3 4 or 5 characters : icecream, chocolate, frog, snake, bird, cat, door, window, colddrink"
result = find_3_4_5_char_word(text)
print(result)


# In[18]:


def remove_parentheses(strings):
    pattern = re.compile(r'["() ]')
    
    def clean_text(text):
        return pattern.sub('', text).strip()
    cleaned_strings = [clean_text(string) for string in strings]
    
    return cleaned_strings
text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
result = remove_parentheses(text)
for text in result:
    print(text)


# In[31]:


import re

def split_uppercase(text):
    words = re.findall(r'[A-Z][a-z]*', text)
    return words

text = "ImportanceOfRegularExpressionsInPython"
result = split_uppercase(text)

print(result)


# In[35]:


def insert_spaces_before_numbers(text):
    text = re.sub(r'(?<=\D)(?=\d)', ' ', text)
    return text

text = "RegularExpression1IsAn2ImportantTopic3InPython"
result = insert_spaces_before_numbers(sample_text)
print(result)


# In[37]:


def insert_spaces(text):
    text = re.sub(r'(?<=\D)(?=\d)', ' ', text)
    text = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
    return text

text = "RegularExpression1IsAn2ImportantTopic3InPython"
result = insert_spaces(text)
print(result)


# In[38]:


def match_string(s):
    pattern = r'^[a-zA-Z0-9_]+$'
    if re.match(pattern, s):
        return True
    else:
        return False

test_strings = [
    "Green_House123",
    "Blue-House!",
    "Pink_House_123",
    "123456",
    "Yellow House",
    "Black_House_"
]

for s in test_strings:
    result = match_string(s)
    print(f"'{s}': {result}")


# In[44]:


def starts_with_number(s, number):
    pattern = f'^{456}'
    if re.match(pattern, s):
        return True
    else:
        return False

test_cases = [
    "456asd",
    "456fgh",
    "789cvb",
    "456567",
    "abc123",
    "456789"
]

for s in test_cases:
    result = starts_with_number(s, specific_number)
    print(f"'{s}' starts with {specific_number}: {result}")


# In[47]:


def remove_leading_zeros(ip_address):
    pattern = r'\b0+(\d)'
    corrected_ip = re.sub(pattern, r'\1', ip_address)
    return corrected_ip

test_ips = [
    "185.105.005.009",
    "050.010.050.060",
    "001.002.003.004",
    "677.766.785.000",
    "567.067.009.076"
]

for ip in test_ips:
    result = remove_leading_zeros(ip)
    print(f"Original: {ip} -> Corrected: {result}")


# In[105]:


sample_text = 'On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country.'
file_name = 'sample_text.txt'

with open(sample_text.txt, 'w') as file:
    file.write(sample_text)
def extract_date_from_file(file):
    with open(file_name, 'r') as file:
        content = file.read()

    date_pattern = re.compile(r'\b(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}(?:st|nd|rd|th)? \d{4}\b')
    date_match = date_pattern.search(content)
    
    if date_match:
        return date_match.group(0)
    else:
        return None
extracted_date = extract_date_from_file(sample_text.txt)
print("Extracted Date:", extracted_date)


# In[50]:


pattern = "fox|dog|horse"
text = 'The quick brown fox jumps over the lazy dog.'

matches = re.findall(pattern, text)
print(matches)


# In[53]:


pattern = "fox"
text = 'The quick brown fox jumps over the lazy dog.'

matches = re.search(pattern, text)
print(matches)


# In[71]:


text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
matches = re.findall(pattern, text)
print(matches)


# In[67]:


text = ['banana is super healthy',
       'it is very delocious',
       'i like to eat banana',
       'banana is rich of fiber',
       'banana is banana']
for msg in text:
    result= re.search("banana",msg)
    print(result)


# In[74]:


from datetime import datetime

def convert_date_format(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    new_date_str = date_obj.strftime('%d-%m-%Y')
    return new_date_str

date_str = '2023-06-05'
new_date_str = convert_date_format(date_str)

print(f"New date: {new_date_str}")


# In[76]:


def find_decimal_numbers(text): 
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    matches = pattern.findall(text)
    
    return matches

text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
result = find_decimal_numbers(text)

print(result)


# In[78]:


def find_numbers_with_positions(text):
    pattern = re.compile(r'\d+')
    matches = pattern.finditer(text)
    
    for match in matches:
        number = match.group()
        position = match.start()
        print(f"Number: {number}, Position: {position}")

text = "The quick brown fox jumps over 15 lazy dogs and 3 cats."
find_numbers_with_positions(text)


# In[79]:


text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
numeric_values = re.findall(r'\b\d+\b', sample_text)

if numeric_values:
    max_value = max(map(int, numeric_values))
    print("Lagest number:", max_value)
else:
    print("No numeric values found.")


# In[81]:


def insert_spaces(text):
    spaced_text = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
    return spaced_text.capitalize()

sample_text = "RegularExpressionIsAnImportantTopicInPython"

result = insert_spaces(sample_text)
print(result)


# In[84]:


text = "Find Sequences Of One Uppercase Letter Followed By Lowercase Letters like This One."

pattern = r'[A-Z][a-z]+'
matches = re.findall(pattern, text)
print(matches)


# In[85]:


def remove_continuous_duplicates(sentence):
    cleaned_sentence = re.sub(r'\b(\w+)( \1\b)+', r'\1', sentence)
    return cleaned_sentence.strip()

sample_text = "Hello hello world world"

result = remove_continuous_duplicates(sample_text)
print(result)


# In[86]:


def is_alphanumeric_ending(string):
    pattern = r'.*[a-zA-Z0-9]$'
    
    if re.match(pattern, string):
        return True
    else:
        return False

test_strings = [
    "Laptop456",
    "Laptop125!",
    "Laptop!",
    "123Laptop",
    "123Laptop ",
    "Laptop1234"
]

for s in test_strings:
    result = is_alphanumeric_ending(s)
    print(f"'{s}': {result}")


# In[88]:


def extract_hashtags(text):
    pattern = r'#\w+'
    hashtags = re.findall(pattern, text)
    
    return hashtags

text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
result = extract_hashtags(text)
print(result)


# In[97]:


def remove_unicode_symbols(text):
    pattern = r'<U\+[A-F0-9]{4}>'
    cleaned_text = re.sub(pattern, '', text)
    
    return cleaned_text

text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
result = remove_unicode_symbols(text)
print( result)


# In[102]:


sample_text = "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."
file_name = 'sample_text.txt'

with open(sample_text.txt, 'w') as file:
    file.write(sample_text)

def extract_dates_from_file(text):
    with open(sample_text.txt, 'r') as file:
        content = file.read()
    
    date_pattern = re.compile(r'\b\d{2}-\d{2}-\d{4}\b')
    dates = date_pattern.findall(content)
    
    return dates
extracted_dates = extract_dates_from_file(sample_text.txt)
print("Extracted Dates:", extracted_dates)



# In[93]:


def remove_words_of_length_2_to_4(text):
    pattern = re.compile(r'\b\w{2,4}\b')

    cleaned_text = pattern.sub('', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text
text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
result = remove_words_of_length_2_to_4(text)
print( result)


# In[ ]:




