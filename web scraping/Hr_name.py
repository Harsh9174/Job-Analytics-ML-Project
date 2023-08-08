import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Load data from a CSV file and clean it by dropping rows with missing values
df = pd.read_csv("A:/Masai Projects/ML Project Job ANAlytics/Job_Data.csv")
df.dropna(inplace=True)
df.to_csv("A:/Masai Projects/ML Project Job ANAlytics/Job_Datacleaned.csv", index=False)

# Extract the 'Link' column values from the DataFrame
Link_L = []
for i in df['Link']:
    Link_L.append(i)

# Set up Selenium WebDriver using Chrome
driver = webdriver.Chrome(executable_path=r'C:/Users/Mi/Downloads/chromedriver_win32/chromedriver.exe')

HR_name = []
Experience = []

# Loop through the list of links
try:
    for link in Link_L:
        driver.get(link)
        
        # Find the HR name element on the page and append to HR_name list
        try:
            hr_name = driver.find_element(By.CLASS_NAME, "rec-name").text
            HR_name.append(hr_name)
            time.sleep(2)
        except:
            HR_name.append("NA")
        print(len(HR_name))
        
        # Find the Experience element on the page and append to Experience list
        try:
            exp = driver.find_element(By.XPATH, '//*[@id="floating-header"]/div[1]/div/span[2]').text
            Experience.append(exp)
        except:
            Experience.append("NA")

except:
    print("NA")

# Create a new DataFrame with HR names and experience data
df_hr_exp = pd.DataFrame({"HR_Name": HR_name, "Experience": Experience})

# Save the new DataFrame to a CSV file
df_hr_exp.to_csv("A:/Masai Projects/Job Analytics project/hr_exp.csv", index=False)
print(df_hr_exp)
