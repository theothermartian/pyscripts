Daily wallpaperchanger changes the currentwallpaper to the bing wallpaper of the day(US).
Dependencies : Selenium
Selenium is used to simulate a click on the bing.com/wallpaper page to bring up the hidden element of the current wallpaper, then proceeds
to extract the link and the date

Much more easier way is to use an bing api to query the image info in json and then download that, but wheres the fun in that!
Usage : make this script executable that is give rwx permission and set this script to run in /etc/rc.local
TODO : 
