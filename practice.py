# print("풍선이라고")
# print("나비")
# print("ㅋㅋㅋㅋㅋ")
# print("오호" * 8)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not (5 < 0))


# animal = "고양이"
# name = "준수"
# age = 20
# hobby = "돈"
# is_adult = age >= 3


# print("우리집 " + animal + "의  이름은" + name + " 이에요")

# hobby = "줄넘기"
# print("그뤠잇은", str(age), " 살이구요 로즈를 너무", hobby, " 합니다.")
# print("그뤠잇은 어른이에요." + str(is_adult))

# # 신세계구먼 파이턴
# """ 이렇게 하면
# 여러문장이 comments"""


# station = "신도림"

# print(station * 2 + "행 열차가 들어오고 있슈")

# print(3 * 3 != 9)
# print(not (1 != 3))
# print((3 > 0) and (2 != 5))
# print((3 > 0) & (1 < 3))

# print((3 > 0) | (0 < 5))

# print(2 * 3 * 2)

# calculation = 2 * 3 * 2 * 3
# print(calculation)
# calculation = calculation * 2
# print(calculation)
# calculation *= 20
# print(calculation)

# print(abs(-5))
# print(pow(4, 2))  # 4 ^2
# print(max(5, 12, 20, 4))
# print(min(4, 1, 2, 4, 0, 9))
# print(round(3.1))
# print(round(8.8))


# from math import *  # must put this import, otherwise there is no calculation

# print(floor(4.99))
# print(ceil(7.8))
# print(sqrt(16))


# from random import *

# print(random())  # 랜덤함수 0.0 이상 1.0미만의 임의값생성
# print(random() * 10)
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10 + 1))  # 1-10 이하의 임의의 값


# print(int(random() * 45 + 1))  # 1-45 이하의 임의의 값
# # 위의 값과 같은 밑의 값
# print(randrange(1, 46))  # 1-46 미만의 임의의 값 생성

# print(randint(1, 45))  # 1-45 이하의 이의의 값


# print("오프라인 스터디 모임 날짜는 매월" + str(randrange(3, 28)) + "로 선정되었쮸")
# print("오프라인 스터디 모임 날짜는 매월" + str(randrange(3, 28)) + "로 선정되었쮸")
# # 내가 만든 값


# # 선생님이 만든 값

# from random import *

# date = randint(4, 28)
# print("오프라인 모임 날짜는 매월 " + str(date) + "일로 선정됐쮸")


# sentence = "나는 소녀입니다"
# print(sentence)
# sentence2 = "파이떤은 쉽지"
# print(sentence2)
# sentence3 = """
# 나는 소녀이고,
# 파이떤은 쉽고
# 나는 6시간을 공부해야하고
# 그래서 인터뷰를 준비해야하고
# 나는 소프트웨어 엔지니어가 된다
# 실리콘밸리 입성할꺼야!
# """
# print(sentence3)


# jumin = "830727-206512"
# print("성별 : " + jumin[7])
# print("연도 : " + jumin[0:2])  # 0부터 2직전까지
# print("생년월일 : " + jumin[2:6])  # 2부터 6직전까지
# print("전부싹다 : " + jumin[0:6]) #0부터 6직전까지
# print("전부싹다 : " + jumin[:6]) #0부터 6직전까지 114번과 동일하나, 다른방법
# print("전부싹다 : " + jumin[7:])
# print(" 뒤에서부터 가지고 오기 : " + jumin[-7:])


# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(
#     python[0].isupper()
# )  # python's sentence "Python " <---- Capital letter P, so it is true, boolean sentence

# print(len(python))
# print(python.replace("Python", "Java Script"))
# print(python.replace("Amazing", "Wonderful"))


# index = python.index("n")
# print(index)  # 1번째 n
# index = python.index("n", index + 1)
# print(index)  # 1번쨰 의 값 플러스 다음 n


# print(python.find("o"))

# print(python.find("Java"))  # find 기능에서는 입력값이 존재하지 않으면 negative로 표현한다.
# # print(python.index("Java"))  # index를 통해서는 ValueError: substring not found,찾을 수없다고 표현한다. 또한 이 이후의 프린터값에 대하여 추가 실행하지 않는다.
# # print("hi")  #141번과 함께 보시오


# print(python.count("n"))  # n이 총 몇번 출현하였는가?  //time: 1:01:06


# print("a" + "b")
# print("a", "b")


# # 방법 ✍️✍️✍️✍️`졸신기`
# print(
#     "I am %d years old." % 25
# )  # 졸 신기!!😃 omg... D means only numbders, positive, negative
# print("나는 %s을 좋아해요" % "컴퓨터공학")  # s means string
# print("Apple은 %c로 시작해요." % "A")  # c menas character

# print("나는 %s살 입니다" % 20)
# print("나는 %s색과 %s색을 좋아해요" % ("빨강", "금"))
# print("%d * %d" %(20, 5))


# #방법2 😃😃😃😃😃
# print("나는 {} 살입니다".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("빨강", "금")) #지정안했지만, 순차적으로 배열
# print("나는 {0}색과 {1}색을 좋아해요".format("빨강", "금")) #{}안에 숫자와 값을 지정
# print("나는 {1}색과 {0}색을 좋아해요".format("빨강", "금")) #지정한 값이, 숫자에 따라 변형됨


# # 방법3 😆😆😆😆
# print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨강"))

# #방법4 (파이턴 버전 v3.6이상만 가능)
# age = 20
# color = "빨강"
# print(f"나는 {age}살이며, {color}색을 좋아해요") #직접적으로 variable을 채택했을 때


# print("백문이 불여일견, \n백견이 불여일타")  # \n은 줄바꿈
# # 저는 "나도코딩"입니다.
# print('저는 "나도코딩" 입니다')  # 큰 따옴표 프린트할 때 -방법1
# print('저는 "나도코딩" 입니다')  # \" 따옴표로 활용가능 \'


# # \\ : 문장 내에서 역슬러시 두개의 활용방법
# print("C:\\Users\\sydne\\USYDfirsthw")  # 경로찾기

