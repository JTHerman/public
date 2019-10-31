import requests
import getpass

url = "https://www.arcgis.com/sharing/rest/generateToken"

portal_url = input("Portal URL: ")
username = input("Username: ")
password = getpass.getpass("Password: ")

params = {
    'username': username,
    'password': password,
    'referer': "https://www.arcgis.com",
    'f': "json"
    }

response = requests.post(url, params)

try:
    d = response.json()
    print("Token: {}".format(d['token']))
except KeyError:
    print("You put something in wrong!")