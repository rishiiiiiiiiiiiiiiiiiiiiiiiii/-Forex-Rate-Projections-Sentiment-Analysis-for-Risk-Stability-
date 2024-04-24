import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

# Set up ChromeOptions for headless browsing
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration

# Set up the Selenium driver
driver = webdriver.Chrome('D:/Softwares/chromedriver.exe', options=chrome_options)

# Reading the csv file - 1208
df = pd.read_csv('japan - Copy.csv')
list_index = []

# Empty list to store the data
articles = []

# Navigate to the URL
for i in range(385):
    link = df.iloc[i]['URL link']
    driver.get(str(link))

    # Wait for the page to load
    driver.implicitly_wait(10)

    if i not in list_index:
        print(i)
        # Find the article content element
        article_content = driver.find_element_by_xpath("//div[1]/div[5]/div/div/main/article/div/div[3]")

        # Extract the article content
        article_content = article_content.text.strip()
        article_content = ' '.join(re.split(r'\n', article_content))
        articles.append(article_content)

        # Find the article content element
        # article_content = driver.find_element_by_xpath("//div[3]/div/div[1]/div[4]/div[3]/div[2]")
        #
        # # Extract the article content
        # article_content = article_content.text.strip()
        # article_content = ' '.join(re.split(r'\n', article_content))
        # articles.append(article_content)


df['Article'] = articles

csv_name = 'japan_data2.csv'
df.to_csv(csv_name, index=False)