# # \r : 커서와 그 뒤의 단어를 맨 앞으로 이동
# print("Red Apples \rPine")  # Red대신 Pine이 옮겨짐


# # \b : 백스페이스( 한 글자 삭제)
# print("Rebbb\bIt")  # 앞의 한글자 삭제


# # \t : 탭역할
# print("Red\tApple")  # 한 네칸 뒤로 간다고 보면 됨


## 👩‍💻Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

## 예) http://naver.com
## 1. http://을 없앤다. => naver.com
## 2.처음 만나는 점(.) 이후 부분을 없앤다 => Never
## 3.남은 글자 중 처음 세자리 + 글자갯수 + 글자 내 'e'의 갯수 + "!"로 구성
##  (nav)        (5)         (1)              (!)

## result: nav51!


# site = "http://naver.com"
# print(site[-9:])
# print(site[7:12])
# print(site[7:10] + str(len(site) - 11) + str(site.count("e")) + "!")  # 내가 한거


# # 선생님이 한거

# # url = "http://naver.com"
# url = "http://google.com"
# my_str = url.replace("http://", "")  # 규칙 1
# # print(my_str)
# my_str = my_str[
#     : my_str.index(".")
# ]  # sy_str부터 점 전까지 ::예 my_str[0:5] -> 0 - 5직전까지 (0,1,2,3,4)

# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1}입니다".format(url, password))
# # print(my_str)


# # Lists []

# # 지하철 칸별로 10명 20명 30명

# subway1 = 10
# subway2 = 20
# subway3 = 30

# print(subway1, subway2, subway3)

# subway = [10, 20, 30]
# print(subway)


# subway = ["rose", "great", "yoonsung"]
# print(subway)

# # great이 몇번째 칸에 타고있는가
# print(subway.index("great"))

# # namhee씨가 다음에 탔을 때
# subway.append("namhee")  # 붙이기 맨 마지막에 붙는다.
# print(subway)


# # sunny를 사이에 넣어보자, rose와 great사이에

# subway.insert(1, "sunny")
# print(subway)


# # 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)


# print(subway.pop())
# print(subway)  # 뒤에서 두번째 빠짐


# print(subway.pop())
# print(subway)  # 뒤에세 세번째 빠짐


# # 같은 이름의 사람이 몇명 있을까요? 알아보기

# subway.append("rose")

# print(subway)
# print(subway.count("rose"))  # 로즈란 이름 두번나옴


# # 정렬하기
# num_list = [5, 2, 10, 3, 98, 6, 9]
# num_list.sort()  # sort 정렬하기
# print(num_list)


# # 뒤집기 가능
# num_list.reverse()  # 뒤집기
# print(num_list)


# # 모두 지우고 싶으면
# num_list.clear()
# print(num_list)


# # 다양한 값을 섞어 사용가능
# mix_lists = ["rose", 20, True]
# print(mix_lists)  # Time: 1:30:58


# # 리스트 확장 1.
# num_list = [5, 2, 10, 3, 98, 6, 9]
# mix_lists = ["rose", 20, True]


# # 리스트 확장 2

# num_list.extend(mix_lists)
# print(num_list)


# # 사전

# cabinet = {3: "노아름", 100: "장우양"}
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(3))


# print(3 in cabinet)  #true
# print(5 in cabinet) #false


# # 사전 2

# cabinet = {"A-3": "노아름", "B-100": "김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])


# # 사전 2- 새손님
# print(cabinet)
# cabinet["C-20"] = "장우양씨"  # 새로운 손님이 왔을때
# cabinet["A-3"] = "신나라"  # 기존고객이 쓰던 사물함을 새로운 이가 넘겨받을때
# print(cabinet)


# # 손님이 떠났을 때
# del cabinet["A-3"]
# print(cabinet)  # A-3고객정보가 사라짐


# # 사물함 키들 정보만 출력하고 싶을 때

# print(cabinet.keys())  # 키와 고객이라고 보면 됨, 키는 처음 설정값

# # 고객들은 value가 됨
# print(cabinet.values())  # 고객들 이름

# # 키와 고객, 둘다 출력하고 싶을때 (keys and values)
# print(cabinet.items())

# # 목욕탕이 문닫을 때
# cabinet.clear()
# print(cabinet)


# ####튜플 연습, 속도가 리스트보다 빠름 ####

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# # menu.add("생선까스")  # 튜플은 add기능을 인정안함, 오류남


# # 튜플 1.

# (name, age, hobby) = ("노아름", 37, "컴퓨터")
# print(name, age, hobby)

# # SEt practice :중복이 안되고, 순서가 없쮸

# my_set = {1, 2, 3, 4, 5, 6, 6, 6, 6}
# print(my_set)  # 중복 값은 인정안함


# java = {"노아름", "장우양", "노상원", "김남희"}
# python = {"유재석", "박명수", "노아름"}

# # 교집합(java와 python을 모두 할 수있는 자)

# print(java & python)
# print(java.intersection(python))


# # 합집합 (java도 할 수있거나 python도 할 수 있는 개발자. 둘중 하나면 됨) //순서가 보장없음
# print(java | python)
# print(java.union(python))


# # 차집합 (java는 할 수있으나 python은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))


# # python을 할줄 아는 사람이 늘어남

# python.add("김태호")
# print(python)  # 김태호 추가됨

# # java를 까먹은 사람
# java.remove("노아름")
# print(java)


# # 자료구조의 변경

# menu = {"커피", "우유", "과자", "케이크", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))


# menu = set(menu)
# print(menu, type(menu))


# Practice #3
# (출력예제)
# --- 당첨자 발표 ----
# 치킨 당첨자 : 1
# 커피 당첨자: [2, 3, 4]
# --축하합니다 --


# # 👩‍💻Quiz)(활용예제)

# from random import *


# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # print(list)
# # shuffle(list)
# # print(list)
# # print(sample(list, 2))


