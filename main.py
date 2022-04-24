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

class Profile:
    def __init__(self, subtitle, name, page_link, city):
        self.subtitle = subtitle
        self.name = name
        self.page_link = page_link
        self.city = city
        self.goodProfile = False

    def showData(self):
        if (self.goodProfile == True):
            print("=================")
            print("Name:", self.name)
            print("Subtitile:", self.subtitle)
            print("PageLink:", self.page_link)
            print("From:", self.city)
            print("=================\n")

class infoManagement:
    def __init__(self, word, speed, number, place):
        self.word = word
        self.speed = speed
        self.number_of_profile = number
        self.place = place
        self.profileList = []
        self.goodProfilesNbr = 0
        self.openlist = [] #list of links to profiles pages

    def showAllData(self):
        for profile in self.profileList:
            profile.showData()

    def innerHTMLOutputToString(self, string: str):
        return string.replace("<!---->","").replace("        ", "").replace("\n", "")

    def getProfile(self, driver):
        items = driver.find_elements(by=By.CLASS_NAME, value="entity-result__item")
        for element in items:
            subtitle_info = ""
            name_ = ""
            page_link_ = ""
            city_ = ""
            subtitle = element.find_element(by=By.CLASS_NAME, value="entity-result__primary-subtitle")
            subtitle_info = self.innerHTMLOutputToString(subtitle.get_attribute("innerHTML"))
            name_ = self.innerHTMLOutputToString(element.find_element(by=By.CLASS_NAME, value="entity-result__title-text").find_element(by=By.CSS_SELECTOR, value='[aria-hidden=true]').get_attribute("innerHTML"))
            page_link_ = element.find_element(by=By.CLASS_NAME, value="entity-result__title-text").find_element(by=By.CLASS_NAME, value="app-aware-link").get_attribute("href")
            city_ = self.innerHTMLOutputToString(element.find_element(by=By.CLASS_NAME, value="entity-result__secondary-subtitle").get_attribute("innerHTML"))
            newProfile = Profile(subtitle_info, name_, page_link_, city_)
            if (self.word.lower() in subtitle_info.lower()) and (self.place.lower() in city_.lower() or self.place.lower() == "none"):
                self.goodProfilesNbr += 1
                newProfile.goodProfile = True
            self.profileList.append(newProfile)
            self.openlist.append(page_link_)


    def browseThroughConnexions(self, driver):
        ## This function browse through the user connexion is the user is on his connexion page
        time.sleep(2)

        ##Find Profiles div elements and create Profiles values
        self.getProfile(driver)

        workdiv = driver.find_element(by=By.CLASS_NAME, value="search-results-container")
        driver.execute_script("window.scrollTo(0, 2000)")
        time.sleep(2)
        while not(workdiv.find_element(by=By.XPATH, value="//button[@aria-label='Suivant']").get_attribute("disabled")) and self.goodProfilesNbr < self.number_of_profile:
            workdiv.find_element(by=By.XPATH, value="//button[@aria-label='Suivant']").click()
            time.sleep(self.speed)
            workdiv = driver.find_element(by=By.CLASS_NAME, value="search-results-container")
            self.getProfile(driver)
            driver.execute_script("window.scrollTo(0, 2000)")
            time.sleep(self.speed)

# Main
if __name__ == '__main__':
    print("Starting...")
    driver = connectUser.connectUser()

    print("Please Enter the word you want to use to scrap peoples profiles: ", end="")
    word = str(input())
    print("Please Enter the place where you want to search (If you dont' want to search in a specific place : 'none'): ",end="")
    place = str(input())
    print("Please enter the speed of scrapping (In seconds : 1 is recommanded): ", end="")
    speed = int(input())
    print("Please Enter the number of profile you want to get: ", end="")
    number_of_profile = int(input())

    data = infoManagement(word, speed, number_of_profile, place)

    print("Getting to connections...")

    time.sleep(3)

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
    
    print("Scrapping, please wait...")

    data.browseThroughConnexions(driver)

    time.sleep(1)

    while (data.goodProfilesNbr < number_of_profile):
        driver.get(data.openlist[0])
        time.sleep(3)
        driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/ul/li/a").click()
        time.sleep(2)
        data.openlist.pop(0)
        data.browseThroughConnexions(driver)
        time.sleep(1)

    time.sleep(1)
    data.showAllData()

    time.sleep(1)
    driver.close()




    

