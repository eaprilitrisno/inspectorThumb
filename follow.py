#FOLLOW
import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
# if headless == True:
options.add_argument("headless")
options.add_argument("user-data-dir='./data'") #Your google chrome data
driver = webdriver.Chrome('./chromedriver',chrome_options=options)
driver.implicitly_wait(5)

url='https://mall.shopee.co.id/shop/#storeId#/#mode#'
list=[
    '10793796','24761278',
    '35883462','36302070','32145986','26479353',
    '7299953','85890646','1289539','7358663',
    '61648718','17146406','2200193','1405703',
    '22597209','20620987','52635036','51925611',
    '30232273','60755826','39277435','39011576',
    '30156064','79571727','16762565','5416318',
    '5355413','3918467','30618903','62754204',
    '5544507','20091889','2161821','2821325',
    '28160481','10919960','13140292','85473960',
    ]
mode=['following','followers']
try: 
    for x in list:
        for h in mode:
            j = url
            target = j.replace('#storeId#',x).replace('#mode#',h)
            driver.get(target)
            print("program running")
            while(1):
                driver.find_element_by_xpath('//body').send_keys(Keys.END)
                time.sleep(3)
                follower_list = driver.find_element_by_class_name("follower-list")
                jumlah_button = driver.find_elements_by_xpath("//li")
                loading = driver.find_element_by_class_name('loading-text').text
                if (len(jumlah_button) < 10 or len(jumlah_button) >= 100 or loading == 'Tidak ada pengikut lainnya'):
                    break
            if len(jumlah_button) > 1 :
                driver.find_element_by_xpath('//body').send_keys(Keys.HOME)
                time.sleep(1)
                print "jumlah button : "+str(len(jumlah_button))
                follows = follower_list.find_elements_by_xpath("//div[contains(text(),'+')]")
                print "jumlah button Ikuti : "+str(len(follows))
                followed = follower_list.find_elements_by_xpath("//div[contains(@class,'btn-follow') and contains(text(),'Mengikuti')]")
                print "jumlah button Mengikuti : "+str(len(followed))
                for i,x in enumerate(follows):
                    shopid = x.get_attribute('shopid')
                    time.sleep(random.randint(1, 5))
                    print("{} follow id: {} ".format(i+1,shopid))
                    while(True):
                        x.click()
                        time.sleep(1)
                        check = driver.find_element_by_xpath("//*[contains(@shopid,'{}')]".format(shopid))
                        if 'Ikuti' in check.text:
                            time.sleep(5)
                        else:
                            print("ok")
                            break
                print('end')
            else:
                print('Skip karna button kurang')
except Exception as e:
    print e
    driver.quit()