# print(
#     "치킨 당첨자는"
#     + str((sample(list, 1)))
#     + "\n커피 당첨자는 "
#     + str(sample(list, 3))
#     + "입니다"
#     + "\n모두 축하드려요 😍"
# )


# # 내가 풀은 값


# from random import *

# users = range(1, 21)  # 1부터 20까지 숫자생성
# # print(type(users))
# users = list(users)  # 리스트로 변환
# # print(type(users))

# print(users)  # 리스트로 변환된 숫자 표기
# shuffle(users)  # 랜덤으로 숫자 섞기
# print(users)  # 랜덤으로 숫자 표기


# winners = sample(users, 4)  # 4명 중에서 1명은 치킨, 3명은 커피

# print(" --당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("--축하합니다--")


# ##선생님의 값


# ##✍️IF 조건 알아보기 ::예제 1

# weather = "snow"

# if weather == "rain":  # A면
#     print("take your umbrella")
# elif weather == "미세먼지":  # 혹은 B면
#     print("wear a mask")
# else:  # A도 아니고 B도 아니면
#     print("Do not as me anymore")  # Time: 2:00:41 take a break time


# ##IF 조건 알아보기 ::예제 2

# weather = input("오늘 날씨 어때요? ")  # 질문에 대한 답을 terminal에 쓰시오

# if weather == "rain" or weather == "snow":  # A면 ::조건 추가하기
#     print("take your umbrella")
# elif weather == "미세먼지":  # 혹은 B면
#     print("wear a mask")
# else:  # A도 아니고 B도 아니면
#     print("Do not as me anymore")


# ##IF 조건 알아보기 ::예제 3

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("it is too hot, you might be in danger, do not go outside!🥵")
# elif 10 <= temp and temp < 30:
#     print("it is fine, weather is nice to go out, enjoy your day!")
# elif 0 <= temp and temp < 10:
#     print("it is chill out there, you need to take a warm jacket and a coat 😏")
# else:
#     print(" it it too cold, do not go out. it is really freezing!")


# ✍️for 조건 (반복되는 상황에서 쓰여지는) :: 예제 1

# print("waiting : 1")
# print("waiting : 2")
# print("waiting : 3")
# print("waiting : 4")


# for waiting_no in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     print("waiting : {0}".format(waiting_no))

# for waiting_no in range(10):  # 0-10까지 ::위에와 같지만 훨씬 더 효율적
#     print("waiting : {0}".format(waiting_no))

# for waiting_no in range(2, 6):  # 0-10중에 내가 지정하고 싶을 경우 ::: 2-5까지
#     print("waiting : {0}".format(waiting_no))


# # string설정해서 반복문
# starbucks = ["아이언맨", "스파이더맨", "배트맨"]

# for customer in starbucks:
#     # print("customer : {0}".format(customer))
#     print("{0}, 커피가 준비되었습니다".format(customer))


# # ✍️While 연습1 ::조건을 만족할때까지 반복해라 (for은 무한반복이지만)

# customer = "토르"
# index = 5  # 처음 설정 값
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 됩니다.")  # 토르손님을 5번 불러도 대답없어서 폐기처분


# # While 연습2 ::조건을 만족할때까지 반복해라 (for은 무한반복이지만)

# customer = "아이언맨"
# index = 5  # 처음 설정 값
# while True:
#     # print("{0}, 커피가 준비 되었습니다.".format(customer))  # 무한루프반복 1
#     print("{0}, 커피가 준비됐쮸. 호출{1}회".format(customer, index))
#     index += 1

#::내생각: 연습1 무한루프와 다른점은 위에는 몇회불렀는지가 없고, 얘는 몇번 쳐불렀는지 확인가능


# customer = "아름"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비됐습니다".format(customer))
#     person = input("이름이 어찌 되나요? ")  # 이건, 고객:아름씨가 올때까지 무한반복으로 묻는다. 아름씨오면 미션 클리어!


# # ✍️continue와 break 연습 1::

# absent = [2, 5]  # 결석
# for student in range(1, 11):  # 1-10의 학생들이 존재함
#     if student in absent:  # 만약 학생들이 결석했으면
#         continue  # 쟤들 빼놓고 계속 남어지 학생들 전진  :: 컨티뉴의 역할
#     print("{0}, 책을 읽어봐".format(student))  # 책을 읽어보렴


# # ✍️continue와 break 연습 2::

# absent = [2, 5]  # 결석
# no_book = [7]  # 책을 놓고온 녀석

# for student in range(1, 11):  # 1-10의 학생들이 존재함
#     if student in absent:  # 만약 학생들이 결석했으면
#         continue  # 쟤들 빼놓고 계속 남어지 학생들 전진  :: 컨티뉴의 역할, 끝까지 계속 한다.
#     elif student in no_book:
#         print("오늘 수업 여기까지, {0}는 교무실로 따라와".format(student))
#         break  # 자기가 할당된 값까지만 실행하고 멈춘다. 그 뒤에 값이 더 있어도 바로 탈출, 브레이크의 역할
#         # continue

#     print("{0}, 책을 읽어봐".format(student))  # 책을 읽어보렴


# ✍️ 한줄 for ::연습 1


# # 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 => 101 102 103 104

# students = [1, 2, 3, 4, 5]
# print(students)  # 1. 이거 받고
# students = [i + 100 for i in students]  # 2. 1설정 받고 얹어서
# print(students)  # 3. 결과


# # ✍️ 한줄 for ::연습 2

# # 학생 이름을 길이로 변환

# students = ["rose Noh", "great Zhang", "selena Gomez", "justin Bieber"]
# students = [len(i) for i in students]
# print(students)


# # 학생 이름을 대문자로 변환

# students = ["rose Noh", "great Zhang", "selena Gomez", "justin Bieber"]
# students = [i.upper() for i in students]
# print(students)


# # 학생 이름을 소문자로 변환

# students = ["rose Noh", "great Zhang", "selena Gomez", "justin Bieber"]
# students = [i.lower() for i in students]
# print(students)


# 👩‍💻Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

