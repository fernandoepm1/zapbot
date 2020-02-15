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

  def send_message(self, message):
    try:
      self.chat_box = self.driver.find_elements_by_class_name("_2S1VP")
      self.chat_box.send_keys(message)
      sleep(1)

      self.send_button = self.driver.find_element_by_class_name("_35EW6")
      self.send_button.click()
      sleep(2)
    except Exception as e:
      print("Could not send message to contact", e)

  def send_media(self, media):
    try:
      self.clip_button = self.driver.find_element_by_css_selector("span[data-icon='clip']").click()
      attach = self.driver.find_element_by_css_selector("input[type='file'")
      attach.send_keys(media)
      sleep(3)

      send = self.driver.find_element_by_xpath("//div[contains(@class, 'yavlE')]")
      self.click()
    except Exception as e:
      print("Error sending media to contact", e)

bot = Zapbot()
bot.open_chat("contact name")
bot.send_message("a beautiful message")
bot.send_media("/path/to/file")