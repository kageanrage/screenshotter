# script to log in to web interface of cameras in home network and take screenshots at regular intervals, then store
# these in a folder. Aim is to build up a database of photos capturing what parts of our home look like and how they
# change over time. Particularly the kids rooms in the evenings around bed time.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from config import Config
import sys


cfg = Config()


def which_cameras():    # reads in arg string from batch file
    if len(sys.argv) > 1:
        cams_str = str(sys.argv[1])  # takes the desired cameras string from the command line arg, passed by the batch file
    else:
        cams_str = "No arguments passed"
    return cams_str


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
izzy_cam_css = "#channel > div > div.channel-list > div:nth-child(1) > div:nth-child(1) > div"
photo_button_css = "#tool > div > div.tool-r > span > button:nth-child(2) > i"
nate_cam_css = "#channel > div > div.channel-list > div:nth-child(2) > div:nth-child(1) > div"
backyard_cam_css = "#channel > div > div.channel-list > div:nth-child(2) > div:nth-child(1) > div"
alfresco_cam_css = "#channel > div > div.channel-list > div:nth-child(4) > div:nth-child(1) > div"
driveway_cam_css = "#channel > div > div.channel-list > div:nth-child(3) > div:nth-child(1) > div"


machine = which_pc()
cams = which_cameras()  # reads in arg string from batch file

ie_path = get_ie_path()
driver = webdriver.Ie(ie_path)
driver.get(cfg.cameras_url)  # load cameras page - take URL from config file

type_username(cfg.cameras_uname)
driver.implicitly_wait(3)
type_pw(cfg.cameras_pw)

if 'Izzy' in cams:  # if the string 'Izzy' appears in the argument...
    click_based_on_css_selector(izzy_cam_css)  # select cam 1
    driver.implicitly_wait(3)
    time.sleep(1)
    click_based_on_css_selector(photo_button_css)  # click photo button

if 'Nate' in cams:  # if the string 'Nate' appears in the argument...
    click_based_on_css_selector(nate_cam_css)  # select cam 1
    driver.implicitly_wait(3)
    time.sleep(2)
    click_based_on_css_selector(photo_button_css)  # click photo button

if 'Backyard' in cams:  # if the string 'Backyard' appears in the argument...
    click_based_on_css_selector(backyard_cam_css)  # select cam 1
    driver.implicitly_wait(3)
    time.sleep(5)
    click_based_on_css_selector(photo_button_css)  # click photo button

driver.quit()

# To Do:
# will need to schedule backyard snaps for daytime, so need to be able to pass argument to script which determines
# which cameras to snapshot. Pass from BAT file, then use scheduling to trigger the right batch file at the right time
#  of day/night
