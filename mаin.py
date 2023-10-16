import json
import time
import random
import os

import undetected_chromedriver as uc

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = input("Post URL: ")
count_up = int(input("Upvotes amount: ")) 
index = 0 # Counts the upvotes made.


def upvote(files_c, proxy):
    print("proxy : " + proxy)
    
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_argument(f"--proxy-server={proxy}")
    options.headless = not False

    driver = uc.Chrome(options=options)
    
        # Reads cookies.
    with open(files_c, "r") as file:
        cookies = json.load(file)

    driver.get("https://reddit.com")
        # Sets up the cookies.
    for cookie in cookies:
        name = cookie["name"]
        value = cookie["value"]
        driver.add_cookie({"name" : name, "value" : value})

    driver.get(url)
    wait = WebDriverWait(driver, 15)

    # Doing the clicking.
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div/div/div/header/div/div[2]/button")))
        elements = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div/div/div/header/div/div[2]/button")
        # elements.click()
            # Just in case the element is blocked visually, it clicks it programmatically.
        driver.execute_script("arguments[0].click();", elements)
    except:
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[1]/div/div[1]/div/button[1]")))
        
        upvote = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[1]/div/div[1]/div/button[1]")
        # upvote.click()
        driver.execute_script("arguments[0].click();", upvote)
        time.sleep(5)
        driver.quit()


folder_path = "cookie"
folder_path_proxy1 = "proxy"
files_p = os.listdir(folder_path_proxy1)
files_c = os.listdir(folder_path)
proxy_arr = []
for file_p in files_p:
        file_path_proxy = os.path.join(folder_path_proxy1, file_p)
        with open(file_path_proxy, "r") as file:
            proxy = file.readlines()
            proxy_arr.extend(proxy)        


for file_c in files_c:
    file_path = os.path.join(folder_path, file_c) # Getting full path.
    proxy_df = random.randint(0,len(proxy_arr) - 1)
    upvote(file_path, proxy_arr[proxy_df])
    index += 1 
    # If the targeted amount of upvotes is made break.
    if index == count_up:
        print("Done")
        break




