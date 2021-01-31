파이썬을 기반으로 한 컴퓨터 사용시간 프로그램입니다.   
GUI(tkinter)를 이용하여 화면을 구성하였으며,   
datetime 모듈을 이용하여 시간을 측정하였습니다.   
사실 효율적인 방법을 이용한 프로그램은 아니지만,   
제가 할 수 있는 방법을 고안하여 프로그램을 구성해보았습니다.   

   ***
### ※ 주의 사항   
시간을 측정해주는 프로그램을 시작프로그램으로 이용하기 위해   
checkpctime.py 파일은 절대경로를 이용하여 코드를 작성하였고   
프로그램을 정상적으로 실행해보고 싶으시다면 파일을 다운로드 받은 후,   
__C:\코딩\Pc_time_check__ 와 같이 디렉토리를 설정해주셔야 합니다.
(GUI 파일은 상대경로 설정되어있지만, checkpctime 파일이 절대경로로 되어있습니다.)      
   
또한, exe 파일 실행시 사진 및 음악파일의 경로를 알맞게 위치시켜야 파일이 실행됩니다. (파일 위치를 변경할 때 주의해주세요)   
   ***

# Pc_time_check - 컴퓨터 사용시간 프로그램
    컴퓨터 사용시간을 측정하고 기록해주는 프로그램입니다.   
    system 함수 등을 이용하여 시간을 받아오는 방법이 더 효율적이었겠지만,   
    아직까지는 저에게 쉽지 않게 여겨져 새로운 방식으로 도전해보았습니다.   
    datetime 모듈을 이용하여 컴퓨터가 켜져있는 동안 시간이 업데이트 되는 방식으로   
    시작프로그램에 수동으로 exe 파일을 집어넣어줘서 사용할 수 있습니다.   
***   
## 사용한 모듈 & 라이브러리
    1. tkinter   
    > GUI를 구성하기 위해 사용한 모듈입니다.
    2. threading
    > 여러 이벤트와 동작을 동시에 처리하기 위해 사용한 모듈입니다.
    3. sqlite3
    > 점수를 저장하기 위해 사용한 Database 모듈입니다.
    4. pyglet
    > GUI에 폰트를 사용하기 위해 폰트를 추가해주는 모듈입니다.
    5. pillow
    > 이미지를 처리하기 위해 사용한 라이브러리 입니다.
    6. os
    > 사진 파일의 위치를 쉽게 지정해주기 위해 사용한 모듈입니다.
    7. pyinstaller
    > python 파일을 exe 파일로 변환하기 위해서 사용한 라이브러리입니다.
***
##  기능
### Time_Check_Program - 사용시간 측정 프로그램
    컴퓨터 사용시간을 받아올 수 있을만한 모듈을 알지 못하였기 때문에,   
    시작프로그램에 시간 측정 프로그램을 넣어 컴퓨터가 부팅되면 시간  측정을 시작하고   
    약 1초마다 사용시간을 업데이트하며 컴퓨터가 종료될 때까지 사용시간을 측정합니다.   
    이러한 데이터들을 Database에 저장해줍니다.   
### Database (sqlite3 이용)
    Time_Check_Program이 실행되는 동안, 시작 시간과 종료시간, 이용시간을   
    계속해서 업데이트하여 Pc_time.db에 저장해줍니다.
### GUI(tkinter) - 데이터 출력 프로그램
    Time_Check_Program으로 Database에 저장된 정보들을 가져와   
    GUI로 화면에 출력을 해줍니다.   
    기본적으로 메인 화면에서 현재 컴퓨터 사용시간과 이번주 컴퓨터 사용횟수가 나오며,   
    사용시간 보기 버튼을 클릭하여 시작 날짜와 시간, 종료 날짜와 시간,   
    이용 시간 등을 원하는 방식으로 정렬하여 최대 45개까지 볼 수 있습니다.   
***
## 코멘트
    PC_time_check 프로젝트를 진행할 때에는 비교적 GUI 다루는 것이   
    익숙해져서 짧은 기간에 단순한 형태로 작업하여 완성을 해보았습니다.   
    Automatic_guest_book (전자 방문록) 프로젝트 때 작업했던 것을 이용하여   
    디자인 시간을 최소화하여 작업하였지만, 나름 깔끔하게 프로젝트가   
    마무리되어서 좋았습니다.   
    수동으로 시작프로그램에 시간 측정 프로그램을 넣어줘야 한다는 점과   
    시간 측정 방식이 조금은 비효율적이라는 것이 아쉽지만,   
    나름 괜찮은 방식과 아이디어로 프로젝트를 완료한 것 같습니다.
***
## 실행사진