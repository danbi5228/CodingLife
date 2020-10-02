# 2020.10.01
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload

driver = webdriver.Chrome('./chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EB%B0%95%ED%9A%A8%EC%8B%A0+%EC%BD%98%EC%84%9C%ED%8A%B8") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

###################################
# 이제 여기에 코딩을 하면 됩니다!

thumbnails = soup.select("#imgList > div > a > img")

i = 1
for thumbnail in thumbnails:
    src = thumbnail["src"]
    dload.save(src, f'img_homework/박효신_{i}.jpg')
    i += 1

###################################

driver.quit() # 끝나면 닫아주기