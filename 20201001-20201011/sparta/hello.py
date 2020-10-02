# 2020.10.01
print('hello world')

# 변수, 자료형, 조건문, 반복문, 기타 라이브러리

# 회사마다 코드 컨벤션이 다르다
# firstName ; 카멜케이스
# last_Name ; 스네이크 케이스

# import dload
#
# dload.save("https://cphoto.asiae.co.kr/listimglink/6/2017110713394315556_1510029583.jpg")


# from selenium import webdriver
# driver = webdriver.Chrome('./chromedriver')
#
# driver.get("http://www.naver.com")

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload

driver = webdriver.Chrome('./chromedriver') # 웹드라이버 파일의 경로
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%9C%A0")
time.sleep(5) # 5초 동안 페이지 로딩 기다리기

req = driver.page_source
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(req, 'html.parser')

###################################
# 이제 여기에 코딩을 하면 됩니다!

# print(soup)

# 원하는 elemnt 우클릭 > 검사 클릭하고, 해당 태그에 대해 " copy select "
# imgList > div:nth-child(2) > a > img

thumbnails = soup.select("#imgList > div > a > img")

i = 1
for thumbnail in thumbnails:
    src = thumbnail["src"]
    dload.save(src, f'img/{i}.jpg')
    i += 1

###################################

driver.quit() # 끝나면 브라우저 닫아주기



## 1일차 숙제
## 아이유가 아닌 다른 연예인의 이미지 크롤링하여 저장