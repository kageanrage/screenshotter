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



def type_username(un):
    pyautogui.typewrite(un)


def click_centre_of_named_image(img_name):
    try:
        location = pyautogui.locateOnScreen(r'click_images\{}.png'.format(img_name))  #
        centre = pyautogui.center(location)
        pyautogui.click(centre)
    except:
        print('{} button not found'.format(img_name))




def type_pw(pwd):
    pyautogui.typewrite(pwd)


machine = which_pc()
config_file = get_config_file()
cameras_url = get_cameras_url()
cameras_username = get_cameras_uname()
cameras_pw = get_cameras_pw()
photos_dir = r'H:\Photos\ipcam'


# Open web browser (selenium)
ie_path = get_ie_path()
time.sleep(1)
driver = webdriver.Ie(ie_path)
driver.get(cameras_url)  # load cameras page - take URL from config file
time.sleep(1)
# click_centre_of_named_image('logo')  # use for testing
time.sleep(1)   # required to give pyautogui time to view the page
# click_centre_of_named_image('allow')
time.sleep(1)
# enter_u_p()
# click_centre_of_named_image('username')    # Not required as automatically selects this field

type_username(cameras_username)
time.sleep(1)
pyautogui.press('enter')
# click_centre_of_named_image('password')   # using tab instead as image recognition was inconsistent
time.sleep(1)
type_pw(cameras_pw)
pyautogui.press('enter')
time.sleep(1)
click_centre_of_named_image('izzy')
time.sleep(1)
click_centre_of_named_image('maximise')
time.sleep(1)
click_centre_of_named_image('take_photo')
time.sleep(1)
click_centre_of_named_image('reduce_window_size')
time.sleep(1)
click_centre_of_named_image('quit_x')


### This all runs fine from PyCharm and batch file, but through scheduler doesn't find Izzy. So annoying.



# grab u/p from config file
# log in to web browser (firefox or IE?)
# go to first camera of interest
# use built-in photo-capture button, or maximise and screenshot
# rename image
# move image
# Do the same for the other cameras of interest
# email me if any failures occur
# create BAT file (in Windows) and schedule with Task Scheduler

