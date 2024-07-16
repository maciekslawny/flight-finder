from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError

from flightfinder.services import CheapestTicketPlanService, TicketPlanFinder
from instagramservice.models import InstagramPost, InstagramStory
from instagramservice.cities_services import AlicanteService

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
LOGIN_USERNAME = 'maciej.slawny'
LOGIN_PASSWORD = 'Slawnyinstagram908!'
INSTAGRAM_NICKNAME = 'ewelka22b'


def scroll_down(driver):
    actions = ActionChains(driver)
    for _ in range(90):
        actions.send_keys(Keys.DOWN).perform()




class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        # Definiujemy argumenty, które możemy przekazać do komendy
        parser.add_argument('departure_city', nargs='?', type=str, default=None)
        parser.add_argument('arrival_city', nargs='?', type=str, default=None)

    def handle(self, *args, **options):
        # #Publikuj
        # post = InstagramPost.objects.get(id=1)
        # post.generate_image()
        # post.publish()

        options = Options()
        options.add_argument("−−incognito")
        chromeOptions = Options()
        chromeOptions.headless = False

        s = Service("/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=s, options=chromeOptions)

        driver.get("https://www.instagram.com/")
        time.sleep(2)
        cookie_btn = driver.find_element(By.XPATH, '//button[@class="_a9-- _ap36 _a9_1"]')
        time.sleep(1)
        cookie_btn.click()
        time.sleep(1)
        username_input = driver.find_element(By.XPATH, '//*[@name="username"]')
        username_input.send_keys(LOGIN_USERNAME)
        time.sleep(1)
        password_input = driver.find_element(By.XPATH, '//*[@name="password"]')
        password_input.send_keys(LOGIN_PASSWORD)
        time.sleep(3)
        login_btn = driver.find_element(By.XPATH, '//*[@type="submit"]')
        login_btn.click()
        time.sleep(10)

        driver.get(f"https://www.instagram.com/p/C7w0DQ8InPb/")
        time.sleep(5)
        element = driver.find_element(By.XPATH,
                                      '//span[contains(@class, "x193iq5w") and contains(@class, "xeuugli") and contains(@class, "x1fj9vlw") and contains(@class, "x13faqbe") and contains(@class, "x1vvkbs") and contains(@class, "xt0psk2") and contains(@class, "x1i0vuye") and contains(@class, "xvs91rp") and contains(@class, "x1s688f") and contains(@class, "x5n08af") and contains(@class, "x10wh9bi") and contains(@class, "x1wdrske") and contains(@class, "x8viiok") and contains(@class, "x18hxmgj") and text()="others"]')
        time.sleep(3)
        element.click()
        time.sleep(5)

        time.sleep(2)
        driver.execute_script("window.scrollBy(0, 500);")

        time.sleep(1)
        # for _ in range(100):
        #     scroll_down(driver)



        # followers_btn = driver.find_element(By.XPATH, f'//*[@href="/{INSTAGRAM_NICKNAME}/following/"]')
        # followers_btn.click()
        # time.sleep(5)
        # print('przed scroll')
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # print('po scroll')
        # followers_list = driver.find_element(By.XPATH, '//*[@class="_aano"]')
        # followers_list.click()
        # time.sleep(1)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # print('click')
        # last_amount = 1
        # repeat = 0
        # for _ in range(100):
        #     print(len(followers_list.find_elements(By.XPATH, '//img')))
        #     print('last_amount', last_amount)
        #     print(len(followers_list.find_elements(By.XPATH, '//img')))
        #
        #     scroll_down(driver)
        #     if len(followers_list.find_elements(By.XPATH, '//img')) == last_amount:
        #         last_amount = len(followers_list.find_elements(By.XPATH, '//img'))
        #         repeat += 1
        #     else:
        #         repeat = 0
        #         last_amount = len(followers_list.find_elements(By.XPATH, '//img'))
        #     if repeat > 3:
        #         print('koniec')
        #         break
        #     time.sleep(1)
        # followers_list = followers_list.find_elements(By.XPATH, '//*[@class="xt0psk2"]')
        # print(len(followers_list))
        # for item in followers_list:
        #     try:
        #         print(item.text)
        #     except:
        #         print('bload')

        time.sleep(100)
