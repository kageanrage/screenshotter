# script to log in to web interface of cameras in home network and take screenshots at regular intervals, then store
# these in a folder. Aim is to build up a database of photos capturing what parts of our home look like and how they
# change over time. Particularly the kids rooms in the evenings around bed time.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from config import Config


cfg = Config()


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

ie_path = get_ie_path()
driver = webdriver.Ie(ie_path)
driver.get(cfg.cameras_url)  # load cameras page - take URL from config file

type_username(cfg.cameras_uname)
driver.implicitly_wait(3)
type_pw(cfg.cameras_pw)
click_based_on_css_selector(izzy_cam_css)  # select cam 1
driver.implicitly_wait(3)
click_based_on_css_selector(photo_button_css)  # click photo button
driver.quit()


# Do the same for the other cameras of interest
# email me if any failures occur
