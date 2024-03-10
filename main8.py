import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import getpass
from selenium.webdriver.common.action_chains import ActionChains
import re
from main6 import apiGemini

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

Email = input("Email: ")
passwordinput = getpass.getpass("Enter your password: ")
tag = input("tag: ")

driver.get('https://pantip.com')
time.sleep(5)
login = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[1]/div/ul[2]/a[4]').click()
time.sleep(5)
email = driver.find_element(By.XPATH,'//*[@id="member_email"]')
time.sleep(1)
email.send_keys(Email)
password = driver.find_element(By.XPATH,'//*[@id="member_password"]')
password.send_keys(passwordinput)
# Send the "Enter" key to submit the form
password.send_keys(Keys.ENTER)
time.sleep(2)
post_count = 12
post_success = 0
# driver.get(f'https://pantip.com/tag/{tag}')
driver.get(f'https://pantip.com/tag/{tag}')
time.sleep(2)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
time.sleep(2)

while True:
    try:
        print('โพสที่ 12 เป็นทต้นไป ตอนนี้',post_count)
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[0]) 
        time.sleep(1)
        if post_count % 8 == 0:
            driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
            time.sleep(2)
        post = driver.find_element(By.XPATH,f'//*[@id="pt-topic-left"]/div[2]/ul/li[{int(post_count-2)}]/div[1]/h2/a')
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -document.body.scrollHeight);")
        time.sleep(2)
        driver.execute_script("arguments[0].scrollIntoView();", post)
        time.sleep(2)
        postselect = driver.find_element(By.XPATH,f'//*[@id="pt-topic-left"]/div[2]/ul/li[{int(post_count)}]/div[1]/h2/a').click()
        time.sleep(4)
        driver.switch_to.window(driver.window_handles[1]) 
        current_url = driver.current_url
        match = re.search(r'\d+', current_url)
        if match:
            topic_id = match.group()
            # print("Extracted Topic ID:", topic_id)
            toppic = driver.find_element(By.XPATH,f'//*[@id="topic-{topic_id}"]/div/div[2]/h2').text
            detail = driver.find_element(By.XPATH,f'//*[@id="topic-{topic_id}"]/div/div[4]/div[1]/div').text
            comment = apiGemini(f'{toppic} {detail} {tag} ตอบสั้นๆ 3 บรรทัด')
            # print(comment)
            commend = driver.find_element(By.XPATH,'//*[@id="detail"]')
            commend.send_keys({comment})
            time.sleep(5)
            submitcommended = driver.find_element(By.XPATH,'//*[@id="btn_comment"]').click()
            post_success += 1
            time.sleep(1)
            print("Successfully extracted", post_success)
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1]) 
            comment_url = driver.current_url
            print("Current URL:", comment_url)
            time.sleep(2)
        else:
            print("No numeric part found in the URL.")
        time.sleep(1)
        driver.close()
    except:
        print('ไม่เจอ element not found')
        driver.close()
        post_count += 1
        continue
    post_count += 1