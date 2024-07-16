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
LOGIN_USERNAME = 'tanie_loty_'
LOGIN_PASSWORD = 'Slawny08!'
INSTAGRAM_NICKNAME = 'ewelka22b'


def scroll_down(driver):
    actions = ActionChains(driver)
    for _ in range(90):
        actions.send_keys(Keys.DOWN).perform()


def give_comment(driver, username, comment):
    driver.get(f"https://www.instagram.com/{username}")
    time.sleep(10)

    posts = driver.find_elements(By.XPATH,
                                 '//*[contains(@class, "x1lliihq") and contains(@class, "x1n2onr6") and contains(@class, "xh8yej3") and contains(@class, "x4gyw5p") and contains(@class, "xfllauq") and contains(@class, "xo2y696") and contains(@class, "x11i5rnm") and contains(@class, "x2pgyrj")]')
    print(len(posts))
    if posts:
        first_post = posts[0]
        first_post.click()
        time.sleep(10)
        comment_input = driver.find_element(By.XPATH, '//textarea[@aria-label="Add a comment…"]')

        time.sleep(1)
        comment_input.click()
        time.sleep(1)
        comment_input_2 = driver.find_element(By.XPATH, '//textarea[@aria-label="Add a comment…"]')
        time.sleep(1)
        comment_input_2.send_keys(comment)
        time.sleep(2)
        comment_input_2.send_keys(Keys.ENTER)
        time.sleep(5)


def like_photos(driver, username):
    driver.get(f"https://www.instagram.com/{username}")
    time.sleep(10)

    posts = driver.find_elements(By.XPATH,
                                 '//*[contains(@class, "x1lliihq") and contains(@class, "x1n2onr6") and contains(@class, "xh8yej3") and contains(@class, "x4gyw5p") and contains(@class, "xfllauq") and contains(@class, "xo2y696") and contains(@class, "x11i5rnm") and contains(@class, "x2pgyrj")]')
    print(len(posts))
    if posts:
        first_post = posts[0]
        first_post.click()

        time.sleep(3)
        element = driver.switch_to.active_element
        time.sleep(1)
        # Kliknij klawisz "l"
        element.send_keys("l")
        time.sleep(1)
        next_photo_btn = driver.find_element(By.XPATH, '//div[@class="_aaqg _aaqh"]/button')
        time.sleep(1)
        next_photo_btn.click()
        time.sleep(300)



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

        usernames = ['milenaplewa5', 'hotteamama', 'oliwkalaa']

        for user in usernames:
            # give_comment(driver, user, 'Podoba mi sie!')
            # time.sleep(5)
            like_photos(driver, user)
            time.sleep(5)

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
