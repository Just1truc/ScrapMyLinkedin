import sys
import email
import re
from urllib import response
from requests import request, session
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup

from sources.connectUser import connectUser
sys.path.insert(1,'./sources/')
import connectUser

# Main
if __name__ == '__main__':
    print("Starting...")
    driver = connectUser.connectUser()

    print("Please Enter the word you want to use to scrap peoples profiles: ", end="")
    word = input()
    print("Please enter the speed of scrapping (In seconds between each scrap to not seem sus): ", end="")
    speed = int(input())
    print("Please Enter the number of profile you want to get: ", end="")
    number_of_profile = int(input())

    print("Getting to connections...")

    time.sleep(2)

    profile_div = driver.find_element(by=By.CLASS_NAME, value="feed-identity-module__actor-meta")
    link = profile_div.find_element(by=By.CLASS_NAME, value="ember-view")
    link.click()

    time.sleep(2)

    profile_div = driver.find_element(by=By.CLASS_NAME, value="ph5")
    links = profile_div.find_elements(by=By.TAG_NAME, value="a")
    for elem in links:
        if (elem.get_attribute("href") == "https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH"):
            elem.click()
            break

    time.sleep(5)

    items = driver.find_elements(by=By.CLASS_NAME, value="entity-result__item")
    for element in items:
        subtitle = element.find_element(by=By.CLASS_NAME, value="entity-result__primary-subtitle")
        print(subtitle.get_attribute("innerHTML").replace("<!---->","").replace("        ", "").replace("\n", ""))

    workdiv = driver.find_element(by=By.CLASS_NAME, value="search-results-container")
    driver.execute_script("window.scrollTo(0, 2000)")
    time.sleep(2)
    while not(workdiv.find_element(by=By.XPATH, value="//button[@aria-label='Suivant']").get_attribute("disabled")):
        workdiv.find_element(by=By.XPATH, value="//button[@aria-label='Suivant']").click()
        time.sleep(3)
        workdiv = driver.find_element(by=By.CLASS_NAME, value="search-results-container")
        items = driver.find_elements(by=By.CLASS_NAME, value="entity-result__item")
        for element in items:
            subtitle = element.find_element(by=By.CLASS_NAME, value="entity-result__primary-subtitle")
            print(subtitle.get_attribute("innerHTML").replace("<!---->","").replace("        ", "").replace("\n", ""))
        driver.execute_script("window.scrollTo(0, 2000)")
        time.sleep(3)
        

    time.sleep(2)

    

