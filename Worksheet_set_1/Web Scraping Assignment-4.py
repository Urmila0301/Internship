#!/usr/bin/env python
# coding: utf-8

# In[130]:


get_ipython().system('pip install selenium')


# In[131]:


# Importing Libraries
import selenium
import pandas as pd
import time
from bs4 import BeautifulSoup

# Importing selenium webdriver 
from selenium import webdriver

# Importing required Exceptions which needs to handled
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

#Importing requests
import requests

# importing regex
import re


# 1. Scrape the details of most viewed videos on YouTube from Wikipedia. Url
# = https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos You need to find following details: A)
# Rank
# B) Name
# C) Artist
# D) Upload date
# E) Views 

# In[24]:


driver = webdriver.Chrome()


# In[25]:


driver.get("https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos ")


# In[26]:


Rank=[]
Name=[]
Artist=[]
Upload_Date=[]
Views=[]


# In[30]:


#scraping the Rank 
rk=driver.find_elements(By.XPATH,"//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr/td[1]")
for i in rk:
    if i.text is None :
        Rank.append("--") 
    else:
        Rank.append(i.text)
print(len(Rank),Rank)


# In[31]:


nm=driver.find_elements(By.XPATH,"//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr/td[2]")
for i in nm:
    if i.text is None :
        Name.append("--") 
    else:
        Name.append(i.text)
print(len(Name),Name)


# In[32]:


#scraping the Artist 
Ar=driver.find_elements(By.XPATH,"//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr/td[3]")
for i in Ar:
    if i.text is None :
        Artist.append("--") 
    else:
        Artist.append(i.text)
print(len(Artist),Artist)


# In[33]:


#scraping the Upload_Date 
date=driver.find_elements(By.XPATH,"//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr/td[5]")
for i in date:
    if i.text is None :
        Upload_Date.append("--") 
    else:
        Upload_Date.append(i.text)
print(len(Upload_Date),Upload_Date)


# In[34]:


#scraping the Views 
v=driver.find_elements(By.XPATH,"//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr/td[4]")
for i in v:
    if i.text is None :
        Views.append("--") 
    else:
        Views.append(i.text)
print(len(Views),Views)


# In[35]:


Youtube_Video=pd.DataFrame([])
Youtube_Video['Rank']=Rank
Youtube_Video['Video Title']=Name
Youtube_Video['Artist']=Artist
Youtube_Video['Upload_Date']=Upload_Date
Youtube_Video['Views In Bllion']=Views
Youtube_Video


# 2. Scrape the details team India’s international fixtures from bcci.tv.
# Url = https://www.bcci.tv/.
# You need to find following details:
# A) Series
# B) Place
# C) Date
# D) Time
# Note: - From bcci.tv home page you have reach to the international fixture page through code. 

# In[73]:


driver = webdriver.Chrome()


# In[74]:


driver.get("https://www.bcci.tv/")


# In[75]:


search=driver.find_element(By.XPATH,"/html/body/header/div[3]/div[2]/ul/div[1]/a[2]")
search.click()


# In[49]:


Series=[]
Place =[]
Date=[]
Time=[]


# In[67]:


#scraping the Series
sr=driver.find_elements(By.XPATH,"/html/body/section/div/div/div/div/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div/div[2]/h5")
for i in sr:
    if i.text is None :
        Series.append("--") 
    else:
        Series.append(i.text)
print(len(Series),Series)


# In[68]:


#scraping the place
pl=driver.find_elements(By.XPATH,"/html/body/section/div/div/div/div/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[3]/span[2]")
for i in pl:
    if i.text is None :
        Place.append("--") 
    else:
        Place.append(i.text)
print(len(Place),Place)


# In[70]:


#scraping the Date 
DT=driver.find_elements(By.XPATH,"/html/body/section/div/div/div/div/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[1]")
for i in DT:
    if i.text is None :
        Date.append("--") 
    else:
        Date.append(i.text)
print(len(Date),Date)


# In[71]:


#scraping the Time 
TM=driver.find_elements(By.XPATH,"/html/body/section/div/div/div/div/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[2]")
for i in TM:
    if i.text is None :
        Time.append("--") 
    else:
        Time.append(i.text)
print(len(Time),Time)


# In[72]:


International_Fixtures=pd.DataFrame([])
International_Fixtures['Series']=Series
International_Fixtures['Place']=Place
International_Fixtures['Date']=Date
International_Fixtures['Time']=Time
International_Fixtures


# 3. Scrape the details of State-wise GDP of India from statisticstime.com.
# Url = http://statisticstimes.com/
# You have to find following details: A) Rank
# B) State
# C) GSDP(18-19)- at current prices
# D) GSDP(19-20)- at current prices
# E) Share(18-19)
# F) GDP($ billion)
# Note: - From statisticstimes home page you have to reach to economy page through code.

# In[77]:


driver = webdriver.Chrome()


# In[78]:


driver.get("http://statisticstimes.com/")


# In[80]:


economy = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/button')
economy.click()


# In[ ]:


ind = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/div')
ind.click()


# In[84]:


gdp = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/ul/li[1]/a')
gdp.click()


# In[88]:


Rank=[]
State =[]
GDP=[]
GSDP_Current=[]
GSDP_Previous=[]
Share=[]
GDP_billion=[]


# In[89]:


#scraping the Rank 
r=driver.find_elements(By.XPATH,"//td[@class='data1']")
for i in r:
    if i.text is None :
        Rank.append("--") 
    else:
        Rank.append(i.text)
print(len(Rank),Rank)


# In[90]:


#scraping the State 
St=driver.find_elements(By.XPATH,"//td[@class='name']")
for i in St:
    if i.text is None :
        State.append("--") 
    else:
        State.append(i.text)
print(len(State),State)


# In[91]:


#scraping the GDP 
gdp=driver.find_elements(By.XPATH,"//*[@id='table_id']/tbody/tr/td[6]")
for i in gdp:
    if i.text is None :
        GDP.append("--") 
    else:
        GDP.append(i.text)
print(len(GDP),GDP)


# In[92]:


#scraping the Share 
shr=driver.find_elements(By.XPATH,"//*[@id='table_id']/tbody/tr/td[5]")
for i in shr:
    if i.text is None :
        Share.append("--") 
    else:
        Share.append(i.text)
print(len(Share),Share)


# In[93]:


#scraping the GSDP_Current 
shr=driver.find_elements(By.XPATH,"//*[@id='table_id']/tbody/tr/td[4]")
for i in shr:
    if i.text is None :
        GSDP_Current.append("--") 
    else:
        GSDP_Current.append(i.text)
print(len(GSDP_Current),GSDP_Current)


# In[94]:


#scraping the GSDP_Previous 
shr=driver.find_elements(By.XPATH,"//*[@id='table_id']/tbody/tr/td[8]")
for i in shr:
    if i.text is None :
        GSDP_Previous.append("--") 
    else:
        GSDP_Previous.append(i.text)
print(len(GSDP_Previous),GSDP_Previous)


# In[95]:


State_GDP=pd.DataFrame([])
State_GDP['Rank']=Rank[:33]
State_GDP['State']=State[:33]
State_GDP['Share In GDP']=Share[:33]
State_GDP['GDP of State']=GDP[:33]
State_GDP['GSDP_Current']=GSDP_Current[:33]
State_GDP['GSDP_Previous']=GSDP_Previous[:33]
State_GDP


# 4. Scrape the details of trending repositories on Github.com.
# Url = https://github.com/
# You have to find the following details:
# A) Repository title
# B) Repository description
# C) Contributors count
# D) Language used
# Note: - From the home page you have to click on the trending option from Explore menu through code.

# In[96]:


driver = webdriver.Chrome()


# In[97]:


driver.get("https://github.com/")


# In[99]:


explore = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/div/qbsearch-input/div[1]/div/modal-dialog/div/div/div/form/query-builder/div[1]/div[1]/div/div[2]')
explore.click()


# In[ ]:


trending = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[2]/nav/ul/li[4]/details/div/ul[2]/li[3]')
trending.click()


# In[102]:


Repository_title=[]
Repository_description=[]
Contributors_count=[]
Language_used=[]


# In[108]:


#scraping the Repository_title 
RT=driver.find_elements(By.XPATH,"/html/body/div[1]/div[4]/main/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[4]/div/div/div[1]/div/div[1]/h3/div/div[2]")
for i in RT:
    if i.text is None :
        Repository_title.append("--") 
    else:
        Repository_title.append(i.text)
