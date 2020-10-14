from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from firebase import firebase
import time
import json

def message():
    driver = webdriver.Chrome()
    return (driver)
    
def sender(driver, d):
    #print(d)
    driver.get(d)
    a = None
    while a is None:
        print("dd")
        try:
            a = driver.find_element_by_link_text('CONTINUE TO CHAT')
        except:
            pass
    link = driver.find_element_by_link_text('CONTINUE TO CHAT')
    link.click()
    #print("c")
    a=None
    while a is None:
        try:
            a = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/header/div/a[1]')
        except:
            pass
    time.sleep(1)
    link = driver.find_element_by_link_text('use WhatsApp Web')
    link.click()
    #print("d")
    a = None
    while a is None:
        try:
            a = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/header/div[1]/div/img')
        except:
            pass
    time.sleep(2)
    link = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')
    link.click()
    #print("e")
    single, double, bt = None, None,None
    while (single is None) or (double is None) or (bt is None):
        try:
            single = "/html/body/div[2]/div/div/div[4]/div/div[3]/div/div/div[2]/div[3]/div/div/div/div[2]/div/div/span"
            double = "/html/body/div[2]/div/div/div[4]/div/div[3]/div/div/div[3]/div[21]/div/div/div/div[2]/div/div/span"
            bt = "/html/body/div[2]/div/div/div[4]/div/div[3]/div/div/div[3]/div[11]/div/div[1]/div/div/div[3]/div/div/span"
        except:
            pass
    #print("f")
    
    driver.execute_script("window.open('');")
    
    # Switch to the new window and open URL B
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://web.whatsapp.com")

#main link https://meristreet-7f81b.firebaseio.com/
link = "https://test-2f39d.firebaseio.com/"

firebase = firebase.FirebaseApplication(link, None)  

ginti = 0
#driver ka setup
driver = message()
driver.get("https://web.whatsapp.com")
while 1 > 0:
    ginti += 1
    print("karya pragati par hai")
    #firebase se data nikalne ki prakriya
    result = firebase.get('/Notifications/', '')  
    y = json.dumps(result)
    numbers = json.loads(y)
    number = numbers.values()
    dc = {}
    dc = number
    lon = []
    lom = []
    ids = list(numbers.keys())
    print(ids)
    for i in dc:
        try:
            lon.append(i["Phone NO"])
            lom.append(i["Message"])
        except:
            pass

    
    count = 0

    
    count = 0

    #task karne k liye
    for i in range(len(lon)):
        a = None
        #print("a")
        while a is None:
            try:
                a = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/header/div[1]/div/img')
            except:
                pass
        s = lom[i]
        d = "https://api.whatsapp.com/send?phone=91" + lon[i] + "&text=" + s
        sentflag = 0
        try:
            sender(driver, d)
            sentflag=1
        except:
            driver.execute_script("window.open('');")
            # Switch to the new window and open URL B
            driver.switch_to.window(driver.window_handles[1])
            driver.get("https://web.whatsapp.com")

        if lon[i] != "":
            print("sent to", lon[i])
            firebase.delete('/Notifications/', ids[i])
            data = {"message": lom[i], "phone no": lon[i]}
            
        if sentflag == 1:
            result = firebase.post('/Notifications/Sent/', data)
        else:
            result = firebase.post('/Notifications/NotSent/', data)
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        count+=1
