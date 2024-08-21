#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# Write a python program to display IMDB’s Top rated 100 Indian movies’ data
# https://www.imdb.com/list/ls056092300/ (i.e. name, rating, year ofrelease) and make data frame

# In[42]:


page = requests.get('https://www.imdb.com/list/ls056092300/')


# In[43]:


page


# In[44]:


soup = BeautifulSoup(page.content)
soup


# Name

# In[45]:


name = soup.find('div', class_="ipc-title__text")
name


# In[ ]:


name.text


# Rating

# In[46]:


rating = soup.find('span', class_="ipc-rating-star--rate")
rating


# In[ ]:


rating.text


# year of release

# In[49]:


yearof_release = soup.find('span', class_="sc-b189961a-8 hCbzGp dli-title-metadata-item")
yearof_release


# In[ ]:


yearof_release.text


# scraping Multiple title

# In[50]:


name = []

for i in soup.find_all('div',class_="ipc-title__text"):
        name.append(i.text)
        
name


# In[51]:


rating = []

for i in soup.find_all('div',class_="ipc-rating-star--rate"):
        rating.append(i.text)
        
rating


# In[52]:


yearof_release = []

for i in soup.find_all('div',class_="sc-b189961a-8 hCbzGp dli-title-metadata-item"):
        yearof_release.append(i.text)
        
yearof_release


# In[53]:


print(len(name),len(rating),len(yearof_release))


# In[54]:


import pandas as pd
df = pd.DataFrame({'Name':name, 'Rating':rating, 'Yearof_release':yearof_release,'Images_url':images})
df


# 2) Write a python program to scrape details of all the posts from https://www.patreon.com/coreyms .Scrape the
# heading, date, content and the likes for the video from the link for the youtube video from the post.

# In[55]:


page = requests.get('https://www.patreon.com/coreyms')


# In[56]:


page


# In[57]:


soup = BeautifulSoup(page.content)
soup


# heading

# In[59]:


heading = soup.find('div', class_="sc-bBHxTw jIEOUn")
heading


# In[ ]:


heading.text


# Date

# In[60]:


date = soup.find('span', id_="track-click")
date


# In[ ]:


date.text


# content

# In[63]:


content = soup.find('div', class_="sc-1cq1psq-0 kWkNqn sc-pn81yk-0 dBfLIG")
content


# In[ ]:


content.text


# Likes

# In[64]:


like = soup.find('span', class_="sc-dkPtRN eEJGed")
like


# In[ ]:


like.text


# In[65]:


heading = []

for i in soup.find_all('div', class_="sc-bBHxTw jIEOUn"):
        heading.append(i.text)
        
heading


# In[66]:


date = []

for i in soup.find_all('span', id_="track-click"):
        date.append(i.text)
        
date


# In[67]:


content = []

for i in soup.find_all('div', class_="sc-1cq1psq-0 kWkNqn sc-pn81yk-0 dBfLIG"):
        content.append(i.text)
        
content


# In[68]:


like = []

for i in soup.find_all('span', class_="sc-dkPtRN eEJGed"):
        like.append(i.text)
        
like


# 3) Write a python program to scrape house details from mentioned URL. It should include house title, location,
# area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar,
# Rajaji Nagar

# In[69]:


page = requests.get('https://www.nobroker.in/')


# In[70]:


page


# In[71]:


soup = BeautifulSoup(page.content)
soup


# In[74]:


house_title = soup.find('h2', class_="heading-6 flex items-center font-semi-bold m-0")
house_title


# In[ ]:


house_title.text


# In[76]:


location = soup.find('div', class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95")
location


# In[ ]:


location.text


# In[78]:


area = soup.find('div', class_="text-default-color align-bottom underline hover:text-primary-color")
area


# In[ ]:


area.text


# In[79]:


EMI_price = soup.find('div', class_="font-semi-bold heading-6")
EMI_price


# In[ ]:


EMI_price.text


# In[81]:


house_title = []

for i in soup.find_all('h2', class_="heading-6 flex items-center font-semi-bold m-0"):
        house_title.append(i.text)
        
house_title


# In[82]:


location = []

for i in soup.find_all('div', class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95"):
        location.append(i.text)

location


# In[83]:


area = []

for i in soup.find_all('div', class_="text-default-color align-bottom underline hover:text-primary-color"):
        area.append(i.text)
        
area 


# In[84]:


EMI_price = []

for i in soup.find_all('div', class_="font-semi-bold heading-6"):
        EMI_price.append(i.text)
        
EMI_price 


# 4) Write a python program to scrape first 10 product details which include product name , price , Image URL from
# https://www.bewakoof.com/bestseller?sort=popular .

# In[85]:


page = requests.get('https://www.bewakoof.com/bestseller?sort=popular')


# In[86]:


page


# In[87]:


soup = BeautifulSoup(page.content)
soup


# In[89]:


product_name = soup.find('div', class_="productNaming bkf-ellipsis")
product_name


# In[90]:


product_name.text


# In[105]:


price = soup.find('div', class_="productPriceBox d-flex align-items-end  false")
price


# In[ ]:


price.text


# In[111]:


images = []

for i in soup.find_all("img", class_="https://images.bewakoof.com/t640/women-s-red-inner-peace-graphic-printed-boyfriend-t-shirt-295706-1720009662-1.jpg"):
    images.append(i['data-src'])
    
images


# In[108]:


product_name = []

for i in soup.find_all('div', class_="productNaming bkf-ellipsis"):
        product_name.append(i.text)
        
product_name


# In[109]:


price = []

for i in soup.find_all('div', class_="productPriceBox d-flex align-items-end  false"):
        price.append(i.text)
        
price


# 5) Please visit https://www.cnbc.com/world/?region=world and scrap-
#  a) headings
# b) date
# c) News link

# In[112]:


page = requests.get('https://www.cnbc.com/world/?region=world')


# In[113]:


page


# In[115]:


soup = BeautifulSoup(page.content)
soup


# In[116]:


headings = soup.find('div', class_="LatestNews-headlineWrapper")
headings


# In[118]:


headings.text


# In[121]:


date = soup.find('span', class_="RiverByline-datePublished")
date


# In[122]:


date.text


# In[125]:


news_link = soup.find('div', class_="Card-titleContainer")
news_link


# In[126]:


news_link.text


# In[127]:


headings = []

for i in soup.find_all('div', class_="LatestNews-headlineWrapper"):
        headings.append(i.text)
        
headings


# In[128]:


date = []

for i in soup.find_all('div', class_="Card-titleContainer"):
        date.append(i.text)
        
date


# In[129]:


news_link = []

for i in soup.find_all('div', class_="Card-titleContainer"):
        news_link.append(i.text)
        
news_link


# (6) Please visit https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloadedarticles/ and scrapa) Paper title
#  b) date
# c) Author

# In[130]:


page = requests.get('https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloadedarticles/')


# In[131]:


page


# In[132]:


soup = BeautifulSoup(page.content)
soup


# In[135]:


Paper_title  = soup.find('div', class_="h5 article-title")
Paper_title


# In[136]:


date  = soup.find('div', class_="h5 article-title")
date


# In[137]:


author  = soup.find('div', class_="article-authors")
author


# In[ ]:




