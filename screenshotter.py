# script to log in to web interface of cameras in home network and take screenshots at regular intervals, then store
# these in a folder. Aim is to build up a database of photos capturing what parts of our home look like and how they
# change over time. Particularly the kids rooms in the evenings around bed time.

from selenium import webdriver



# Open web browser (selenium)
ie_path = r'C:\selenium\IEDriverServer.exe'
driver = webdriver.Ie(ie_path)
driver.get('INSERT URL HERE') # load cameras page - take URL from config file




# grab u/p from config file
# log in to web browser (firefox or IE?)
# go to first camera of interest
# use built-in photo-capture button, or maximise and screenshot
# rename image
# move image
# Do the same for the other cameras of interest
# email me if any failures occur
# create BAT file (in Windows) and schedule with Task Scheduler

