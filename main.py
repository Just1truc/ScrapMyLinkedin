

from urllib import response
from requests import request, session
# Importing
import requests
from bs4 import BeautifulSoup


# Main
if __name__ == '__main__':
    print("Starting...")
    URL = 'https://www.linkedin.com/uas/login'
    session = requests.session()
    login_response = session.get('https://www.linkedin.com/uas/login')
    login = BeautifulSoup(login_response.text, features="lxml")

    # Get hidden form inputs

    inputs = login.find(class_ = 'login__form')
    print(inputs.prettify())
    inputs = inputs.find_all('input', {'type': ['hidden', 'submit']})

    # Create POST data
    post = {input.get('name'): input.get('value') for input in inputs}
    print(post)
    print("Enter Username : ", end="")
    username = str(input())
    print("Enter Password : ", end="")
    password = str(input())
    post['session_key'] = username
    post['session_password'] = password

    # Post login
    post_response = session.post('https://www.linkedin.com/checkpoint/lg/login-submit', data=post)
    print(post_response.status_code)

    # Get home page
    home_response = session.get('http://www.linkedin.com/')
    home = BeautifulSoup(home_response.text, features="lxml")
    #print(home)
