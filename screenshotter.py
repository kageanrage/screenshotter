# script to log in to web interface of cameras in home network and take screenshots at regular intervals, then store
# these in a folder. Aim is to build up a database of photos capturing what parts of our home look like and how they
# change over time. Particularly the kids rooms in the evenings around bed time.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import pyautogui
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


def type_username_PAG(un):
    pyautogui.typewrite(un)


def type_username(un):
    elem = driver.find_element_by_id("username")
    elem.send_keys(un)
    elem.send_keys(Keys.TAB)


def click_centre_of_named_image(img_name):
    try:
        location = pyautogui.locateOnScreen(r'click_images\{}.png'.format(img_name), grayscale=True)
        centre = pyautogui.center(location)
        pyautogui.click(centre)
    except:
        print('{} button not found'.format(img_name))


def click_camera_button():
    driver.find_element_by_xpath("//div[contains(text(),'ch-btn play')]").click()



def type_pw_PAG(pwd):
    pyautogui.typewrite(pwd)


def type_pw(pwd):
    elem = driver.find_element_by_id("password")
    elem.send_keys(pwd)
    elem.send_keys(Keys.ENTER)


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
type_pw(cameras_pw)
click_camera_button()



# grab u/p from config file
# log in to web browser (firefox or IE?)
# go to first camera of interest
# use built-in photo-capture button, or maximise and screenshot
# rename image
# move image
# Do the same for the other cameras of interest
# email me if any failures occur
# create BAT file (in Windows) and schedule with Task Scheduler

