#!/usr/bin/env python
# coding: utf-8

# 1. Write a python program which searches all the product under a particular product from www.amazon.in. The
# product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for
# guitars.
# 2. In the above question, now scrape the following details of each product listed in first 3 pages of your search
# results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then
# scrape all the products available under that product name. Details to be scraped are: "Brand
# Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and
# “Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_amazon_search_url(query):
    return f"https://www.amazon.in/s?k={query}"

def get_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        return None

def parse_product_details(product):
    try:
        brand_name = product.find('span', class_='a-size-base-plus').text.strip()
    except:
        brand_name = '-'
    try:
        product_name = product.h2.text.strip()
    except:
        product_name = '-'
    try:
        price = product.find('span', class_='a-price-whole').text.strip() + product.find('span', class_='a-price-fraction').text.strip()
    except:
        price = '-'
    try:
        product_url = "https://www.amazon.in" + product.h2.a['href']
    except:
        product_url = '-'
    
    # For return/exchange, expected delivery, and availability, we need to visit the product page
    return_details, expected_delivery, availability = '-', '-', '-'
    if product_url != '-':
        soup = get_soup(product_url)
        if soup:
            try:
                return_details = soup.find('div', id='return-policy').text.strip()
            except:
                return_details = '-'
            try:
                expected_delivery = soup.find('div', id='ddmDeliveryMessage').text.strip()
            except:
                expected_delivery = '-'
            try:
                availability = soup.find('div', id='availability').span.text.strip()
            except:
                availability = '-'
    
    return {
        'Brand Name': brand_name,
        'Name of the Product': product_name,
        'Price': price,
        'Return/Exchange': return_details,
        'Expected Delivery': expected_delivery,
        'Availability': availability,
        'Product URL': product_url
    }

def scrape_amazon_products(query, pages=3):
    products_list = []
    for page in range(1, pages+1):
        url = get_amazon_search_url(query) + f"&page={page}"
        soup = get_soup(url)
        if not soup:
            break
        products = soup.find_all('div', {'data-component-type': 's-search-result'})
        for product in products:
            product_details = parse_product_details(product)
            products_list.append(product_details)
        time.sleep(2)  # Be polite and don't hammer the server
    
    return products_list

def main():
    query = input("Enter the product to search: ")
    products = scrape_amazon_products(query)
    df = pd.DataFrame(products)
    df.to_csv(f"{query}_products.csv", index=False)
    print(f"Scraped data saved to {query}_products.csv")

if __name__ == "__main__":
    main()


# 3. Write a python program to access the search bar and search button on images.google.com and scrape 10
# images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’. 

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import os

def download_image(url, folder_path, file_name):
    try:
        image_content = requests.get(url).content
        with open(os.path.join(folder_path, file_name), 'wb') as image_file:
            image_file.write(image_content)
        print(f'Successfully downloaded {file_name}')
    except Exception as e:
        print(f'Failed to download {file_name}. Error: {e}')

def scrape_images(keyword, num_images=10):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://images.google.com')
    
    search_bar = driver.find_element(By.NAME, 'q')
    search_bar.send_keys(keyword)
    search_bar.send_keys(Keys.RETURN)
    
    time.sleep(2)
    
    # Scroll to load images
    for _ in range(2):
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(2)
    
    images = driver.find_elements(By.CSS_SELECTOR, 'img.rg_i.Q4LuWd')
    urls = []
    
    for img in images[:num_images]:
        try:
            img.click()
            time.sleep(1)
            actual_images = driver.find_elements(By.CSS_SELECTOR, 'img.n3VNCb')
            for actual_image in actual_images:
                src = actual_image.get_attribute('src')
                if 'http' in src:
                    urls.append(src)
                    if len(urls) >= num_images:
                        break
        except Exception as e:
            print(f'Error clicking image: {e}')
        if len(urls) >= num_images:
            break

    driver.quit()
    
    # Create a folder for the keyword if it doesn't exist
    folder_path = os.path.join(os.getcwd(), keyword)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Download images
    for i, url in enumerate(urls):
        download_image(url, folder_path, f'{keyword}_{i + 1}.jpg')

def main():
    keywords = ['fruits', 'cars', 'Machine Learning', 'Guitar', 'Cakes']
    for keyword in keywords:
        print(f'Scraping images for "{keyword}"...')
        scrape_images(keyword, num_images=10)
        print(f'Finished scraping images for "{keyword}".\n')

if __name__ == "__main__":
    main()


# 4. Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com
# and scrape following details for all the search results displayed on 1st page. Details to be scraped: “Brand
# Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”,
# “Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the
# details is missing then replace it by “- “. Save your results in a dataframe and CSV. 

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def get_flipkart_search_url(query):
    return f"https://www.flipkart.com/search?q={query}"

def get_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        return None

def parse_product_details(product):
    try:
        name = product.find('div', {'class': '_4rR01T'}).text.strip()
        brand = name.split()[0]
    except:
        name, brand = '-', '-'

    try:
        product_url = "https://www.flipkart.com" + product.find('a', {'class': '_1fQZEK'})['href']
    except:
        product_url = '-'

    try:
        price = product.find('div', {'class': '_30jeq3 _1_WHN1'}).text.strip()
    except:
        price = '-'

    # Default values
    color, ram, storage, primary_camera, secondary_camera, display_size, battery_capacity = '-', '-', '-', '-', '-', '-', '-'

    if product_url != '-':
        soup = get_soup(product_url)
        if soup:
            try:
                details = soup.find('table', {'class': '_14cfVK'}).find_all('tr')
                for detail in details:
                    th = detail.find('th').text.strip()
                    td = detail.find('td').text.strip()
                    if "Color" in th:
                        color = td
                    elif "RAM" in th:
                        ram = td
                    elif "Internal Storage" in th:
                        storage = td
                    elif "Primary Camera" in th:
                        primary_camera = td
                    elif "Secondary Camera" in th:
                        secondary_camera = td
                    elif "Display Size" in th:
                        display_size = td
                    elif "Battery Capacity" in th:
                        battery_capacity = td
            except:
                pass
    
    return {
        'Brand Name': brand,
        'Smartphone name': name,
        'Colour': color,
        'RAM': ram,
        'Storage(ROM)': storage,
        'Primary Camera': primary_camera,
        'Secondary Camera': secondary_camera,
        'Display Size': display_size,
        'Battery Capacity': battery_capacity,
        'Price': price,
        'Product URL': product_url
    }

def scrape_flipkart_smartphones(query):
    url = get_flipkart_search_url(query)
    soup = get_soup(url)
    if not soup:
        print("Failed to retrieve the search results page.")
        return []
    
    products = soup.find_all('div', {'class': '_1AtVbE'})
    smartphones_list = []

    for product in products:
        product_details = parse_product_details(product)
        if product_details['Smartphone name'] != '-':
            smartphones_list.append(product_details)
    
    return smartphones_list

def main():
    query = input("Enter the smartphone to search: ")
    smartphones = scrape_flipkart_smartphones(query)
    if smartphones:
        df = pd.DataFrame(smartphones)
        df.to_csv(f"{query}_smartphones.csv", index=False)
        print(f"Scraped data saved to {query}_smartphones.csv")
    else:
        print("No data scraped.")

if __name__ == "__main__":
    main()


# 5. Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_coordinates(city):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://maps.google.com')
    
    search_box = driver.find_element(By.ID, 'searchboxinput')
    search_box.send_keys(city)
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(5)  # Wait for the page to load
    
    current_url = driver.current_url
    driver.quit()
    
    try:
        # The URL contains the coordinates in the format: ".../@latitude,longitude,..."
        coordinates_part = current_url.split('/@')[1].split(',')[0:2]
        latitude = coordinates_part[0]
        longitude = coordinates_part[1]
        return latitude, longitude
    except Exception as e:
        print(f"Error extracting coordinates: {e}")
        return None, None

def main():
    city = input("Enter the city to search: ")
    latitude, longitude = get_coordinates(city)
    if latitude and longitude:
        print(f"Coordinates of {city}:")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    else:
        print("Failed to retrieve coordinates.")

if __name__ == "__main__":
    main()


# 6. Write a program to scrap all the available details of best gaming laptops from digit.in.

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        return None

def parse_laptop_details(laptop):
    try:
        name = laptop.find('h3').text.strip()
    except:
        name = '-'

    details = laptop.find_all('div', class_='Spcs-details')
    details_dict = {'Name': name}

    for detail in details:
        try:
            key = detail.find('div', class_='Spcs-key').text.strip()
            value = detail.find('div', class_='Spcs-value').text.strip()
            details_dict[key] = value
        except:
            continue
    
    return details_dict

def scrape_gaming_laptops(url):
    soup = get_soup(url)
    if not soup:
        print("Failed to retrieve the webpage.")
        return []
    
    laptops = soup.find_all('div', class_='TopNumbeHeading')
    laptops_list = []

    for laptop in laptops:
        laptop_details = parse_laptop_details(laptop)
        laptops_list.append(laptop_details)
    
    return laptops_list

def main():
    url = "https://www.digit.in/top-products/best-gaming-laptops-40.html"
    laptops = scrape_gaming_laptops(url)
    if laptops:
        df = pd.DataFrame(laptops)
        df.to_csv("best_gaming_laptops.csv", index=False)
        print("Scraped data saved to best_gaming_laptops.csv")
    else:
        print("No data scraped.")

if __name__ == "__main__":
    main()


# 7. Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped:
# “Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”. 

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        return None

def parse_billionaire_details(billionaire):
    try:
        rank = billionaire.find('div', class_='rank').text.strip()
    except:
        rank = '-'

    try:
        name = billionaire.find('div', class_='personName').text.strip()
    except:
        name = '-'

    try:
        net_worth = billionaire.find('div', class_='netWorth').text.strip()
    except:
        net_worth = '-'

    try:
        age = billionaire.find('div', class_='age').text.strip()
    except:
        age = '-'

    try:
        citizenship = billionaire.find('div', class_='countryOfCitizenship').text.strip()
    except:
        citizenship = '-'

    try:
        source = billionaire.find('div', class_='source').text.strip()
    except:
        source = '-'

    try:
        industry = billionaire.find('div', class_='category').text.strip()
    except:
        industry = '-'
    
    return {
        'Rank': rank,
        'Name': name,
        'Net worth': net_worth,
        'Age': age,
        'Citizenship': citizenship,
        'Source': source,
        'Industry': industry
    }

