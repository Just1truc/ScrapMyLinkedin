import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import json
import time

def getCredentials(path):
    buffer = open(path, "r")
    inside = buffer.read()
    dict = json.loads(inside)
    if "username" in dict and "password" in dict:
        return dict["username"], dict["password"]
    return False, False

def connectUser():
    error = True

    driver = []
    i = 0

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    while (error):
        print("Please enter your informations :")
        if i==0:
            email_, password_ = getCredentials("./credentials.json")
            if email_ == False and password_ == False:
                print("Email Or Phone number: ", end="")
                email_ = input()
                print("Password: ", end="")
                password_ = input()
        else:
            print("Email Or Phone number: ", end="")
            email_ = input()
            print("Password: ", end="")
            password_ = input()

        print("Loading web page...")

        driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   chrome_options=options)
        driver.get('https://www.linkedin.com/uas/login')
        form = driver.find_element(by=By.CLASS_NAME, value="login__form")
        email_input = form.find_element(by=By.ID, value="username")
        password_input = form.find_element(by=By.ID, value="password")

        email_input.send_keys(email_)
        password_input.send_keys(password_)
        form.submit()

        post_response = BeautifulSoup(driver.page_source, features='lxml')
        workin = False
        error_username = ""
        error_password = ""
        while workin == False and driver.current_url != 'https://www.linkedin.com/feed/':
            if (post_response.find(id='error-for-username') != None and post_response.find(id='error-for-password') != None):
                error_username = str(post_response.find(id='error-for-username')).split('>')[1].split('<')[0]
                error_password = str(post_response.find(id='error-for-password')).split('>')[1].split('<')[0]
                workin = True
            else:
                time.sleep(1)
                post_response = BeautifulSoup(driver.page_source, features='lxml')


        if driver.current_url == 'https://www.linkedin.com/feed/':
            break

        print("An error occured. The credential must be invalids")
        print("The error is : " + error_username + error_password + "\n")
        driver.close()
        i += 1


    print('Connected !\n')
    return driver