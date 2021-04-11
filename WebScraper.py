# Python program to illustrate web Scraping

from selenium import webdriver  # Selenium is a web testing library. It is used to automate browser activities.
from bs4 import BeautifulSoup  # Beautiful Soup is a Python package for parsing HTML and XML documents. It creates
# parse trees that is helpful to extract the data easily.
import pandas as pd  # Pandas is a library used for data manipulation and analysis. It is used to extract

# the data and store it in the desired format.

# To configure webdriver to use Chrome browser, we have to set the path to chromedriver
driver = webdriver.Chrome(executable_path='C:/Users/VIDHI/PycharmProjects/WebScraper/chromedriver_win32/chromedriver'
                                          '.exe')
names = []

driver.get("https://www.cs.usc.edu/directory/faculty/")

content = driver.page_source
soup = BeautifulSoup(content, features="lxml")

for link in soup.findAll('div', attrs={'class': 'faculty-text'}):
    print("Inside for loop")
    name = link.find('h5', attrs={'class': 'resultName'})
    print("name:", name)
    # description = link.find('div', attrs={'class': ''})
    # print("description:", description)
    # email_id = link.find('a', attrs={'class': '_3LWZlK'})
    # print("email_id:", email_id)
    names.append(name.text)
    # prices.append(description.text)
    # ratings.append(email_id.text)

df = pd.DataFrame({'Name': names})
df.to_csv('faculties.csv', index=False, encoding='utf-8')