print(len(Repository_title),Repository_title)


# In[112]:


#scraping the Description 
des=driver.find_elements(By.XPATH,"/html/body/div[1]/div[4]/main/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[4]/div/div/div[2]/div/div[1]/div[1]")
for i in des:
    if i.text is None :
        Repository_description.append("--") 
    else:
        Repository_description.append(i.text)
print(len(Repository_description),Repository_description)


# In[116]:


CC=driver.find_elements(By.XPATH,"/html/body/div[1]/div[4]/main/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[4]/div/div/div[1]/div/div[1]/ul/span[2]")
for i in CC:
    if i.text is None :
        Contributors_count.append("NAN") 
    else:
        Contributors_count.append(i.text)
print(len(Contributors_count),Contributors_count)


# In[120]:


#scraping the Language 
L=driver.find_elements(By.XPATH,"/html/body/div[1]/div[4]/div/main/turbo-frame/div/div/div/div[2]/div[2]/div/div[5]")
for i in L:
    if i.text is None :
        Language_used.append("NAN") 
    else:
        Language_used.append(i.text)
print(len(Language_used),Language_used)


# In[126]:


Trending_Repository=pd.DataFrame([])
Trending_Repository['Repository title']=Repository_title
Trending_Repository['Repository description']=Repository_description
Trending_Repository['Contributors count']=Contributors_count
Trending_Repository['Language used']=Language_used


# In[127]:


Trending_Repository


# 5. Scrape the details of top 100 songs on billiboard.com. Url = https:/www.billboard.com/ You have to find the following details:
# A) Song name
# B) Artist name
# C) Last week rank
# D) Peak rank
# E) Weeks on board
# Note: - From the home page you have to click on the charts option then hot 100-page link through code.

# In[153]:


driver = webdriver.Chrome()


# In[154]:


driver.get("https:/www.billboard.com/")


# In[ ]:


top100 = driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div/div/div/ul/li[1]/h3/a')
top100.click()


# In[ ]:


Song_Name =[]
Artist_name=[]
rank=[]
Last_Week=[]
Weeks_on_board=[]


# In[158]:


#scraping the Song_Name 
son=driver.find_elements(By.XPATH,"/html/body/div[3]/main/div[2]/div[3]/div/div/div/div[2]/div[4]/ul/li[4]/ul/li[1]/h3")
for i in son:
    if i.text is None :
        Song_Name.append("--") 
    else:
        Song_Name.append(i.text)
print(len(Song_Name),Song_Name)


# In[161]:


#scraping the Singer 
sin=driver.find_elements(By.XPATH,"/html/body/div[3]/main/div[2]/div[3]/div/div/div/div[2]/div[4]/ul/li[4]/ul/li[1]/span")
for i in sin:
    if i.text is None :
        Artist_name.append("--") 
    else:
        Artist_name.append(i.text)
print(len(Artist_name),Artist_name)


# In[162]:


#scraping the Rank 
rb=driver.find_elements(By.XPATH,"/html/body/div[3]/main/div[2]/div[3]/div/div/div/div[2]/div[4]/ul/li[4]/ul/li[5]/span")
for i in rb:
    if i.text is None :
        rank.append("--") 
    else:
        rank.append(i.text)
print(len(rank),rank)


# In[163]:


#scraping the Last_Week Rank 
lwr=driver.find_elements(By.XPATH,"/html/body/div[3]/main/div[2]/div[3]/div/div/div/div[2]/div[3]/ul/li[4]/ul/li[4]/span")
for i in lwr:
    if i.text is None :
        Last_Week.append("--") 
    else:
        Last_Week.append(i.text)
print(len(Last_Week),Last_Week)


# In[164]:


#scraping the Weeks_on_board 
wob=driver.find_elements(By.XPATH,"/html/body/div[3]/main/div[2]/div[3]/div/div/div/div[2]/div[4]/ul/li[4]/ul/li[6]/span")
for i in wob:
    if i.text is None :
        Weeks_on_board.append("--") 
    else:
        Weeks_on_board.append(i.text)
print(len(Weeks_on_board),Weeks_on_board)


# In[165]:


