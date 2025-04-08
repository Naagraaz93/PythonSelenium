from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set Chrome options to detach browser
options = Options()
options.add_experimental_option("detach", True)

# Start Chrome with the detach option
driver = webdriver.Chrome(options=options)

# Open a website
driver.get("https://selenium.dev")
