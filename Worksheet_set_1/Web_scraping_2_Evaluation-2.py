#!/usr/bin/env python
# coding: utf-8

# In[60]:


get_ipython().system('pip install selenium')


# In[62]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# Q1: In this question you have to scrape data using the filters available on the webpage You have to use the location and
# salary filter. 

# In[73]:


driver = webdriver.Chrome()


# In[74]:


driver.get("https://www.naukri.com/")


# In[75]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Scientist')


# In[76]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[43]:


try:
    location_filter = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//label[text()="Delhi / NCR"]'))
    )
    location_filter.click()
except Exception as e:
    print("Location filter not found:", e)
    driver.quit()


# In[44]:


try:
    salary_filter = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//label[text()="3-6 Lakhs"]'))
    )
    salary_filter.click()
except Exception as e:
    print("Salary filter not found:", e)
    driver.quit()


# In[77]:


Job_title=[]
job_location=[]
company_name=[]
exp_required=[]


# In[80]:


title_tags=driver.find_elements(By.XPATH,'//div[@class="srp-jobtuple-wrapper"]')
for i in title_tags:
    title=i.text
    Job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//span[@class="locWdth"]')
for i in location_tags:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//div [@class=" row2"]/span/a[1]')
for i in company_tags:
    company=i.text
    company_name.append(company)
    
 
exp_tags=driver.find_elements(By.XPATH,'//span[@class="expwdth"]')
for i in exp_tags:
    exp=i.text
    exp_required.append(exp)


# In[81]:


print(len(Job_title),len(job_location),len(company_name),len(exp_required))


# In[82]:


import pandas as pd
df=pd.DataFrame({'Title':Job_title,'location':job_location,'company_name':company_name,'experince':exp_required})
df


# Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the
# job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data.
# 

# In[104]:


driver = webdriver.Chrome()


# In[105]:


driver.get("https://www.shine.com/")


# In[107]:


designation=driver.find_element(By.CLASS_NAME, 'form-control')
designation.send_keys('Data Analyst')


# In[108]:


location=driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Bangalore')


# In[109]:


search=driver.find_element(By.CLASS_NAME,"searchForm_btnWrap__Cb75F")
search.click()


# In[110]:


Job_title=[]
job_location=[]
company_name=[]
exp_required=[]


# In[111]:


title_tags=driver.find_elements(By.XPATH,'//strong[@class="jobCard_pReplaceH2__xWmHg"]')
for i in title_tags:
    title=i.text
    Job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags:
    company=i.text
    company_name.append(company)
    
 
exp_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in exp_tags:
    exp=i.text
    exp_required.append(exp)


# In[112]:


print(len(Job_title),len(job_location),len(company_name),len(exp_required))


# In[113]:


import pandas as pd
df=pd.DataFrame({'Title':Job_title,'location':job_location,'company_name':company_name,'experince':exp_required})
df


# Q3: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:
# https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=F
# LIPKART

# In[125]:


driver = webdriver.Chrome()


# In[126]:


driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART")


# In[128]:


#Rating
url=driver.find_elements(By.XPATH, '//div[@class="col-12-12 ggs1+C"]')
url[0:100]


# In[130]:


#Review summary
url=driver.find_elements(By.XPATH, '//p[@class="z9E0IG"]')
url[0:10]


# In[131]:


#Full review
url=driver.find_elements(By.XPATH, '//div[@class=""]')
url[0:10]


# Q4: Scrape data forfirst 100 sneakers you find whenyouvisitflipkart.com and search for “sneakers” inthe search
# field.

# In[134]:


driver = webdriver.Chrome()


# In[135]:


driver.get("https://www.flipkart.com/")


# In[137]:


search=driver.find_element(By.CLASS_NAME,"Pke_EE")
search.send_keys('sneakers')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[141]:


url=driver.find_elements(By.XPATH, '//div[@class="syl9yP"]')
url[0:100]


# In[147]:


Brand_title=[]


# In[149]:


start=0
end=3
for page in range(start,end):
    Brand=driver.find_elements(By.XPATH,'//div[@class="syl9yP"]')
    for i in Brand:
        Brand_title.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[12]')
    next_button.click()
    time.sleep(3)


# In[150]:


Brand_title


# In[151]:


url=driver.find_elements(By.XPATH, '//a[@class="WKTcLC"]')
url[0:100]


# In[152]:


ProductDescription_title=[]


# In[155]:


start=0
end=4
for page in range(start,end):
    ProductDescription=driver.find_elements(By.XPATH,'//a[@class="WKTcLC"]')
    for i in ProductDescription:
        ProductDescription_title.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[12]')
    next_button.click()
    time.sleep(4)


# In[157]:


len(ProductDescription_title)


# In[158]:


ProductDescription_title


# In[159]:


url=driver.find_elements(By.XPATH, '//div[@class="hl05eU"]')
url[0:100]


# In[160]:


Price_title=[]


# In[166]:


start=0
end=5
for page in range(start,end):
    ProductDescription=driver.find_elements(By.XPATH,'//div[@class="Nx9bqj"]')
    for i in ProductDescription:
        ProductDescription_title.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[12]')
    next_button.click()
    time.sleep(5)


# In[167]:


len(Price_title)


# In[168]:


Price_title


# Q5: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then set CPU
# Type filter to “Intel Core i7” as shown in the below image:

# In[169]:


driver = webdriver.Chrome()


# In[170]:


driver.get("https://www.amazon.in")


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"twotabsearchtextbox")
designation.send_keys('Laptop')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[202]:


url=driver.find_elements(By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]')
url[0:10]


# In[203]:


Title_tag=[]


# In[205]:


start=0
end=3
for page in range(start,end):
    titles=driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
    for i in titles:
        Title_tag.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[29]/div/div/span/a[3]')
    next_button.click()
    time.sleep(3)


# In[206]:


len(Title_tag)


# In[207]:


Title_tag


# In[208]:


url=driver.find_elements(By.XPATH, '//i[@class="a-icon a-icon-star-small a-star-small-4 aok-align-bottom"]')
url[0:10]


# In[209]:


Rating_title=[]


# In[210]:


start=0
end=2
for page in range(start,end):
    Rating=driver.find_elements(By.XPATH,'//i[@class="a-icon a-icon-star-small a-star-small-4 aok-align-bottom"]')
    for i in Rating:
        Rating_title.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[29]/div/div/span/a[3]')
    next_button.click()
    time.sleep(2)


# In[211]:


len(Rating_title)


# In[212]:


Rating_title


# In[213]:


url=driver.find_elements(By.XPATH, '//span[@class="a-price-whole"]')
url[0:10]


# In[214]:


price_tag=[]


# In[215]:


start=0
end=2
for page in range(start,end):
    price=driver.find_elements(By.XPATH,'//i[@class="a-icon a-icon-star-small a-star-small-4 aok-align-bottom"]')
    for i in price:
        price_tag.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[29]/div/div/span/a[3]')
    next_button.click()
    time.sleep(2)


# In[216]:


len(price_tag)


# In[217]:


price_tag


# Q6: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps

# In[218]:


driver = webdriver.Chrome()


# In[219]:


driver.get("https://www.azquotes.com/")


# In[221]:


quote=driver.find_element(By.CLASS_NAME,"ui-autocomplete-input")
quote.send_keys('Top 1000 Quotes of All Time')


# In[223]:


url=driver.find_elements(By.XPATH, '//a[@class="gs-title"]')
url[0:100]


# In[224]:


for i in url[0:4]:
    print(i.get_attribute('href'))


# In[ ]:


quote_tag=[]


# In[ ]:


start=0
end=5
for page in range(start,end):
    quote=driver.find_elements(By.XPATH,'//a[@class="gs-title"]')
    for i in quote:
        quote_tag.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[5]/div[2]/div[1]/div/div[2]/div/div[10]')
    next_button.click()
    time.sleep(5)


# In[ ]:


len(quote_tag)


# In[ ]:


quote_tag


# Q7: Write a python program to display list of respected former Prime Ministers of India (i.e. Name,
# Born-Dead, Term of office, Remarks) from https://www.jagranjosh.com/general-knowledge/list-ofall-prime-ministers-of-india-1473165149-1

# In[13]:


driver = webdriver.Chrome()


# In[14]:


driver.get("https://www.jagranjosh.com/general-knowledge/list-ofall-prime-ministers-of-india-1473165149-1")


# In[15]:


Name_tag=[]
Age_tag=[]
Termofoffice_tag=[]
duration_tag=[]


# In[19]:


name_title=driver.find_elements(By.XPATH,'/html/body/div[1]/div[6]/div/div[1]/div')
for i in name_title:
    name=i.text
    Name_tag.append(name)
    
age_title=driver.find_elements(By.XPATH,'/html/body/div[1]/main/div[1]/div[1]/article/div[4]/div[9]/div[1]/table/tbody/tr[1]/td[3]')
for i in age_title:
    age=i.text
    Age_tag.append(age)
    
termofoffice_title=driver.find_elements(By.XPATH,'/html/body/div[1]/main/div[1]/div[1]/article/div[4]/div[9]/div[1]/table/tbody/tr[1]/td[4]')
for i in termofoffice_title:
    termofoffice=i.text
    Termofoffice_tag.append(termofoffice)
    
 
duration_title=driver.find_elements(By.XPATH,'/html/body/div[1]/main/div[1]/div[1]/article/div[4]/div[9]/div[1]/table/tbody/tr[1]/td[5]')
for i in duration_title:
    duration=i.text
    duration_tag.append(duration)


# In[20]:


print(len(Name_tag),len(Age_tag),len(Termofoffice_tag),len(duration_tag))


# In[21]:


import pandas as pd
df=pd.DataFrame({'Name':Name_tag,'Age':Age_tag,'Termofoffice':Termofoffice_tag,'Duration':duration_tag})
df


# Q8: Write a python program to display list of 50 Most expensive cars in the world
# (i.e. Car name and Price) from https://www.motor1.com/

# In[22]:


driver = webdriver.Chrome()


# In[23]:


driver.get("https://www.motor1.com/")


# In[40]:


search=driver.find_element(By.XPATH,"/html/body/div[9]/div[2]/div/div/div[3]/div/div/div/form/input")
search.send_keys('50 most expensive cars')


# In[43]:


search=driver.find_element(By.XPATH,"/html/body/div[9]/div[9]/div/div[1]/div/div/div[1]/div/div[1]/h3/a")
search.click()


# In[56]:


car_name=[]


# In[57]:


car_tags=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in car_tags:
    car=i.text
    car_name.append(car)


# In[58]:


print(len(car_name))


# In[59]:


import pandas as pd
df=pd.DataFrame({'Name':car_name})
df


# In[ ]:




