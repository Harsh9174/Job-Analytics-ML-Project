import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Load company data from an Excel file
df = pd.read_excel("A:\Masai Projects\ML Project Job ANAlytics/Remaning company.xlsx")

# Create a list to store company names
company = []

# Iterate through the 'Company' column and store company names in the list
for i in df['Company']:
    company.append(i)

# Set up the Selenium WebDriver using Chrome
service = Service('C:/Users/Mi/Downloads/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(executable_path=r'C:/Users/Mi/Downloads/chromedriver_win32/chromedriver.exe')

# LinkedIn URL
link = "https://www.linkedin.com/"

# Open LinkedIn in the browser
driver.get(link)
time.sleep(5)

# Find the username input field and enter the username
username = driver.find_element(By.XPATH,'//*[@id="session_key"]')
username.send_keys(str("harsh.agrawal9010@gmail.com"))
time.sleep(5)

# Find the password input field and enter the password
password = driver.find_element(By.XPATH,'//*[@id="session_password"]')
password.send_keys(str("Harsh@9174"))
time.sleep(5)

# Find the "Sign In" button and click it to log in
signin = driver.find_element(By.XPATH,'//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
signin.click()
time.sleep(60)

# Find the search box and prepare a list to store follower data
search_box = driver.find_element(By.XPATH,'//*[@id="global-nav-typeahead"]/input')
data = []

try:
    # Loop through the list of company names
    for comp in company:
        search_box.clear()
        search_box.send_keys(str(comp))
        search_box.send_keys(Keys.ENTER)
        time.sleep(8)
        
        try:
            # Find and extract follower information
            followers = driver.find_element(By.CLASS_NAME, 'reusable-search-simple-insight__text-container').text
            data.append([comp, followers])
            print(f"{comp}: {followers}")
        except:
            print("NA")
except:
    print("NA")

# Create a DataFrame from the collected follower data
df_followers = pd.DataFrame(data, columns=['company', 'followers'])

# Save the DataFrame to a CSV file
df_followers.to_csv("A:/Masai Projects/Job Analytics project/Followers.csv", index=False)
print(df_followers)
