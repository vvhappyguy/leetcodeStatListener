import json
from requests import get
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime

users_config_file = "users.json"

class User():
    def __init__(self, config):
        self.name = config["name"]
        self.tgName = config["tgName"]
        self.leetcodeLink = config["leetcodeLink"]
        self.balance = 0
    def __repr__(self) -> str:
       return f'name={self.name}, tgName={self.tgName}, leetcodeLink={self.leetcodeLink}'

class Report():
    def __init__(self) -> None:
        date = datetime.datetime.now()
        pass


def initUsers():
    users = []
    with open(users_config_file) as json_file:
        data = json.load(json_file)
        for user in data["users"]:
            users.append(User(user))
    return users

def getPage(url):
    URL = url
    page = get(URL)
    print(page.text)
    soup = BeautifulSoup(page.content, "html.parser")
    allNews = soup.findAll()
    with open("res.txt", "w") as o:
        o.write(str(page.text))
    #print(allNews)


if __name__ == "__main__":
    users = initUsers()
    driver = webdriver.Chrome("/mnt/d/Downloads/chromedriver_win32/chromedriver.exe")
    for user in users:
        driver.get(user.leetcodeLink)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        res = str(soup.find_all("div", {"class": 'text-[24px] font-medium text-label-1 dark:text-dark-label-1'})[0])
        print(f'Name={user.name} Solved={res[res.find(">")+1:res.find("</div>")]}')
    driver.close()