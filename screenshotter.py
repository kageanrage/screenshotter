# script to log in to web interface of cameras in home network and take screenshots at regular intervals, then store
# these in a folder. Aim is to build up a database of photos capturing what parts of our home look like and how they
# change over time. Particularly the kids rooms in the evenings around bed time.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time


def which_pc():
    if os.path.exists(r"C:\Program Files\StableBit\DrivePool"):
        return 'desktop'
    else:
        return 'laptop'


def get_ie_path():
    if machine == 'desktop':
        return r'C:\Github local repos\selenium IE driver\IEDriverServer.exe'
    else:
        return r'C:\selenium\IEDriverServer.exe'


def get_config_file():
    if machine == 'desktop':
        config = r"C:\Github local repos\dont_share\config.txt"
    else:
        config = r"C:\KP Python\dont_share\config.txt"
    return config


def get_cameras_url():
    f = open(config_file, 'r')  # import config info
    f_str = str((f.read()))  # import config info
    url = f_str[174:214]
    return url


def get_cameras_uname():
    f = open(config_file, 'r')  # import config info
    f_str = str((f.read()))  # import config info
    uname = f_str[237:244]
    return uname


def get_cameras_pw():
    f = open(config_file, 'r')  # import config info
    f_str = str((f.read()))  # import config info
    pw = f_str[267:281]
    return pw


def type_username(un):
    elem = driver.find_element_by_id("username")
    elem.send_keys(un)
    elem.send_keys(Keys.TAB)


def click_based_on_css_selector(css_sel):
    button_element = driver.find_element_by_css_selector(css_sel)
    button_element.click()


def type_pw(pwd):
    elem = driver.find_element_by_id("password")
    elem.send_keys(pwd)
    elem.send_keys(Keys.ENTER)


# CSS selectors
izzy_cam_css = "div.ch:nth-child(1) > div:nth-child(1) > div:nth-child(1)"
photo_button_css = "span.ng-scope:nth-child(1) > button:nth-child(2)"
nate_cam_css = ""
backyard_cam_css = ""


machine = which_pc()
config_file = get_config_file()
cameras_url = get_cameras_url()
cameras_username = get_cameras_uname()
cameras_pw = get_cameras_pw()
photos_dir = r'H:\Photos\ipcam'


ie_path = get_ie_path()
driver = webdriver.Ie(ie_path)
driver.get(cameras_url)  # load cameras page - take URL from config file

type_username(cameras_username)
driver.implicitly_wait(3)
type_pw(cameras_pw)
click_based_on_css_selector(izzy_cam_css)  # select cam 1
driver.implicitly_wait(3)
click_based_on_css_selector(photo_button_css)  # click photo button
driver.quit()


# Do the same for the other cameras of interest
# email me if any failures occur
