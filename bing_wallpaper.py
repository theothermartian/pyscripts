###Jun19,2016
###@theothermartian
### Downloads bing wallpaper of the day on startup. Make this executable and add to .desktop file in ~/.config/autostart
#idea found on the web. Will improve as I learn.
# TODO : Make browser invisble
# Disadvantage : Using coordinates brngs with it the risk of the layout of webpage gettng modified in the future, which will fail this method
# Alternate easier way to get image : Query bing api to get image
#TODO featurise new display
#TODO featurise selenium else use webapi
#
# Prereq libs : selenium, [xvfb,pyvirtualdisplay], json
#
#
######################################


import urllib2
import os
from selenium import webdriver
from pyvirtualdisplay import Display


def getImage():
	#using fake display to open chrome 
	display = Display(visible=0, size=(800, 600))
	display.start()
	driver = webdriver.Chrome('./chromedriver') #path to chromedriver should be proper
	driver.get("http://www.bing.com/gallery/")
	assert "Bing Homepage Gallery" in driver.title

	#find the topmost element
	elem = driver.find_element_by_id("controlTop")
	action = webdriver.common.action_chains.ActionChains(driver)

	#click on the first image to its left, which is the latest image.
	action.move_to_element_with_offset(elem, 400, 20)
	action.click()
	action.perform()

	#http://selenium-python.readthedocs.io/locating-elements.html#locating-by-xpath
	img = driver.find_element_by_class_name('detailImage').get_attribute('src')

	assert "No results found." not in driver.page_source
	driver.close()

	display.stop()
	return img

def download(imgsrc):
	file_name = imgsrc.split('/')[-1]
	u = urllib2.urlopen(imgsrc)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (file_name, file_size)

	file_size_dl = 0
	block_sz = 8192
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
	        break

	    file_size_dl += len(buffer)
	    f.write(buffer)
	    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
	    status = status + chr(8)*(len(status)+1)
	    print status,

	f.close()
	return file_name

def setwallpaper(file_name):
	os.system("gsettings set org.gnome.desktop.background picture-uri file://" + os.getcwd() + "/"+file_name)
	os.system("notify-send \""+"Wallpaper changed to "+file_name.split(".")[0]+"\" ")
	os.remove(file_name)
	return

if __name__ == "__main__":
	imgsrc = getImage()
	file_name = download(imgsrc)
	setwallpaper(file_name)

