#!/usr/bin/env python
# coding: utf-8

from arcgis.gis import GIS
import time, getpass

portal_URL = input("Portal URL: ")

# Built-in
username = input("Username: ")
password = getpass.getpass(prompt='Password: ', stream=None)
gis = GIS(portal_URL, username, password)

# IWA
# gis = GIS(portal_URL)

# SAML
# clientID = input("App ID: ")
# gis = GIS(portal_URL, client_id=clientID)

all_users = gis.users.search(max_users=1000)

for user in all_users:
    
    username = user.username
    last_login = user.lastLogin
    
    if last_login != -1:
        last_login = time.localtime(user.lastLogin/1000)
        date = "{}/{}/{} {}:{}".format(last_login[0], last_login[1], last_login[2], last_login[3], last_login[4])
    else:
        date = "Never"
    
    print("User: {}\nLast active: {}\n".format(username, date))