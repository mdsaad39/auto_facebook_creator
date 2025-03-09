import random
import csv
from datetime import datetime, timedelta
from passwordgenerator import pwgenerator
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import names
import json
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui





def generate_algerian_phone_number():
    # Choose a random mobile network code
    network_codes = ["05", "06", "07"]
    mobile_network_code = random.choice(network_codes)

    # Generate a random subscriber number
    subscriber_number = "".join([str(random.randint(0, 9)) for _ in range(8)])

    # Concatenate the parts to form the phone number
    phone_number = f"+213 {mobile_network_code} {subscriber_number}"
    return phone_number

def generate_gender():
    genders = ['Male', 'Female']
    return random.choice(genders)

def generate_username(f, l):
    unique_numbers = random.sample(range(1000, 10000), 4)
    username = (f[0] + l).lower() + "_" + str(unique_numbers[0])
    return username

def generate_name_from_csv(gender):
    if gender == 'Female':
        filename = 'ww/ww.csv'
    else:
        filename = 'bb/wb.csv'
    # Read in the data from the CSV file
    names = []
    probabilities = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            names.append(row[1])
            probabilities.append(float(row[0]))

    # Generate a name based on the probabilities
    name = random.choices(names, weights=probabilities)[0]
    return name

def generate_last_name_from_csv():
    filename = 'lastNames.csv'
    # Read in the data from the CSV file
    names = []
    probabilities = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            names.append(row[0])
            probabilities.append(float(row[1]))

    # Generate a name based on the probabilities
    name = random.choices(names, weights=probabilities)[0]
    return name



# Open Chrome browser
# Specify the path to the profile directory
from selenium.webdriver.firefox.options import Options

# Specify the path to the Tor Browser's Firefox executable
tor_executable_path = r'Tor Browser\Browser\firefox.exe'

# Create FirefoxOptions object
firefox_options = Options()

# Configure the proxy settings for Tor
firefox_options.set_preference('network.proxy.type', 1)
firefox_options.set_preference('network.proxy.socks', '127.0.0.1')
firefox_options.set_preference('network.proxy.socks_port', 9150)

# Set the path to the Tor Browser's Firefox executable
firefox_options.binary_location = tor_executable_path

# Create the FirefoxDriver using the FirefoxOptions
driver = webdriver.Firefox(options=firefox_options)
time.sleep(5)

time.sleep(1)  # Wait for 1 second

pyautogui.press('esc')

connect_button = driver.find_element(By.ID, "connectButton")

connect_button.click()
time.sleep(20)

# Navigate to the website
driver.get("https://www.fakemailgenerator.com/")

driver.execute_script("window.stop();")


# Wait for the page to load
#driver.execute_script("window.stop();")

email_input = driver.find_element(By.ID, "home-email")
email = email_input.get_attribute("value")
domain_button = driver.find_element(By.ID, "domain-select")
domain = domain_button.text.strip()
g = generate_gender()
f = generate_name_from_csv(g)
l = generate_last_name_from_csv()

# Password
password_gen = pwgenerator.generate()



# Print the profile information
profile_info = {
    "Email": email+domain,
    "Password": password_gen,
    "First Name": f,
    "Last Name": l,
    "Gender": g,
}

print(json.dumps(profile_info))
driver.execute_script("window.open('about:blank', '_blank');")
facebook = 'https://www.facebook.com/'
driver.switch_to.window(driver.window_handles[-1])
driver.get(facebook)
time.sleep(3)
try:
    button = driver.find_element(By.CSS_SELECTOR, 'button[data-cookiebanner="accept_button"][title="Allow all cookies"]')
    button.click()

except NoSuchElementException:
    print("Button not found on the page.")

# fill the regestration page 
#===========================================================================
element = driver.find_element(By.CLASS_NAME, "_4jy2")
element.click()
wait = WebDriverWait(driver, 50)

firstname = wait.until(EC.visibility_of_element_located((By.NAME, "firstname")))
lastname = driver.find_element(By.NAME, "lastname")
email = driver.find_element(By.NAME, "reg_email__")
#time.sleep(1)
#email_confirmation = driver.find_element(By.NAME, "reg_email_confirmation__")
password = driver.find_element(By.NAME, "reg_passwd__")
birthday_day = driver.find_element(By.NAME, "birthday_day")
birthday_month = driver.find_element(By.NAME, "birthday_month")
time.sleep(1)

birthday_year = driver.find_element(By.NAME, "birthday_year")
gender = driver.find_element(By.NAME, "sex")
gender_buttons = driver.find_elements(By.CSS_SELECTOR, 'span._5k_2._5dba')



#fill
firstname.send_keys(f)
lastname.send_keys(l)
email.send_keys(profile_info["Email"])
time.sleep(1)
try:
    email_confirmation = driver.find_element(By.NAME, "reg_email_confirmation__")
    email_confirmation.send_keys(profile_info["Email"])
except NoSuchElementException:
    pass

password.send_keys(password_gen)
# Randomly select a day between 1 and 31
day = random.randint(1, 28)

# Randomly select a month from the available options
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
month = random.choice(months)



# Randomly select a year between 1905 and 2023

year = random.randint(1988, 2005)
# Update the form fields with the random values
#birthday_day.send_keys(str(day))
birthday_month.send_keys(month)

ActionChains(driver).move_to_element(birthday_day).click().perform()
desired_day = str(day)  # Convert the generated day to string
day_option = driver.find_element(By.XPATH, f'//option[@value="{desired_day}"]')
day_option.click()
time.sleep(1)

ActionChains(driver).move_to_element(birthday_year).click().perform()
desired_year = str(year) 
year_option = driver.find_element(By.XPATH, f'//option[@value="{desired_year}"]')
year_option.click()



if g == 'Female':
    female_button = gender_buttons[0].find_element(By.CSS_SELECTOR, 'input[type="radio"][name="sex"][value="1"]')
    female_button.click()
else:
    male_button = gender_buttons[1].find_element(By.CSS_SELECTOR, 'input[type="radio"][name="sex"][value="2"]')
    male_button.click()


driver.find_element(By.NAME, 'websubmit').click()
time.sleep(5)


#get the confermation code
#==============================================================================
driver.switch_to.window(driver.window_handles[0])
print("switched and sleep")
driver.refresh()
confirmation_code_element = WebDriverWait(driver, 300).until(
    EC.visibility_of_element_located((By.XPATH, '//dd[contains(text(), "Facebook confirmation code")]'))
)
# Extract the confirmation code from the element
# Extract the confirmation code from the element and exclude "FB-"
confirmation_code = confirmation_code_element.text.split(' ')[0].replace("FB-", "")

print(f"confermation code {confirmation_code}")

#go back and confirm 
#==================================================================================
driver.switch_to.window(driver.window_handles[-1])
input_field = driver.find_element(By.ID, "code_in_cliff")
input_field.send_keys(confirmation_code)
#time.sleep(5)
continue_button = driver.find_element(By.CSS_SELECTOR, 'button._42ft.mls._4jy0._8iu3._8iu6._4jy4._4jy1.selected._51sy')
continue_button.click()

time.sleep(15)
driver.get("https://www.facebook.com/ItzMouhLaad")
time.sleep(5)
menu_button = driver.find_element(By.XPATH, '//div[@aria-label="See options"]')
menu_button.click()


# Wait for the menu to expand
time.sleep(3)

# Find and click the "Follow" option from the expanded menu
follow_option = driver.find_element(By.XPATH, '//span[text()="Follow"]')
follow_option.click()
print(f"{profile_info['Email']} followed you")
driver.quit()