# 조건 1: 승객별 운행 소요 시간은 5분-50분 사이의 랜덤수
# 조건 2: 당신은 소요시간 5분-15분 사이의 승객만 매칭해야함


# (출력문 예제)
# [0] 1번째 손님 (소요시간: 15분)
# [ ] 2번쨰 손님 (소요시간: 50분)
# [0] 3번째 손님 (소요시간: 5분)
# ...
# [ ] 50번째 손님(소요시간: 45분)

# 총 탑승승객: 2분


# # ✍️continue와 break 연습 1::

# absent = [2, 5]  # 결석
# for student in range(1, 11):  # 1-10의 학생들이 존재함
#     if student in absent:  # 만약 학생들이 결석했으면
#         continue  # 쟤들 빼놓고 계속 남어지 학생들 전진  :: 컨티뉴의 역할
#     print("{0}, 책을 읽어봐".format(student))  # 책을 읽어보렴


# 😏 내가 푼거

# question = int(input("도착역까지 몇분이 소요되시나요? "))
# if 4 >= question:
#     print("탑승불가합니다. 다음을 이용해주세요🥵")
# elif 5 <= question and question < 16:
#     print("손님, 탑승하세요")
# else:
#     print(" 다음을 이용해주세요!")


# # 😃😃v 선생님이 푼거, 중요하다 매우매우


# from random import *

# cnt = 0  # 총 탑승승객 수
# for i in range(1, 51):  # 1-50의 승객 설정
#     time = randrange(5, 51)  # 5분에서 50분 소요시간

#     if 5 <= time <= 15:  # 5분에서 15분 이내의 손님, 탑승 수 승객 수 증가처리, 매칭성공
#         print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1  # 카운트 값 증가처리
#     else:  # 카운트 값, 증가처리없음, 매칭에 실패하였기 때문
#         print("[] {0}번째 손님 (소요시간 : {1}분)".format(i, time))


# print("총 탑승 승객 : {0}분".format(cnt))


# ✍️ 함수연습


# def open_account():  # 함수정의 def, 입력값, 실행은 ()
#     print("새로운 계좌가 생성됐쮸.")


# open_account()  # 함수를 설정할때는 똑같은 함수 입력값을 두번 적어주지 않으면 프린터실행이 안됨


# # ✍️✍️✍️ 함수-전달값과 반환값


# def open_account():  # 함수정의 def, 입력값, 실행은 ()
#     print("새로운 계좌가 생성됐쮸.")


# def deposit(balance, money):  # 입금
#     print("입금됐쮸. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money  # 반환


# def withdraw(balance, money):  # 출금
#     if balance > money:  # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
#         return balance  # BREAK TIME : 2:35:40


# def withdraw_night(balance, money):  # 저녁에 출금
#     commission = 100  # 수수료 100원
#     return commission, balance - money - commission


# balance = 0  # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 200)
# commission, balance = withdraw_night(balance, 500)  # 500은 내가 출금하려는 금액
# print("수수료 {0} 원이며 잔액은 {1}원 입니다.".format(commission, balance))


# # ✍️✍️✍️ 함수-전달값과 반환값 -2번쨰


# Situation 1: all individuals have different backgrounds


# def profile(name, age, main_lan):
#     print("name : {0}\t age: {1}\t main language: {2}".format(name, age, main_lan))


# profile("ahrum", 20, "python")
# profile("great", 26, "JavaScript")


# # Situation 2: same school, same class, same subject ::공통분모가 있을때는, 아예 설정을 처음부터 한다


# def profile(name, age=18, main_lan="python"):
#     print("name : {0}\t age: {1}\t main language: {2}".format(name, age, main_lan))


# profile("rose")
# profile("great")


# # # ✍️✍️✍️ 함수-전달값과 반환값 -3번째, 키워드를 이용한 함수


# def profile(name, age, main_lan):
#     print(name, age, main_lan)


# profile(name="rose", main_lan="python", age=37)
# profile(name="great", age=35, main_lan="javascript")  #순차가 달라도, 키워드를 찾아서 재정비하여 배열한다.


# # ✍️✍️✍️ 함수-가변인자를 이용한 #1


# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("name : {0}\t age:\t".format(name, age), end=" ")  # end빈칸으로 해놓으면

#     print(lang1, lang2, lang3, lang4, lang5)


# profile("rose", 20, "python", "java", "c", "react", "solidity")
# profile("great", 37, "kotlin", "swift", "", "", "")


# # 이러한 상황에서, 내가 무슨 정보를 추가로 넣고싶을 때 ,


# def profile(name, age, *language):
#     print("name : {0}\t age:\t".format(name, age), end=" ")  # end빈칸으로 해놓으면
#     for lang in language:
#         print(lang, end=" ")
#     print()


# profile(
#     "rose", 20, "python", "java", "c", "react", "solidity", "C++"
# )  ##얼마든지 추가값을 넣어도 괜찮다.
# profile("great", 37, "kotlin", "swift")


# # ✍️✍️✍️ 함수-지역변수,전역변수

# # ---------비교 예제 1--------

# gun = 10  # global variable


# def checkpoint(soldiers):  # 경계근무
#     gun = 20  # local variable <<
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))


# print("전체 총: {0}".format(gun))  #
# checkpoint(2)  # 2명이 경계근무를 스러 나감
# print("남은 총 : {0}".format(gun))


# # ---------비교 예제 2--------

# gun = 10  # global variable


# def checkpoint(soldiers):  # 경계근무
#     global gun  # global variable은 def밖의 변수와 연동되어진다.
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))


# print("전체 총: {0}".format(gun))  #
# checkpoint(2)  # 2명이 경계근무를 스러 나감
# print("남은 총 : {0}".format(gun))


# # ----비교 예제 1과 2의 다른점을 생각하고 def안의 local variable과 def밖의 global variable을 이해하시오


# gun = 10  # global variable


# def checkpoint(soldiers):  # 경계근무
#     global gun  # global variable은 def밖의 변수와 연동되어진다.
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))