def scrape_forbes_billionaires(url):
    soup = get_soup(url)
    if not soup:
        print("Failed to retrieve the webpage.")
        return []
    
    billionaires = soup.find_all('div', class_='table-row')
    billionaires_list = []

    for billionaire in billionaires:
        billionaire_details = parse_billionaire_details(billionaire)
        billionaires_list.append(billionaire_details)
    
    return billionaires_list

def main():
    url = "https://www.forbes.com/billionaires/"
    billionaires = scrape_forbes_billionaires(url)
    if billionaires:
        df = pd.DataFrame(billionaires)
        df.to_csv("forbes_billionaires.csv", index=False)
        print("Scraped data saved to forbes_billionaires.csv")
    else:
        print("No data scraped.")

if __name__ == "__main__":
    main()


# 8. Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted
# from any YouTube Video. 

# In[ ]:


import os
import pandas as pd
from googleapiclient.discovery import build

# Set your API key here
api_key = 'YOUR_API_KEY'

# Function to get comments from a video
def get_comments(video_id, max_results=100):
    # Build a resource based on the YouTube API
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    # Retrieve comments
    comments = []
    results = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=max_results,
        textFormat='plainText'
    ).execute()

    while results:
        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append({
                'Comment': comment['textDisplay'],
                'Upvotes': comment['likeCount'],
                'Published At': comment['publishedAt']
            })
        
        # Check if there are more comments
        if 'nextPageToken' in results and len(comments) < 500:
            results = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                pageToken=results['nextPageToken'],
                maxResults=max_results,
                textFormat='plainText'
            ).execute()
        else:
            break

    return comments

def main():
    video_id = input("Enter the YouTube video ID: ")
    comments = get_comments(video_id, max_results=100)
    
    if comments:
        df = pd.DataFrame(comments)
        df.to_csv(f"{video_id}_comments.csv", index=False)
        print(f"Scraped {len(comments)} comments and saved to {video_id}_comments.csv")
    else:
        print("No comments scraped.")

if __name__ == "__main__":
    main()


# 9. Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in
# “London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall
# reviews, privates from price, dorms from price, facilities and property description. 

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to get soup object
def get_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        return None

# Function to parse hostel details
def parse_hostel_details(hostel):
    try:
        name = hostel.find('h2', class_='title').text.strip()
    except:
        name = '-'

    try:
        distance = hostel.find('span', class_='description').text.strip()
    except:
        distance = '-'

    try:
        rating = hostel.find('div', class_='score orange big').text.strip()
    except:
        rating = '-'

    try:
        total_reviews = hostel.find('div', class_='reviews').text.strip().split()[0]
    except:
        total_reviews = '-'

    try:
        overall_reviews = hostel.find('div', class_='keyword').text.strip()
    except:
        overall_reviews = '-'

    try:
        privates_from_price = hostel.find('a', class_='prices').find_all('div', class_='price')[0].text.strip()
    except:
        privates_from_price = '-'

    try:
        dorms_from_price = hostel.find('a', class_='prices').find_all('div', class_='price')[1].text.strip()
    except:
        dorms_from_price = '-'

    try:
        facilities = ', '.join([f.text for f in hostel.find_all('div', class_='facilities')])
    except:
        facilities = '-'

    try:
        property_description_url = "https://www.hostelworld.com" + hostel.find('a', class_='view-button')['href']
        soup = get_soup(property_description_url)
        property_description = soup.find('div', class_='property-description').text.strip()
    except:
        property_description = '-'
    
    return {
        'Hostel Name': name,
        'Distance from City Centre': distance,
        'Ratings': rating,
        'Total Reviews': total_reviews,
        'Overall Reviews': overall_reviews,
        'Privates From Price': privates_from_price,
        'Dorms From Price': dorms_from_price,
        'Facilities': facilities,
        'Property Description': property_description
    }

# Function to scrape hostels data
def scrape_hostels(url):
    soup = get_soup(url)
    if not soup:
        print("Failed to retrieve the webpage.")
        return []

    hostels = soup.find_all('div', class_='property')
    hostels_list = []

    for hostel in hostels:
        hostel_details = parse_hostel_details(hostel)
        hostels_list.append(hostel_details)
    
    return hostels_list

def main():
    url = "https://www.hostelworld.com/hostels/London"
    hostels = scrape_hostels(url)
    if hostels:
        df = pd.DataFrame(hostels)
        df.to_csv("london_hostels.csv", index=False)
        print("Scraped data saved to london_hostels.csv")
    else:
        print("No data scraped.")

if __name__ == "__main__":
    main()


# In[ ]:




