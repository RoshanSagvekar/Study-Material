###Pre-requisites
###pip install selenium
###pip install pandas
###pip install bs4
###pip install lxml
###pip install openpyxl
###pip install xlwt
###Download chromedrive from https://sites.google.com/a/chromium.org/chromedriver/home

from selenium import webdriver
import datetime, time
import pandas as pd
from bs4 import BeautifulSoup

##from selenium.webdriver.common.keys import Keys
##import webbrowser, sys, requests, urllib.request, datetime, os, shutil,

def login_to_linkedin(user, pwd):
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("detach", True)
    
    try:
        driver = webdriver.Chrome("chromedriver")
    except:
        print("You need to download a new version of Chromedriver")
    try:
        driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        driver.find_element_by_id('username').send_keys(user)
        driver.find_element_by_id('password').send_keys(pwd)
##        send_button = driver.find_element_by_xpath("//*[@id='app__container']/main/div/form/div[3]/button")
        send_button = driver.find_element_by_xpath("//*[@id='organic-div']/form/div[3]/button")
        send_button.click()
        driver.maximize_window()
    except ImportError:
        print("Closing Program")

def search_jobs():
    global search_term
    user = input("ENter Linkedin Username:")
    pwd = input("ENter Linkedin Password:")
    search_terms = {'hiring', 'opening', 'job', 'vacancy', 'looking', 'required', 'freshers', 'recruitment'}
##    search_term = input("What jobs do you want to search for?").lower()
##    search_terms.add(search_term)
    print("Please enter the number of the last posts you want to analyse:")
    number_of_posts = int(input())
    login_to_linkedin(user, pwd)
    print("Login Successful.")
    
    #calculate number of scrolls depending on the input
    number_of_scrolls = -(-number_of_posts // 5)  # 5 is LinkedIn's number of posts per scroll
    SCROLL_PAUSE_TIME = 5
    
    for scroll in range(number_of_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        src = driver.page_source
        soup = BeautifulSoup(src, features="lxml")

        posts = soup.findAll('div', attrs={'class':'relative ember-view'})
        for post in posts:
            a = post.find("a", href = True,
                            attrs={'class':'app-aware-link feed-shared-actor__container-link relative display-flex flex-grow-1'})
            try:
##                person = post.findAll("div", attrs={'class':'feed-shared-actor'})[0].getText()
                person = post.findAll('span', attrs={'class':'feed-shared-actor__name'})[0].getText()
                description = post.findAll("div", attrs={'class':'feed-shared-text'})[0].getText()
                link = a['href']
                for search in search_terms:
                    if search in description.lower():
                        data.append({'name':person, 'description':description, 'link':link})
                        print("Storing information.")
            except:
                pass

driver = search_term = ""
data = []
search_jobs()
file_name = search_term+"-"+datetime.datetime.now().strftime("%d-%b-%Y")+'.xls'
if len(data) > 0:
    df = pd.DataFrame(data)
    df.sort_values("name", inplace=True)
    df.drop_duplicates(subset="description", keep="first", inplace=True)
    df.to_excel(file_name)
    print("Data written to " + file_name)
driver.close()
driver.quit()
