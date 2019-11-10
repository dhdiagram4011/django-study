## 2019.11.10
## Deveopver : dohyoung.kim
## Email : dhdiagram@gmail.com
## Cellular_Phone : 010-2176-4011
## Application_Name : Airline-Ticketing-System


## Application Information

## External Web Service URL
http://rev.dhdiagram.net
http://rev.dhdiagram.net/admin
localhost:8000 -> rev.dhdiagram.net

0. admin Control Page
http://localhost:8000/admin

1. Reservation_Page (구간별 스케쥴 조회 페이지 - 고객조회페이지)
http://localhost:8000/reservation/reservationStart/


2. 구간별 운항 스케쥴 페이지
http://localhost:8000/reservation_start/cargo/ -> 전체구간 조회
http://localhost:8000/reservation_start/gmp2cju/ -> 김포 - 제주구간
http://localhost:8000/reservation_start/gmp2pus/ -> 김포 - 부산구간
http://localhost:8000/reservation_start/cju2pus/ -> 제주 - 부산구간
http://localhost:8000/reservation_start/cju2gmp/ -> 제주 - 김포구간
http://localhost:8000/reservation_start/pus2cju/ -> 부산 - 제주구간
http://localhost:8000/reservation_start/pus2gmp/ -> 부산 - 김포구간

3. 회원가입페이지
http://localhost:8000/accounts/register/


4. 회원가입 후 로그인페이지
http://localhost:8000/accounts/login/


5. 구간 스케쥴 조회 및 예약티켓 pdf 파일 다운로드 페이지
http://localhost:8000/ticket/boarding_ticket_download/
http://localhost:8000/ticket/b_gmp2cju/ -> 김포 - 제주구간
http://localhost:8000/ticket/b_gmp2pus/ -> 김포 - 부산구간
http://localhost:8000/ticket/b_cju2pus/ -> 제주 - 부산구간
http://localhost:8000/ticket/b_cju2gmp/ -> 제주 - 김포구간
http://localhost:8000/ticket/b_pus2cju/ -> 부산 - 제주구간
http://localhost:8000/ticket/b_pus2gmp/ -> 부산 - 김포구간





# django-study
