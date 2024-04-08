from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  # Import the Service class
from selenium.webdriver.chrome.service import Options  # Import the Service class
import os
from dotenv import load_dotenv


# Specify the path to your .env file
dotenv_path = '.env'

# Load the .env file
load_dotenv(dotenv_path)

driver_path = os.getenv("CHROME_DRIVER_PATH")

# Create an Options object and add the --headless argument
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")  # This option is often recommended for headless mode

# Initialize the WebDriver with the Service object and the Chrome options
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the website
driver.get('http://example.com')

# Find the first link on the page and click it
first_link = driver.find_element(By.TAG_NAME, 'a')
first_link.click()

# Close the browser window
driver.quit()
