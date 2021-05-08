from selenium import webdriver
import time
import os
from os.path import dirname, join
from dotenv import load_dotenv
from xlwt import Workbook
import pandas as pd

dotenv_path = join(dirname('.env'), '.env')
load_dotenv(dotenv_path)
 
#from webdriver_manager.chrome import ChromeDriverManager
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options, executable_path="/home/ashu/Desktop/projects/linkedin_scrapper_tester/chromedriver")

browser.get("https://www.linkedin.com")
#browser.save_screenshot("foo.png")

username = browser.find_element_by_id('session_key')
username.send_keys(os.environ.get("USERNAME"))
password = browser.find_element_by_id('session_password')
password.send_keys(os.environ.get("PASSWORD"))


login_button = browser.find_element_by_class_name("sign-in-form__submit-button")
login_button.click()

time.sleep(5)
# browser.save_screenshot("foo3.png")
df = pd.read_excel("/home/ashu/Desktop/projects/linkedin_scrapper_tester/sample_1.xlsx")

wb = Workbook()
sheet1 = wb.add_sheet("Sheet 1")
for i in df.index:
    company_url = df['link'][i]
    company_name = df['name'][i]

    browser.get(company_url+'/about')
    time.sleep(0.5)


    elem = browser.find_elements_by_class_name("org-page-details__definition-text")

    # for ele in elem:
    #     print(ele.text)
    company_type = "private"
    for ele in elem:
        if ele.text.find("Public") != -1:
            company_type = "public"


    company_size = browser.find_element_by_class_name("org-about-company-module__company-size-definition-text").text
    # print(company_size.text)
    

    
    sheet1.write(i, 0, company_name)
    sheet1.write(i, 1, company_type)
    sheet1.write(i, 2, company_size)

wb.save("return.xlsx")

