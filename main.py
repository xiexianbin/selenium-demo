# coding: UTF-8

import requests
import time

from bs4 import BeautifulSoup
from selenium import webdriver


def download_mp3(index):
    url = 'http://m.ysxs8.com/yousheng/7550_{}.html'.format(index)

    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        executable_path="./chromedriver",
        options=options)
    try:
        driver.get(url)
        iframe = driver.find_elements_by_tag_name('iframe')[0]
        driver.switch_to.frame(iframe)
        iframe = driver.find_elements_by_tag_name('iframe')[0]
        driver.switch_to.frame(iframe)
        # soup = BeautifulSoup(driver.page_source, 'html.parser')
        # print(soup.body)
        # print("--\n")

        audio = driver.find_element_by_tag_name("audio")
        audio_url = audio.get_attribute('src')
        print("audio_url: {} {}".format(index, audio_url))

        r = requests.get(audio_url)
        with open("downloads/{}.mp3".format(index), 'wb') as f:
            f.write(r.content)

        time.sleep(2)
    finally:
        driver.close()


if __name__ == '__main__':
    start = 500
    for i in range(2):
        download_mp3(start+i)