# def checkpoint_ret(gun, soldiers):  #위(경계근무)랑 같은 이야기인데, 다르게 설정하는 법, 이야기하는 것임
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun


# print("전체 총: {0}".format(gun))  #
# # checkpoint(2)  # 2명이 경계근무를 스러 나감
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))


# 👩‍💻Quiz)표준 체중을 구하는 프로그램을 작성하슈--------------------------------

# 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자: 키(m) * 키(m) *22
# 여자: 키(m) * 키(m) *21


# 조건 1: 표준체중은 별도의 함수 내에서 계산
#         함수명: std_weight
#         전달값: 키(height), 성별(gender)
# 조건 2: 표준 체중은 소수점 둘째자리까지 표시

# (출력예제)
# 키 175cm 남자의 표준 체중은 67.38kg입니다.
# ----------------------------------------------------------------------------

# # 🥸🥸🥸🥸🥸 스스로 풀어보시오!!(이거 안했음!)

# # 😃😃v 선생님이 푼거


# def std_weight(height, gender):  # 키 m단위(실수), 성별은 string으로 처리할 것
#     if gender == "male":
#         return height * height * 22
#     else:
#         return height * height * 21


# height = 175  # 센치미터 단위
# gender = "male"
# weight = std_weight(height / 100, gender)  # 키 센티미터가 아닌 m로 계산할거임


# print("키 {0}cm {1}의 표준 체중은 {2}kg입니다".format(height, gender, weight))  # 소수점 세째짜리까지 나옴.


# # ---소수점 둘째짜리까지 만드는 법 :: round (  , 2) ::: round반올림, 2는 소수점 둘쨰자리 의미 :: 위와 비교분석하시오


# height = 175  # 센치미터 단위
# gender = "male"
# weight = round(std_weight(height / 100, gender), 2)  # 키 센티미터가 아닌 m로 계산할거임

# print("키 {0}cm {1}의 표준 체중은 {2}kg입니다".format(height, gender, weight))


# # ✍️표준입출력 공부


# print("python", "java", "Javascript", sep=" , ")
# print("python", "java", "Javascript", sep=" vs ")  # 알아서 자동적으로 띄어쓰기 + 원하는 특수문자 넣기

# print(
#     "python", "javaScript", sep=",", end="?"
# )  # end="?"<-- 이녀석은 문장의 뒤에 ?을 쓰고, 그 다음 프린터값을 이어나감을 의미한다.
# print("which one is more having fun to learn?")


# # BREAK TIME: 3:00:34


# import sys

# print("python", "java", file=sys.stdout)  # stdout 표준출력으로 처리
# print("python", "java", file=sys.stderr)  # stderr 표준에러로 처리


# scores = {"math": 0, "english": 50, "coding": 80}
# for (
#     subject,
#     score,
# ) in scores.items():  # items는 key and value, it is set, not a certain variable.
#     # key     #value
#     # print(subject, score) #1
#     print(subject.ljust(8), str(score).rjust(4), sep=":") #compare #1
#     # ljust means, leftside + 8 spaces vacant, aligned
#     # rjust means, rightside + 4 spaces far away, keep vacant, aligned
#     # Why did it put 'str' because 50 is integer, must be kept by str, otherwise, print does not recognize it


# ✍️표준입출력 공부 -은행 대기 순번표

# # 001, 002, 003, 004 ...
# for num in range(1, 21):
#     print("waiting number : " + str(num))


# # 001, 002, 003, 004 ...
# for num in range(1, 21):
#     print(
#         "waiting number : " + str(num).zfill(3)
#     )  # 뭔가 3자리수로 표현하고 싶을 경우. zero를 fill 채운다.숫자만큼


# # ✍️표준입출력 공부


# answer = input("put any numbers : ")
# print("your put number " + answer + " is.")


# # ✍️다양한 print format

# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보

# print("{0: >10}".format(500))  # 앞에 10자리가 비어있음 500앞에
# # positive number represents +, negative number represents -

# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# # 왼쪽 정렬하고, 빈칸으로 _로 채움

# print("{0:<+10}".format(500))
# print("{0:_<+10}".format(500))
# print("{0:&<+10}".format(500))
# print("{0:*<+10}".format(500))  # 숫자뒤에 10자리 공간을 확보


# print("{0:,}".format(10000000000))  # 3자리마다 콤마 찍어주기
# print("{0:+,}".format(-10000000000))  # 3자리마다 콤마 찍어주기 +/- 부호도 붙이기


# # 3자리마다 콤마를 찍어주고, 부호도 붙이고 자리수도 확보하기

# print("{0:😛<+30,}".format(-1000000000000000))  # 저 이모티콘 자리엔 아무거나 넣어도 됨.
# # 숫자 뒤에 30자리 확보, 3자리마다 콤마 찍어주고, +/-도 넣어주고, 숫자가 자리를 다 못채우면
# # 못 채우는 만큼 설정한 특수부호 넣어주기

# # 소수점 출력
# print("{0:f}".format(2 / 3))  # f란 소수점이야기

# # 소수점을 특정 자리수까지만
# print("{0:.2f}".format(2 / 3))  # .2f란 소수점 2번째까지만,반올림해서


## ✍️✍️✍️✍️ 파일입출력::::자동으로 외부파일이 생성되는 기적!
#   ::오류남, score.txt가 안생김 :3:20-3:21//txt생겼는데, python안이 아니라, USYFfisrhw의 맨 마지막에 생성됨.
## python folder안으로 들여넣었을 때, 연동이 안되고 에러나며, 다시 바깥으로 생성됨


##1번 처음생성
# score_file = open("score.txt", "w", encoding="utf8")  # w는 쓰기를 의미
# print("math : 0", file=score_file)
# print("english : 40", file=score_file)
# score_file.close()  # 외부파일을 이용할 경우, open을 지정하였듯이 무조건 close도 해줘야한다

##2번 처음생성한 파일에다가 덛붙여 정보작성
# score_file = open("score.txt", "a", encoding="utf8")  # a는 덮어쓰기를 의미
# score_file.write("science: 80")
# score_file.write("\ncoding: 100")
# score_file.close()


# #3번 생성한 파일을 터미널에다가 불러오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()


# # 4번 생성한 파일을 터미널에다가 불러오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline())  # 한줄만 불러오기
# print(score_file.readline())
# # print(score_file.readline())
# # print(score_file.readline())
# score_file.close()


# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")  # 한줄만 불러오기
# print(score_file.readline(), end="")
# # print(score_file.readline(), end="")
# # print(score_file.readline(), end="")
# score_file.close()


# # 파일이 몇줄인지 모를때, 반복문을 통하여 불러올 수있음.
# score_file = open("score.txt", "r", encoding="utf8")
# while True:  # 무한루프
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
#     print(line, end="")  # 줄바꿈을 원치않을시 end=""넣어줌
# score_file.close()


# #list형식으로 저장

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()  # list 형식으로 저장
# for line in lines:
#     print(line, end="")

# score_file.close()


# 피클 기능 활용하기 #1  :정보를 파일에 집어넣고 파일생성
# import pickle

# profile_file = open("profile.pickle", "wb")
# # wb :writing binary, pickle을 import할때 encoding을 굳이 쓸 필요 없슈
# profile = {"name ": "rose", "age": 35, "hobby": ["study", "healingmusic", "coding"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장

# profile_file.close()  # terminal에 정보가 뜨며, profile.pickle이란 파일이 생성됨. @@주의@@ profile.pickle파일은 python folder외부에 있음.USYDfirsthw안의 맨 밑을 확인하시오


# # 피클 기능 활용하기 #2

# import pickle

# profile_file = open("profile.pickle", "rb")  #: 생성된 파일의 정보를 터미널에 불러오기
# profile = pickle.load(profile_file)  # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


# BREAK TIME: 3:30:23

# # ✍️With ::😛😛😛 졸라 신기방기!! -#1


# import pickle

# with open("profile.pickle", "rb") as profile_file:  #'rb' reading binary
#     print(pickle.load(profile_file))  # 따로 클로즈를 할 필요가없음


# # ✍️With ::😛😛😛 졸라 신기방기!! -#2

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("I study python hard!")  # 새로운 파일(study.txt)을 생성하며 그 곳에 정보를 기입


# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())  # 터미널에 기존 정보를 소환함


# 👨‍💻Quiz==================================================

# 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있다
# 보고서는 항상 아래와 같은 형태로 프린트 되어야한다


# -X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약:
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건: 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만든다.

# ===========================================================


# # # 😃😃v 선생님이 푼거


# for i in range(1, 4):  # 1주차부터 50주차까지, 숫자가 자동생성되야 하므로, 숫자먼저 세팅
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         # 숫자를 프린터 안에 인식하려면, string이 필요하며, 이 수식을 통하여
#         # 정보를 새로 생성될 파일안에 적어넣어야 하므로 writing에 해당되는 "w"처리를 한다.
#         # 한국어도 잘 인식되려면, encoding="utf8"은 필수이다. 이러한 것을 새로운 파일
#         # report_file에 저장한다.
#         report_file.write("-{0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무요약 : ")  # \n줄바꿈 표시가 없으면 다닥다닥 다들 붙어서 기입되어짐


# ✍️✍️✍️ Class 강의! ::스타크래프트 게임을 대입해 활용

# 마린: 공격 유닛, 군인, 총을 쏠 수 있음


# name = "marin"
# hp = 40  # 유닛의 체력
# damage = 5  # 유닛의 공격력

# print("{0} 유닛이 생성되었쭈".format(name))
# print("체력{0}, 공격력{1}\n".format(hp, damage))


# # 탱크 : 공격 유닛, 탱크, 포를 쏠 수있는 데, 일반모드/시즈모드

# tank = "tank"
# tank_hp = 150
# tank_damage = 35


# print("{0} 유닛이 생성되었쭈".format(tank))
# print("체력{0}, 공격력{1}\n".format(tank_hp, tank_damage))


# # 탱크2

# tank2 = "tank2"
# tank2_hp = 150
# tank2_damage = 35


# print("{0} 유닛이 생성되었쭈".format(tank2))
# print("체력{0}, 공격력{1}\n".format(tank2_hp, tank2_damage))


# # 마린과 탱크의 상관관계를 함수로 표현해보자!


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격한드아!!!. [공격력 {2}]".format(name, location, damage))


# attack(name, "1시", damage)
# attack(tank, "1시", tank_damage)
# attack(tank2, "1시", tank2_damage)


# 이렇게 하나하나 유닛값을 설정해줘도 되지만, 존나 엄청난 막노동+노가다를 의미하므로,
# 사피언스의 후예답게, 쉽게 가즈아!!! 이떄 class로 묶어서 표현 하즈아!! 붕어빵틀이라고 보면 됨.
# 붕어빵 하나하나 장인제작할래 그냥 찍어서 몇백개 만들래?


# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었쭈".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# marine1 = Unit("marine1", 40, 5)
# marine2 = Unit("marine2", 40, 5)
# tank = Unit("tank", 150, 35)

# Time break : 3:47:00


# # ✍️✍️✍️__init 함수


# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었쭈".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# marine1 = Unit("marine1", 40, 5)
# marine2 = Unit("marine2", 40, 5)
# tank = Unit("tank", 150, 35)

# marine3 = Unit("marine3")
# marine3 = Unit("marine3", 40) #__init__에 설정된 값 만큼 다 넣어줘야 오류가 안남


# # ✍️✍️✍️__init 함수


# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었쭈".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# # 레이스 생성: 공중유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))


# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 수법

# wraith2 = Unit("빼앗은 레이스2", 80, 5)
# wraith2.clocking = True  ##함수 바깥의 외부 변수를 추가로 넣을 수있음

# if wraith2.clocking == True:
#     print("{0}는 현재  클로킹 상태입니다.".format(wraith2.name))


# # ✍️✍️✍️__init 함수


# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었쭈".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# # 공격유닛


# class AttackUnit:
#     def __init__(self, name, hp, damage):  # self는 자기자신을 이야기한다. 무조건 적는다
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print(
#             "{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}".format(
#                 self.name, location, self.damage
#             )
#         )

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
#         self.hp -= damage
#         print("{0} :현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} :파괴되었습니다.".format(self.name))


# # 파이어벳:공격유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")


# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)
# firebat1.damaged(25)  # 마이너스값 나옴


# ✍️✍️✍️ 상속


# # ✍️✍️✍️__init 함수


# # 일반 쫄병 유닛
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었쭈".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# # 공격유닛


# class AttackUnit:
#     def __init__(self, name, hp, damage):  # self는 자기자신을 이야기한다. 무조건 적는다
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print(
#             "{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}".format(
#                 self.name, location, self.damage
#             )
#         )

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
#         self.hp -= damage
#         print("{0} :현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} :파괴되었습니다.".format(self.name))


# # 파이어벳:공격유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")


# ✍️✍️✍️✍️ 상속연습 -한번상속
#  메딕: 치료유닛(의무병), 공격력 0 ############ 헌데 기본 유닛, 함수에서 같은 것을
# 다 똑같이 쓰지않고, inherit을 통하여 코딩을 짜보기


# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp


# # 공격유닛


# class AttackUnit(Unit):  ##위의 일반유닛에서 상속받는다라는 것
#     def __init__(self, name, hp, damage):  # self는 자기자신을 이야기한다. 무조건 적는다
#         Unit.__init__(self, name, hp)  ##상속받는 코드
#         self.damage = damage

#     def attack(self, location):
#         print(
#             "{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}".format(
#                 self.name, location, self.damage
#             )
#         )

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
#         self.hp -= damage
#         print("{0} :현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} :파괴되었습니다.".format(self.name))


# # 메딕: 치료유닛(의무병)

# # 파이어벳:공격유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)


# # # ✍️✍️✍️다중상속


# # 일반유닛


# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp


# # 공격유닛


# class AttackUnit(Unit):  ##위의 일반유닛에서 상속받는다라는 것
#     def __init__(self, name, hp, damage):  # self는 자기자신을 이야기한다. 무조건 적는다
#         Unit.__init__(self, name, hp)  ##상속받는 코드
#         self.damage = damage

#     def attack(self, location):
#         print(
#             "{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}".format(
#                 self.name, location, self.damage
#             )
#         )

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
#         self.hp -= damage
#         print("{0} :현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} :파괴되었습니다.".format(self.name))


# # 드랍쉽: 공중유닛, 수송기, 마린/파이어뱃/ 탱크 등을 실어나름, 공격기능 없쮸

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print(
#             "{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed)
#         )


# # 공중 공격 유닛 클래스
# #
# #
# class FlyableAttackUnit(AttackUnit, Flyable):  # 위의 두 클래스를 inherit해온다.
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)


# # 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사

# valkyrie = FlyableAttackUnit("발키기", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")


# ✍️✍️✍️✍️연산자 오버로딩


# # 일반유닛


# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상유닛 이동]")
#         print("{0} :{1} 방향으로 이동한다.[속도 {2}]".format(self.name, location, self.speed))


# # 공격유닛


# class AttackUnit(Unit):  ##위의 일반유닛에서 상속받는다라는 것
#     def __init__(self, name, hp, speed, damage):  # self는 자기자신을 이야기한다. 무조건 적는다
#         Unit.__init__(self, name, hp, speed)  ##상속받는 코드
#         self.damage = damage

#     def attack(self, location):
#         print(
#             "{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}".format(
#                 self.name, location, self.damage
#             )
#         )

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
#         self.hp -= damage
#         print("{0} :현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} :파괴되었습니다.".format(self.name))


# # 드랍쉽: 공중유닛, 수송기, 마린/파이어뱃/ 탱크 등을 실어나름, 공격기능 없쮸

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print(
#             "{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed)
#         )


# # 공중 공격 유닛 클래스
# #
# #
# class FlyableAttackUnit(AttackUnit, Flyable):  # 위의 두 클래스를 inherit해온다.
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)  # 지상스피드를 interger 0으로 표기함
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동")
#         self.fly(self.name, location)


# # 벌쳐: 지상유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)


# # 배틀그루져: 공중유닛, 체력도 굉장히 좋음, 공격력도 좋음

# battlecruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)


# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")  # BreakTime 4:15:09
# battlecruiser.move("9시")


# ✍️✍️✍️PASS practice!(패스활용하기)
# 건물


# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상유닛 이동]")
#         print("{0} :{1} 방향으로 이동한다.[속도 {2}]".format(self.name, location, self.speed))


# # 공격유닛


# class AttackUnit(Unit):  ##위의 일반유닛에서 상속받는다라는 것
#     def __init__(self, name, hp, speed, damage):  # self는 자기자신을 이야기한다. 무조건 적는다
#         Unit.__init__(self, name, hp, speed)  ##상속받는 코드
#         self.damage = damage

#     def attack(self, location):
#         print(
#             "{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}".format(
#                 self.name, location, self.damage
#             )
#         )

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
#         self.hp -= damage
#         print("{0} :현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} :파괴되었습니다.".format(self.name))


# # 드랍쉽: 공중유닛, 수송기, 마린/파이어뱃/ 탱크 등을 실어나름, 공격기능 없쮸

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print(
#             "{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed)
#         )


# # 공중 공격 유닛 클래스#
# class FlyableAttackUnit(AttackUnit, Flyable):  # 위의 두 클래스를 inherit해온다.
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)  # 지상스피드를 interger 0으로 표기함
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)


# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass


# # 서플라이 디폿: 건물, 1개 건물 = 8 유닛
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


# def game_start():
#     print("[알림] 새로운 게임이 시작합니다.")


# def game_over():
#     pass


# game_start()  # print의 문구를 적는다.
# game_over()  # pass는 그냥 넘기고 종료. start와 비교하시오


# # ✍️✍️✍️SUPER practice!(슈퍼활용하기)


# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상유닛 이동]")
#         print("{0} :{1} 방향으로 이동한다.[속도 {2}]".format(self.name, location, self.speed))


# # 공격유닛


# class AttackUnit(Unit):  ##위의 일반유닛에서 상속받는다라는 것
#     def __init__(self, name, hp, speed, damage):  # self는 자기자신을 이야기한다. 무조건 적는다
#         Unit.__init__(self, name, hp, speed)  ##상속받는 코드
#         self.damage = damage

#     def attack(self, location):
#         print(
#             "{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}".format(
#                 self.name, location, self.damage
#             )
#         )

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
#         self.hp -= damage
#         print("{0} :현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} :파괴되었습니다.".format(self.name))


# # 드랍쉽: 공중유닛, 수송기, 마린/파이어뱃/ 탱크 등을 실어나름, 공격기능 없쮸

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print(
#             "{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed)
#         )


# # 공중 공격 유닛 클래스#
# class FlyableAttackUnit(AttackUnit, Flyable):  # 위의 두 클래스를 inherit해온다.
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)  # 지상스피드를 interger 0으로 표기함
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)