Top_Song=pd.DataFrame([])
Top_Song['Peak_rank']=rank
Top_Song['Song_Name']=Song_Name
Top_Song['Singer / Crew']=Artist_name
Top_Song['Last_Week_Rank']=Last_Week
Top_Song['Weeks_on_board']=Weeks_on_board
Top_Song


# 6. Scrape the details of Highest selling novels.
# A) Book name
# B) Author name
# C) Volumes sold
# D) Publisher
# E) Genre
# Url - https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare

# In[166]:


driver = webdriver.Chrome()


# In[167]:


driver.get("https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare")


# In[168]:


Book_name=[]
Author_name=[]
Volumes_sold=[]
Publisher=[]
Genre=[]


# In[169]:


#scraping the Book_name 
bname=driver.find_elements(By.XPATH,"/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[2]")
for i in bname:
    if i.text is None :
        Book_name.append("--") 
    else:
        Book_name.append(i.text)
print(len(Book_name),Book_name)


# In[170]:


#scraping the Author_name 
Auth=driver.find_elements(By.XPATH,"/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[3]")
for i in Auth:
    if i.text is None :
        Author_name.append("--") 
    else:
        Author_name.append(i.text)
print(len(Author_name),Author_name)


# In[172]:


#scraping the Genre 
gen=driver.find_elements(By.XPATH,"/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[6]")
for i in gen:
    if i.text is None :
        Genre.append("--") 
    else:
        Genre.append(i.text)
print(len(Genre),Genre)


# In[173]:


#scraping the Publisher 
pub=driver.find_elements(By.XPATH,"/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[5]")
for i in pub:
    if i.text is None :
        Publisher.append("--") 
    else:
        Publisher.append(i.text)
print(len(Publisher),Publisher)


# In[174]:


#scraping the Volumes_sold 
vs=driver.find_elements(By.XPATH,"/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[4]")
for i in vs:
    if i.text is None :
        Volumes_sold.append("--") 
    else:
        Volumes_sold.append(i.text)
print(len(Volumes_sold),Volumes_sold)


# In[175]:


Book=pd.DataFrame([])
Book['Book_name']=Book_name
Book['Author_name']=Author_name
Book['Genre']=Genre
Book['Publisher']=Publisher
Book['Volumes_sold']=Volumes_sold
Book


# 7. Scrape the details most watched tv series of all time from imdb.com.
# Url = https://www.imdb.com/list/ls095964455/ You have to find the following details:
# A) Name
# B) Year span
# C) Genre
# D) Run time
# E) Ratings
# F) Votes

# In[180]:


driver = webdriver.Chrome()


# In[181]:


driver.get("https://www.imdb.com/list/ls095964455/")


# In[178]:


Name=[]
Year_span=[]
Genres=[]
Run_time=[]
Ratings=[]
Votes=[]


# In[192]:


#scraping the Name 
mname=driver.find_elements(By.XPATH,"/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1/span")
for i in mname:
    if i.text is None :
        Name.append("--") 
    else:
        Name.append(i.text)
print(len(Name),Name)


# In[185]:


#scraping the Year_span 
ys=driver.find_elements(By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/div/div[1]/div[2]/ul[1]/li[1]")
for i in ys:
    if i.text is None :
        Year_span.append("--") 
    else:
        Year_span.append(i.text)
print(len(Year_span),Year_span)


# In[186]:


#scraping the Genres 
gnr=driver.find_elements(By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/div/div[1]/div[2]/ul[2]/li[3]")
for i in gnr:
    if i.text is None :
        Genres.append("--") 
    else:
        Genres.append(i.text)
print(len(Genres),Genres)


# In[188]:


#scraping the Run_time 
rt=driver.find_elements(By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/div/div[1]/div[2]/ul[1]/li[2]")
for i in rt:
    if i.text is None :
        Run_time.append("--") 
    else:
        Run_time.append(i.text)
print(len(Run_time),Run_time)


# In[189]:


#scraping the Ratings 
rate=driver.find_elements(By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/span/span[1]")
for i in rate:
    if i.text is None :
        Ratings.append("--") 
    else:
        Ratings.append(i.text)
print(len(Ratings),Ratings)


# In[190]:


#scraping the Votes 
v=driver.find_elements(By.XPATH,"/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/ul/li[1]/a/span")
for i in v:
    if i.text is None :
        Votes.append("--") 
    else:
        Votes.append(i.text)
print(len(Votes),Votes)


# In[193]:


TV_Series=pd.DataFrame([])
TV_Series['Year_span']=Year_span
TV_Series['Run_time']=Run_time
TV_Series['Genres']=Genres
TV_Series['Ratings']=Ratings
TV_Series['Votes']=Votes
TV_Series


# 8. Details of Datasets from UCI machine learning repositories.
# Url = https://archive.ics.uci.edu/ You have to find the following details:
# A) Dataset name
# B) Data type
# C) Task
# D) Attribute type
# E) No of instances
# F) No of attribute G) Year
# Note: - from the home page you have to go to the Show All Dataset page through code.

# In[213]:


driver = webdriver.Chrome()


# In[214]:


driver.get("https://archive.ics.uci.edu/")


# In[ ]:


search_1 = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/ul/li[1]/a')
search_1.click()


# In[205]:


Dataset_Name=[]
Data_Type=[]
Task=[]
Attribute_Type=[]
No_of_Instances=[]
No_of_Attribute=[]
Year=[]


# In[206]:


#scraping the Dataset_Name 
dname=driver.find_elements(By.XPATH,"/html/body/div/div[1]/div[1]/main/div/div[2]/div[2]/div[1]/div[1]/div[2]/h2/a")
for i in dname:
    if i.text is None :
        Dataset_Name.append("--") 
    else:
        Dataset_Name.append(i.text)
print(len(Dataset_Name),Dataset_Name)


# In[208]:


#scraping the Data_Type 
dtype=driver.find_elements(By.XPATH,"/html/body/div/div[1]/div[1]/main/div/div[2]/div[2]/div[3]/div[1]/div[2]/div/div[2]/span")
for i in dtype:
    if i.text is None :
        Data_Type.append("--") 
    else:
        Data_Type.append(i.text)
print(len(Data_Type),Data_Type)


# In[209]:


#scraping the Task 
t=driver.find_elements(By.XPATH,"/html/body/div/div[1]/div[1]/main/div/div[2]/div[2]/div[3]/div[1]/div[2]/div/div[1]/span")
for i in t:
    if i.text is None :
        Task.append("--") 
    else:
        Task.append(i.text)
print(len(Task),Task)


# In[210]:


#scraping the Attribute_Type 
att=driver.find_elements(By.XPATH,"/html/body/div/div[1]/div[1]/main/div/div[2]/div[2]/div[3]/div[2]/div/table/tbody/tr/td[2]")
for i in att:
    if i.text is None :
        Attribute_Type.append("--") 
    else:
        Attribute_Type.append(i.text)
print(len(Attribute_Type),Attribute_Type)


# In[216]:


#scraping the No_of_Instances 
noi=driver.find_elements(By.XPATH,"/html/body/div/div[1]/div[1]/main/div/div[2]/section[1]/div[2]/div[1]/div/div[2]/div/div[2]/span")
for i in noi:
    if i.text is None :
        No_of_Instances.append("--") 
    else:
        No_of_Instances.append(i.text)
print(len(No_of_Instances),No_of_Instances)


# In[218]:


#scraping the No_of_Attribute 
noa=driver.find_elements(By.XPATH,"/html/body/div/div[1]/div[1]/main/div/div[1]/div[1]/div[2]/div[2]/div[6]/p")
for i in noa:
    if i.text is None :
        No_of_Attribute.append("--") 
    else:
        No_of_Attribute.append(i.text)
print(len(No_of_Attribute),No_of_Attribute)


# In[219]:


#scraping the Year 
y=driver.find_elements(By.XPATH,"/html/body/div/div[1]/div[1]/main/div/div[2]/div[2]/div[1]/div[2]/div/table/tbody/tr/td[3]")
for i in y:
    if i.text is None :
        Year.append("--") 
    else:
        Year.append(i.text)
print(len(Year),Year)


# In[220]:


UCI=pd.DataFrame([])
UCI['Dataset_Name']=Dataset_Name[:100]
UCI['Data_Type']=Data_Type[:100]
UCI['Task']=Task[:100]
UCI['Attribute_Type']=Attribute_Type[:100]
UCI['No_of_Instances']=No_of_Instances[:100]
UCI['No_of_Attribute']=No_of_Attribute[:100]
UCI['Year']=Year[:100]
UCI


# In[ ]:




