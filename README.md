## 2019.11.10<br>
## Deveopver : dohyoung.kim<br>
## Email : dhdiagram@gmail.com<br>
## Cellular_Phone : 010-2176-4011<br>
## Application_Name : Airline-Ticketing-System<br>
<br>
<br>
## Application Information<br>
<br>
## External Web Service URL<br>
http://rev.dhdiagram.net<br>
http://rev.dhdiagram.net/admin<br>
localhost:8000 -> rev.dhdiagram.net<br>
<br>
0. admin Control Page<br>
http://localhost:8000/admin<br>
<br>
1. Reservation_Page (구간별 스케쥴 조회 페이지 - 고객조회페이지)<br>
http://localhost:8000/reservation/reservationStart/<br>
<br>
<br>
2. 구간별 운항 스케쥴 페이지<br>
http://localhost:8000/reservation_start/cargo/ -> 전체구간 조회<br>
http://localhost:8000/reservation_start/gmp2cju/ -> 김포 - 제주구간<br>
http://localhost:8000/reservation_start/gmp2pus/ -> 김포 - 부산구간<br>
http://localhost:8000/reservation_start/cju2pus/ -> 제주 - 부산구간<br>
http://localhost:8000/reservation_start/cju2gmp/ -> 제주 - 김포구간<br>
http://localhost:8000/reservation_start/pus2cju/ -> 부산 - 제주구간<br>
http://localhost:8000/reservation_start/pus2gmp/ -> 부산 - 김포구간<br>
<br>
3. 회원가입페이지<br>
http://localhost:8000/accounts/register/<br>
<br>
<br>
4. 회원가입 후 로그인페이지<br>
http://localhost:8000/accounts/login/<br>
<br>
<br>
5. 구간 스케쥴 조회 및 예약티켓 pdf 파일 다운로드 페이지<br>
http://localhost:8000/ticket/boarding_ticket_download/<br>
http://localhost:8000/ticket/b_gmp2cju/ -> 김포 - 제주구간<br>
http://localhost:8000/ticket/b_gmp2pus/ -> 김포 - 부산구간<br>
http://localhost:8000/ticket/b_cju2pus/ -> 제주 - 부산구간<br>
http://localhost:8000/ticket/b_cju2gmp/ -> 제주 - 김포구간<br>
http://localhost:8000/ticket/b_pus2cju/ -> 부산 - 제주구간<br>
http://localhost:8000/ticket/b_pus2gmp/ -> 부산 - 김포구간<br>
<br>
<br>
# django-study
