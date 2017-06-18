# script to log in to web interface of cameras in home network and take screenshots at regular intervals, then store
# these in a folder. Aim is to build up a database of photos capturing what parts of our home look like and how they
# change over time. Particularly the kids rooms in the evenings around bed time.

from selenium import webdriver
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


def check_for_logo():
    try:
        location = pyautogui.locateOnScreen(r'click_images\logo.png')
        print('Logo found at {}'.format(location))
    except:
        print('Logo not found')


def click_allow_button():
    try:
        location = pyautogui.locateOnScreen(r'click_images\username.png')  #
        centre = pyautogui.center(location)
        pyautogui.click(centre)
    except:
        print('Allow button not found')


def type_username(un):
    pyautogui.typewrite(un)


def click_username_field():
    try:
        location = pyautogui.locateOnScreen(r'click_images\username.png')  #
        centre = pyautogui.center(location)
        pyautogui.click(centre)
    except:
        print('username button not found')


def click_pw_field():
    try:
        location = pyautogui.locateOnScreen(r'click_images\password.png')  #
        centre = pyautogui.center(location)
        pyautogui.click(centre)
    except:
        print('pw button not found')


def type_pw(pwd):
    pyautogui.typewrite(pwd)


machine = which_pc()
config_file = get_config_file()
cameras_url = get_cameras_url()
cameras_username = get_cameras_uname()
cameras_pw = get_cameras_pw()


# Open web browser (selenium)
ie_path = get_ie_path()
driver = webdriver.Ie(ie_path)
driver.get(cameras_url)  # load cameras page - take URL from config file
time.sleep(1)
# check_for_logo()  # use for testing
time.sleep(1)   # required to give pyautogui time to view the page
click_allow_button()
time.sleep(1)
# enter_u_p()
# click_username_field()    # Not required as automatically selects this field
type_username(cameras_username)
click_pw_field()
type_pw(cameras_pw)





# grab u/p from config file
# log in to web browser (firefox or IE?)
# go to first camera of interest
# use built-in photo-capture button, or maximise and screenshot
# rename image
# move image
# Do the same for the other cameras of interest
# email me if any failures occur
# create BAT file (in Windows) and schedule with Task Scheduler