# # 건물


# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)  # 건물은 이동이 불가하므로, Speed자리에 숫자0값을 넣는다.::기존의 방법1
#         super().__init__(name, hp, 0)  # super을 통해 코드값을 적을 경우, self를 제외하고 삽입한다.
#         self.location = location


# # FAIL!!! ONCE AGAIN! ✍️✍️✍️게임만들어보기


# from random import *


# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))

#     def move(self, location):
#         print("[지상유닛 이동]")
#         print("{0} :{1} 방향으로 이동한다.[속도 {2}]".format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
#         self.hp -= damage
#         print("{0} :현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} :파괴되었습니다.".format(self.name))


# # 공격유닛


# class AttackUnit(Unit):  ##위의 일반유닛에서 상속받는다라는 것
#     def __init__(self, name, hp, speed, damage):  # self는 자기자신을 이야기한다. 무조건 적는다
#         Unit.__init__(self, name, hp, speed)  ##상속받는 코드
#         self.damage = damage

#     def attack(self, location):
#         print(
#             "{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}".format(
#                 self.name, location, self.damage
#             )
#         )


# # 마린
# class Marine(AttackUnit):  # 어텍유닛 상속받음
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#         # 스팀팩 :일정 시간동안 이동 및 공격 속도를 증가, 하지만 체력은 10감소

#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용한다 (HP 10감소)".format(self.name))

#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))


# # 탱크


# class Tank(AttackUnit):
#     # 시즈모드: 탱크를 지상에 고정시켜 더 높은 파워로 공격가능, 그럴 시 이동불가
#     seize_developed = False  # 시즈모드 개발여부

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.set_seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return

#         # 현재 시드모드 아닐 때  --> 시즈모드 하면 되고

#         if self.set_seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다".format(self.name))
#             self.damage *= 2
#             self.set_seize_mode = True

#         else:
#             print("{0} : 시즈모드로 해제합니다".format(self.name))
#             self.damage /= 2
#             self.set_seize_mode = False

#         # 시즈모드일 시, ==> 시즈모드 해제

#         # Time BREAK : 4:31:44


# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print(
#             "{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed)
#         )


# # 공중 공격 유닛 클래스#
# class FlyableAttackUnit(AttackUnit, Flyable):  # 위의 두 클래스를 inherit해온다.
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)  # 지상스피드를 interger 0으로 표기함
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)


# # 레이스


# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False  # 클로킹 모드 (해제상태)

#     def clocking(self):
#         if self.clocked == True:  # 클로킹 모드 --> 모드 해체
#             print("{0} : 클로킹 모드 설정 해제합니다".format(self.name))
#             self.clocked = False
#         else:  # 클로킹 모드 해제 ==> 모드 설정
#             print("{0} : 클로킹 모드 설정합니다".format(self.name))
#             self.clocked = True


# def game_start():
#     print("[알림] 새로운 게임 시작했쮸")


# def game_over():
#     print("Player :gg")  # good game
#     print("[Player]님이 게임에서 퇴장했습니다.")


# # 실제 게임 진행

# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()


# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()


# # 레이스 1기 생성

# w1 = Wraith()

# # 유닛 일괄 관리 (생성된 모든 유닛 append)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m1)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군이동
# for unit in attack_units:
#     unit.move("1시")

# # 탱크 시즈모드 개발

# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었쮸")


# # 공격 모드 준비(마린: 스팀팩, 탱크:시즈모드, 레이스:클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()

#     elif isinstance(unit, Wraith):
#         unit.clocking()


# # 전군 공격!

# for unit in attack_units:
#     unit.attack("1시")

# # 전군 피해

# for unit in attack_units:
#     unit.damaaged(randint(5, 21))  # 공격 랜덤으로 받고 범위는 5-20


# # 게임종료

# game_over()


# 오류남. 스타크래프트 다시 만들어봐야함


# 👩‍💻QUIZ  부동산

# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오

# (출력 예제)
# 총 3대의 매물이 있쮸
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년


# [활용할 코드]  :
# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         pass

#     # 매물정보표시
#     def show_detail(self):
#         pass


# # ✍️✍️👩‍💻선생님 값


# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     # 매물정보표시
#     def show_detail(self):
#         print(
#             self.location,
#             self.house_type,
#             self.deal_type,
#             self.price,
#             self.completion_year,
#         )


# houses = []  # 1. 하우스라는 리스트를 만든다
# house1 = House("gangnam", "apartment", "sales", "1million", "2010")
# house2 = House("mapo", "officetel", "deposited sales", "500k", "2007")
# house3 = House("songpa", "townhouse", "rent", "5000/500", "2000")

# houses.append(house1)
# houses.append(house2)
# houses.append(house2)


# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()

# # print(house1, house2, house3)

# # 강남 아파트 매매 10억 2010년
# # 마포 오피스텔 전세 5억 2007년
# # 송파 빌라 월세 500/50 2000년


# 예외처리
