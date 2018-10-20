
#UNFOLLOW
import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
# if headless == True:
#options.add_argument("headless")
options.add_argument("user-data-dir='./data'") #Your google chrome data
driver = webdriver.Chrome('./chromedriver',chrome_options=options)
driver.implicitly_wait(5)

url = 'https://shopee.co.id/shop/21943822/following/?__classic__=1'
driver.get(url)
while(1):
    print("program running")
    while(1):
        driver.find_element_by_xpath('//body').send_keys(Keys.END) 
        follower_list = driver.find_element_by_class_name("follower-list")
        jumlah_button = follower_list.find_elements_by_xpath("//li")
        loading = driver.find_element_by_class_name('loading-text').text
        print "Jumlah Button : "+str(len(jumlah_button))
        
        if (len(jumlah_button) < 10 or len(jumlah_button) >= 2100 or loading == 'Tidak ada pengikut lainnya'):
            break
    if len(jumlah_button) > 1 :
        driver.find_element_by_xpath('//body').send_keys(Keys.COMMAND + Keys.UP)
        time.sleep(1)
        print "jumlah button : "+str(len(jumlah_button))
        follows = follower_list.find_elements_by_xpath("//div[contains(text(),'+')]")
        print "jumlah button Ikuti : "+str(len(follows))
        followed = follower_list.find_elements_by_xpath("//div[contains(@class,'btn-follow') and contains(text(),'Mengikuti')]")
        print "jumlah button Mengikuti : "+str(len(followed))
        followed.reverse()
        for i,x in enumerate(followed):
            if (i % 5) == 0:
                driver.find_element_by_xpath('//body').send_keys(Keys.HOME)
            elif (i > 500):
                break
            time.sleep(random.randint(0, 2))
            print("{} unfollow id: {} ".format(i+1,x.get_attribute('shopid')))
            x.click()
        print('end')
    else:
        print('Skip karna button kurang')
   
