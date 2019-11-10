#airline scheduling list

#항공 스케쥴링은 크롤링으로서 테스트로 대한항공의 운항 스케쥴 정보를 이용한다
#서울 - 부산
#서울 - 제주
#부산 - 제주
#부산 - 서울
#제주 - 서울
url = "https://www.koreanair.com/"

import requests

data = requests.get(url)

#if data.status_code != requests.codes.ok:
#    print("항공운항스케쥴 정보 접속 실패")
#    exit()
#else:
#    print("항공운힝스케쥴 정보 접속 성공")
#    exit()

from bs4 import BeautifulSoup
html = BeautifulSoup(data.text, "html.parser")


#운항스케쥴 및 가격 가져오기
tags = html.select(".keForm")

# 운항 스케쥴을 사이트에서 스케쥴이 끝날때까지 모두 가져오기
for tag in tags:
    week = tag.select_one(".week").text #요일
    l_price = tag.select_one(".lowest").text #최저가격
    airline_info = tag.select_one(".instead-tit").text #타이틀 - 항공편정보 , 특별운임, 정상운임
    airpline_type = tag.select_one(".airplane").text #항공기 기종
    airline_schedule = tag.select_one(".schedule-airplane").text #출발시간, 도착시간
    d_price = tag.select_one(".discount-fare").text #특별운임
    o_price = tag.select_one(".original-cost").text #정상운임
    
    print(l_price, airline_info, airline_schedule, d_price, o_price)
    #print(title)


