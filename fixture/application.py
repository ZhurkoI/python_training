from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application():

    def __init__(self):
        # creating the fixture
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        # destroying the fixture
        self.driver.quit()