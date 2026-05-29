from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup


class LinkFetcher:
    

    def __init__(self,url):
        self.url = url

    def fetch(self):
        links = []
        driver = webdriver.Chrome()

        driver.get(str(self.url))


        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # links.append(driver.find_element(By.TAG_NAME,"a").text)
        # print("Scrolling" + driver.find_element(By.TAG_NAME,"a").text)
        time.sleep(2)

        html = driver.page_source

        soup = BeautifulSoup(
            html,
            "lxml"
        )

        soups = soup.find_all("a",class_="uni-link")

        for i, soup in enumerate(soups):
            links.insert(i,":https://www.topuniversities.com"+soup["href"])

        
        

        return links
        
        driver.quit()

        
