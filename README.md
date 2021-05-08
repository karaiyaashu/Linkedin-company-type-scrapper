# Linkedin Scrapper 
## To get  company type and number of employee tag from company profile


**Installation**

pip install -r requirements.txt


**Chrome Driver**


Download the correct chromedriver from the following link
https://chromedriver.chromium.org/downloads


**enviroment variable**

Create a .env file with

> USERNAME='YOUR_LINKEDIN_LOGIN_EMAIL'

>PASSWORD='YOUR_LINKEDIN_PASSWORD'


**setup**

path to your chrome driver 

>browser = webdriver.Chrome(options=chrome_options, executable_path="path_to_chromedriver")


path to input file

>df = pd.read_excel("path_to_input_excel_file")


**RUN**
>python3 main.py