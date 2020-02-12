from selenium import webdriver
from time import sleep
import os

class Zapbot:
  dir_path = os.getcwd()
  chromedriver = os.path.join(dir_path, "chromedriver")
  profile = os.path.join(dir_path, "profile", "wpp")

  def __init__(self):
    self.options = webdriver.ChromeOptions()
    self.options.add_argument(r"user-data-dir={}".format(self.profile))
    self.driver = webdriver.Chrome(self.chromedriver, chrome_options = self.options)
    self.driver.get("https://web.whatsapp.com/")
    self.driver.implicitly_wait(15)

bot = Zapbot()