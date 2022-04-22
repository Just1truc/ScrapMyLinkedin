
import email
import re
from urllib import response
from requests import request, session
import time
# Importing
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def connectUser():
    error = True

    driver = []

    while (error):
        print("Please enter your informations :")
        print("Email Or Phone number: ", end="")
        email_ = input()
        print("Password: ", end="")
        password_ = input()

        print("Loading web page...")

        driver = webdriver.Chrome()
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


    print('Connected !\n')
    return driver

# Main
if __name__ == '__main__':
    print("Starting...")
    driver = connectUser()

    print("Please Enter the word you want to use to scrap peoples profiles: ", end="")
    word = input()
    print("Please enter the speed of scrapping (In seconds between each scrap to not seem sus): ", end="")
    speed = int(input())
    print("Please Enter the number of profile you want to get", end="")
    number_of_profile = int(input())

    profile_div = driver.find_element(by=By.CLASS_NAME, value="feed-identity-module__actor-meta")
    link = profile_div.find_element(by=By.CLASS_NAME, value="ember-view")
    link.click()
    print(driver.current_url)


    

