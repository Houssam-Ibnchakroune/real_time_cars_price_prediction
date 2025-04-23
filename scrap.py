
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

def scrape_vehicle_data(vehicle_name_url):
    # Set up Selenium WebDriver (headless mode)
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    links = []
    n_p = 6  # Number of pages to scrape
    
    try:
        for i in range(1, n_p + 1):
            driver.get(f'https://www.avito.ma/fr/maroc/voitures_d_occasion/{vehicle_name_url}--%C3%A0_vendre?o={i}')
            WebDriverWait(driver, 10).until(
                lambda driver: driver.execute_script('return document.readyState') == 'complete'
            )
            html_content = driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            table = soup.find_all("a", class_='sc-1jge648-0 jZXrfL')
            for element in table:
                links.append(element.get('href'))
    finally:
        driver.quit()

    # Scrape the individual vehicle details
    dictionaries = []
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        for url in links:
            keys, values, list3, list4 = [], [], [], []
            pattern = r"^/vi/\d+\.htm$"  # Matches URLs in the format "/vi/number.htm"
            
            # Check if the URL matches the pattern
            if re.match(pattern, url):
                print(f"Skipping URL: {url}")
                continue 
            driver.get(url)
            
            WebDriverWait(driver, 10).until(
                lambda driver: driver.execute_script('return document.readyState') == 'complete'
            )
            
            # WebDriverWait(driver, 60).until(
            #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.sc-1g3sn3w-4 etbZjx'))
            # )
            html_content = driver.page_source

            
            soup = BeautifulSoup(html_content, 'html.parser')
            soup=soup.find("div", class_="sc-1g3sn3w-4 etbZjx")
            price = soup.find("div", class_="sc-1veij0r-8 unoEl")
            caracteristiques = soup.find("div",class_="sc-19cngu6-0 dnArJl")
            attribute_name = caracteristiques.find_all("span", class_="sc-1x0vz2r-0 bXFCIH")
            value = caracteristiques.find_all("span", class_="sc-1x0vz2r-0 fjZBup")

            for name, value in zip(attribute_name, value):
                keys.append(name.text)
                values.append(value.text)
            keys.append('price')
            values.append(price.text)
            dictionary = dict(zip(keys, values))
            dictionaries.append(dictionary)
            
            
            

            
    finally:
        driver.quit()

    df = pd.DataFrame(dictionaries)
    df.to_csv('data.csv', index=False)
    return df  


