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

  def open_chat(self, contact):
    try:
      self.search_box = self.driver.find_element_by_class_name("jN-F5")
      self.search_box.send_keys(contact)
      sleep(2)

      self.contact = self.driver.find_element_by_xpath("//span[@title = '{}']".format(contact))
      self.contact.click()
      sleep(2)
    except Exception as e:
      print("Chat could not be opened", e)

bot = Zapbot()