import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import copy
import pyperclip
import pyautogui

# 크롬에서 토스를 연다

def kakao(name,phone,url):
    # 친구 추가버튼 좌표 : Point(x=1885, y=64)
    # 친구이름 좌표 : Point(x=1313, y=421)
    # 친구 붙여넣기 : Point(x=1565, y=515)
    # 전화번호 좌표 : Point(x=1371, y=471)
    # 전화 붙여넣기 : Point(x=1540, y=584)
    # 친구추가 좌표 : Point(x=1558, y=740)


    # pyautogui.moveTo(1885, 1885, duration=0.5)   # 200, 200 위치로 0.5초간 이동

    pyperclip.copy(phone)         # pyperclip.copy(): 클립보드에 텍스트를 복사합니다.

    pyautogui.click(1885, 64)
    time.sleep(3 * random.random())

    pyautogui.rightClick(1313, 421)
    # pyautogui.press(name)

    # 붙여넣기
    time.sleep(1)
    pyautogui.click(1565, 515)



    time.sleep(1)
    pyperclip.copy(phone)         # pyperclip.copy(): 클립보드에 텍스트를 복사합니다.

    # 전화번호 클릭, 붙여넣기
    pyautogui.rightClick(1371, 471)
    time.sleep(1)
    pyautogui.click(1540, 584)


    # 친구 추가 버튼
    time.sleep(1)
    pyautogui.click(1558,740)

    # 만약 친구가 없었다면 닫기버튼 ; Point(x=1613, y=240)

    time.sleep(1)
    pyautogui.click(1613,240)
    
    # 통합 검색버튼 좌표 : Point(x=1831, y=55)
    # 검색 창 좌표 : Point(x=1164, y=126)
    # 검색 창 붙여넣기 좌표 : Point(x=1452, y=243)
    # 맨 위의 친구이름 좌표 : Point(x=1185, y=222)

    # 채팅창 위치 좌표 : Point(x=1243, y=752)
    # 채팅창 붙여넣기 좌표 : Point(x=1281, y=872)
    # 채팅창 전송버튼 좌표 : Point(x=1700, y=751)
    # 채팅창 닫기 버튼 좌표 : Point(x=1713, y=211)
    # 친구창으로 이동 좌표 : Point(x=1872, y=129)


    pyperclip.copy(phone)         # pyperclip.copy(): 클립보드에 텍스트를 복사합니다.

    pyautogui.click(1831, 55)
    time.sleep(1)

    pyautogui.rightClick(1164, 126)
    time.sleep(1)

    pyautogui.click(1452, 243)

    time.sleep(1)

    pyautogui.doubleClick(1185, 222)

    time.sleep(1)
    
    
    
    # in 채팅방
#     pyperclip.copy(f'안녕하세요 {li[2]} 님 {li[1]} 구매해주셔서 감사합니다. \n {url}' )
    pyperclip.copy(f'안녕하세요. {name}님, {url}')
    pyautogui.rightClick(1243, 752)
    time.sleep(1)
    pyautogui.click(1281, 872)
    time.sleep(1)
    pyautogui.click(1700,751)
    
     # 채팅방 닫기
    time.sleep(1)
    pyautogui.click(1713,211)
    
    # 친구창으로 이동
    time.sleep(1)
    pyautogui.click(1872,129)

# 메뉴파인딩 함수
# Todo : 파일 입출력으로 변경

def find_menu(str):
    ans = 'https://www.google.com/'
    lines = []
    if '레다 크라임씬 EP.01' in str:
        with open('crime.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
            lines = file.readlines()
            ans = lines.pop(0)
        
        with open('crime.txt', 'w') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
            file.writelines(lines)

    
    elif '이야기를 전해드릴게요' in str:
        with open('story.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
            lines = file.readlines()
            ans = lines.pop(0)

        with open('story.txt', 'w') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
            file.writelines(lines)
    return ans


driver = webdriver.Chrome() # Driver가 있는 path를 넣어 줄 수 있음

time.sleep(2)

driver.get("https://app.tosspayments.com/")

time.sleep(60)
print('토스 사이트 들어가짐')

elems = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/section/div[3]/div[3]/table/tbody')

n = 0
li = []
l = []

for i in elems.find_elements_by_class_name('text--left'):
    if n % 10 == 0:
#         print("날짜 : ",i.text)
        l.append(i.text)
    elif n % 10 == 2: # 결제 완료 여부
        l.append(i.text)
    elif n % 10 == 3:
#         print("컨텐츠 : ",i.text)
        l.append(i.text)
    elif n % 10 == 5:
#         print("이름 : ",i.text)
        l.append(i.text)
    elif n % 10 == 7:
#         print("번호 : ",i.text)
        l.append(i.text)
        li.append(l)
        l = []
    n += 1

print('일단 한번 훑음')
# 본격 진행 전에 시간 벌어주기
# - 로그인하고 이것저것 누르고 확인버튼 누르기 



# 본격 진행

for _ in range(1): # 바뀔 예정

    driver.refresh()
    time.sleep(5)

    elems2 = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/section/div[3]/div[3]/table/tbody')

    n = 0
    li2 = []
    l2 = []

    for i in elems2.find_elements_by_class_name('text--left'):
            
        if n % 10 == 0:
#             print("날짜 : ",i.text)
            l2.append(i.text)
        elif n % 10 == 2:
            l2.append(i.text) # 결제완료 여부
        elif n % 10 == 3:
#             print("컨텐츠 : ",i.text)
            l2.append(i.text)
        elif n % 10 == 5:
#             print("이름 : ",i.text)
            l2.append(i.text)
        elif n % 10 == 7:
#             print("번호 : ",i.text)
            l2.append(i.text)
            li2.append(l2.copy())
            
#             if l2 not in li:

    
            if l2 in li and l2[1] == '결제완료':
                # 이 고객은 새로운 사람
                # 이 사람꺼 보내준다
                
                # 메뉴 확인해서 링크 변수에 넣기
                url = find_menu(l2[2])
                kakao(l2[3],"01025895645",url)
                
                # 카톡 친추하기
                
                # 카톡 보내기 + url로

            l2 = []    
            
        n += 1

    li = copy.deepcopy(li2)
    li2 = []
    
    # 나중에 바꿀 것
    time.sleep(1)

# 마지막에 li2 는 li로