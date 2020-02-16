from selenium import webdriver
from time import sleep
import os

class Zapbot:
  dir_path = os.getcwd()
  chromedriver = os.path.join(dir_path, "chromedriver_linux64")
  profile = os.path.join(dir_path, "profile", "wpp")

  def __init__(self):
    self.options = webdriver.ChromeOptions()
    self.options.add_argument(r"user-data-dir={}".format(self.profile))
    self.driver = webdriver.Chrome(self.chromedriver, chrome_options = self.options)
    self.driver.get("https://web.whatsapp.com/")
    self.driver.implicitly_wait(15)

  def open_chat(self, contact_name):
    try:
      search_title = "Search or start new chat"
      search_box = self.driver.find_element_by_xpath("//input[@title='{}']".format(search_title))
      search_box.send_keys(contact_name)
      sleep(2)

      contact = self.driver.find_element_by_xpath("//span[@title='{}']".format(contact_name))
      contact.click()
      sleep(2)
    except Exception as e:
      print("Chat could not be opened", e)

  def send_message(self, message):
    try:
      #chat_box_classes = "copyable-text selectable-text"
      self.chat_box = self.driver.find_element_by_class_name("_3u328")
      self.chat_box.send_keys(message)
      sleep(1)

      send_button = self.driver.find_element_by_xpath("//button//span[@data-icon='send']")
      send_button.click()
      sleep(2)
    except Exception as e:
      print("Could not send message to contact", e)

  def send_media(self, media, caption_text = ""):
    try:
      clip_button = self.driver.find_element_by_xpath("//div[@role='button'][@title='Attach']")
      clip_button.click()
      sleep(2)

      attach_file = self.driver.find_element_by_xpath("//input[@type='file']")
      attach_file.send_keys(media)
      sleep(3)

      caption = self.driver.switch_to.active_element
      caption.send_keys(caption_text)
      sleep(3)

      send_button = self.driver.find_element_by_xpath("//span[@data-icon='send-light']")
      send_button.click()
    except Exception as e:
      print("Error sending media to contact", e)

bot = Zapbot()
bot.open_chat("contact name")
bot.send_message("a beautiful message")
bot.send_media("/path/to/file", "a great caption")
