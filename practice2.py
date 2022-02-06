# # practice 1
# print("hello world")
# print(2*5)
# print(3<5)
# print(not True)


# # practice 2

# animal1 = "cat"
# animal2 = "dog"
# name = "rose"

# print(animal1 + " & " + animal2 + "are my favourite pets.")
# print("Hey! " + name + "!!!")


# practice 2

# print(3 * 3,  9)
# print(3*3 ==9)


# cal = 2 * 3 * 4
# print(cal)

# print(cal * 3)


# name = "rose"
# age = 27
# salary = 150000
# bonus = 200000
# print(name + " salary is " + str(salary + bonus))


# print(abs(9))  # absolute value

# print(pow(4, 2))  # 16 pow =제곱
# print(max(5, 12, 10,3))
# print(min(2, 6, 0))
# print(round(3.2))
# print(round(8.9))


# from math import *
# print(floor(4.99))
# print(ceil(4.8))
# print(sqrt(9))


# from contextlib import redirect_stderr
# from gc import get_threshold
# from math import floor
# from random import *

# print(random()) #1미만의 임의값
# print(random()*10)
# print(random()+1)
# print(int(random() * 10)+1) #integer 정수
# # print(randint(1,45))
# print(randrange(1, 46))
# print("오프라인은 " + "매월" + str(randrange(1, 13)) + "  입니다.")


# data = randint(4, 28)
# print("every month, we are going to meet" + str(data))


# sentence = "I am the founder who created innovative software platform"
# print(sentence + " until 2024")

# sentence = """
# who am I?
# what do I do?
# I want to get into the software company soon
# I hope I will pass the second interview sincerely
# 🙂🙂🙂🙂
# No matter what, I have confidence!
# Let's go for it!

# I think learning python is so having fun!
# such a new field.
# Omg.....
# I cannot believe.
# I think most unbelievable mysterious happenings in my life.
# """


# print(sentence)


# numbers = "921212-121212"
# print(" 성별: " + numbers[-7:])


# name = "Rose is beaitufil"
# # # # print(name.upper())
# # # print(name[0].isupper())

# name = "Rose is beautifil"
# funFact = "is my favourite number"
# print(str(len(name)*5) + " " + funFact)


# name = "Roseb is beaitufil, wow excellent"
# print(name.replace(str("Rose"), str("Jessica")))
# print(name.replace("Rose", "Olivia"))


# # ⚠️⚠️⚠️⚠️ very curious
# index = name.index("e") #연동과정 1
# print(index)
# index = name.index("e", index+1) #연동과정 2
# print(index)
# index = name.index("e", index+10) #연동과정 3
# print(index)


# print( " I am %d years old" %25)
# print( " Hello, World! %s is my destiny" %"software engineering")
# print(
#     " I am %d yeard old" % 25
#     + " and my hobby is 'studying & learning %s & %s" % ("software engineering", "computer science")
# )


# print("I am {} years old ".format(randrange(1,20))) #format integer
# print("I am very happy to study {} & {}".format("computer", "finance")) #연동 순수 1
# print("I am very happy to study {0} & {1}".format("computer", "finance")) #연동 2
# print("I am very happy to study {1} & {0}".format("computer", "finance")) #연동 3


##Method 1
# print("I am {age} years old, {color} is my favourite".format(age=27,color="red"))


##Method 2
# book="computer science"
# color="gold"
# day = 30

# print("I bought "+ book + "  " + str(day) +" of November last year with " + color +" theme.")


# print(" I have a book \n that is my love")
# print( "Red  apple is so lovely \rPine")
# print("Hello World\b++++")
# print("hello world \tOMG")


# # # 연동과정
# subway = ["sydney", "new york", "seoul"]
# print(subway)  # 제네시스 1

# # print(subway.index("seoul"))
# subway.append("singapore")  # 덧붙이기2
# print(subway)
# subway.append("paris")
# # print(subway)  # 덧붙이기3


# subway.append("sydney")
# print(subway)
# print(subway.count("sydney"))
# print(subway.count("new york"))


# randomList=[9,4,1,6,8,20,34,77,3,6,7]
# # randomList.sort()
# # randomList.reverse()
# randomList.append(777)
# print(randomList)
# randomList.clear()
# print(randomList)


# client1 = ["rose", 27, "sydney", "single", False]
# client2 = ["great", 25, "seoul", "married", True]

# # print(client1)
# # print(client2)

# # extend clients

# additionalInfo = ["graduated Uni", "Accounting"]
# client1.extend(additionalInfo)
# # what is different of
# additionalInfo.extend(client1)

# print(client1)
# print(additionalInfo)

# # 🙂🙂🙂🙂🙂✍️


# cabinet = { 3: "rose", 100: "Great"}
# print(cabinet[100])
# print(cabinet.get(3))


# # 🙂🙂🙂🙂🙂✍️
# purse = {3: floor(3.88), "fiat": "great"}
# # print(purse.get("coin"))


# print(3.5 in purse)


# menu = ("samgyupsal", "jjajjangmyun", "friedrice")
# print(menu[1])


# 🤔TUPLE Exercise 1.

# (name, age, hobby) = ("rose", "33", "computer and reading")
# print(name, age, hobby)

# female = {"rose", "rosa", "roseline", "teacher"}
# male = {"great", "jack", "frankie", "teacher"}
# # print(female, male)

# # print(female&male)
# # print(female.intersection(male))
# # print(female | male)
# # print(female.union(male))
# # print(female - male)
# # print(male - female)


# female.add("Jennifer")
# print(female)
# female.remove("rose")
# print(female)


### BREAK TIME Line 409


# menu = {"우유","과자","귤"}
# # menu = list(menu)
# print(menu, type(menu))
# menu = set(menu)
# print(menu, type(menu))


# list = [1,2,3,4,5,6,7,8,9,10]
# print ("이번에 당첨되신 분은" + "[" + str(list[2]) +"," + str(list[3]) + "," + str(list[4]) + "]")


# from random import *

# users = range(1, 21)  # 1부터 20까지 숫자생성
# # print(type(users))
# users = list(users)  # 리스트로 변환
# # print(type(users))

# print(users)  # 리스트로 변환된 숫자 표기
# shuffle(users)  # 랜덤으로 숫자 섞기
# print(users)  # 랜덤으로 숫자 표기


# from random import *

# # users = range(31) #숫자만 잡은거 0-30까지
# users = range(1,31) #숫자만 잡은거 1-30까지
# users = list(users) #잡은 이후에 무조건 리스트를 입혀야 정렬이 됨
# shuffle(users) #섞을땐 프린트처럼 바로 씀
# print(users) #마지막 프린트


# weather = input("How is the weather today? ")

# if weather == "rain":
#     print("take an umbrella")
# elif weather == "snow":
#     print("wear a warm jacket")
# elif weather == "how":
#     print("Do not go outside, too hot!")
# else:
#     print("Perfect day! Enjoy your day!")


# from ast import Continue


# temp = int(input("what is the temperture for today? "))

# if 25 < temp:
#     print("It is too hot")
# elif 15 < temp <= 24:
#     print("It is a fine day. Let's go outside for a picnic")
# elif 0 < temp < 14:
#     print(" It is quite chill, wear a jacket for it")
# else:
#     print(" Too cold outside, Do not go out")


# for (반복되어지는 상황에서)

# for waiting_no in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     print("waiting : {0}".format(waiting_no))


# 지정안하고
# for waitingNumber in range(1,11):
#     print("waiting :  {0}".format(waitingNumber))


# 지정하고

# starbucks = ["rose", "great", "ellen"]
# for customer in starbucks:
#     print("sir/madam {0}, your order is ready".format(customer))


# ##Until reaching a certain point

# customer = "rose"
# index = 5
# while index >=1:
#     print("{0}, your order is ready {1}개의 나머지 오더 남았습니다.".format(customer, index))
#     index -= 4
#     if index <= 0:
#         print("your coffee is over")


# customer = "rose"
# person = "unknown"

# while person != customer:
#     print("{0}, your order is ready".format(customer))
#     person = input("what is your name? ")


# BREAK TIME 578

# # from random import *
# List = [2, 10]
# for students in range(0,30):
#     if students in List:
#         continue
#     print("{0}, read the book".format(students))


# # continue and break 연습

# absent = [3, 5, 8, 22]
# no_materials = [10, 11]

# for students in range(1, 25):
#     if students in absent:
#         continue
#     elif students in no_materials:
#         break
#     print("{0}, read the book ".format(students))


# students = [1,2,3,4,5]
# # print(students)
# lists = [i+100 for i in students]
# print(lists)


# names = ["rose", "jack", "james"]
# lists = [i+"hello" for i in names]
# print(lists)


# students = ["roseline", "great", "selena"]
# lists = [len(i) for i in students]
# print(lists)


# students = ["rose", "great", "selena"]
# students =[i.upper() for i in students]
# print(students)


# from random import *

# customers = 0
# for i in range(1,11):
#     time = randrange(10,31)

#     if 10 <= time <= 31:
#         print("[0] {0}번쨰 손님 (Time: {1}분)".format(i, time))
#         customers += 1
#     else:
#         print("[]번쨰 손님 (소요시간: {1}분)".format(i,time))

# print("총 탑승승객: {0}분".format(customers))

# def open_account():
#     print("hello world")
# open_account()

# def open_account():
#     print("new account opened")
# open_account()


# 😐 bank play

# def deposit(balance, money):
#     print(
#         "We've taken your deposit. thankyou. remaining is {0}".format(balance + money)
#     )
#     return balance + money


# def withdraw(balance, money):

#     if balance > money:
#         print(
#             "We've taken your deposit. thankyou. remaining is {0}".format(
#                 balance - money
#             )
#         )
#         return balance - money
#     else:
#         balance <= money
#         print(
#             "you cannot withdraw money. your account is not sufficient. your remaining balance is {0}".format(
#                 balance
#             )
#         )


# def weekend(balance, money, commission):

#     if commission == 100:
#         print(
#             "you received your balance {0} with commision charged".format(
#                 balance - money - commission
#             )
#         )
#         return balance - money - commission
#     else:
#         print("your commission amount is wrong".format(balance - money - commission))


# balance = 1000
# balance = deposit(balance, 2000)
# balance = withdraw(balance, 800)
# balance = weekend(balance, 200, 100)
# balance = deposit(balance, 500)

# # balance = deposit(balance, 3000)
# balance = withdraw(balance, 300)
# balance = weekend(balance, 300, 100)


# def profile(name, age, language):
#     print("name : {0}\t age: {1}\t language: {2}\t".format(name,age,language))


# profile("ahrum", 23, "korean")
# profile("jack", 33, "English")


# def profile(name, age=23, language="pythong"):
#     print("name : {0}\t age : {1}\t language : {2}".format(name, age, language))

# profile("Jack", 44, "Java Script")
# profile(name="Jack", age=44, language= "Java Script")


# gun = 10
# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print("남은총: {0}".format(gun))

# checkpoint(2)


# meals = 100

# def servingMeal(customer):
#     global meals
#     meals = meals - customer
#     print("the remaining meals: {0}".format(meals))

#     if meals == 0:
#           print("out of meals for today. thank you, use our meal tomorrow")


# servingMeal(100)


# def profile(name, age, language):
#     print("name : {0}\t age: {1}\t language: {2}".format(name, age, language))

# profile("ahrum", 30, "python")
# profile("Jack", 25, "JS")


# def std_weight(height, gender):
#     if gender == "male":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 170
# gender = "male"
# weight = round(std_weight(height /100, gender))

# print("height {0}, gender {1}  ".format(height,gender))


# print("python",30,5*2, round(1.3345,2))


# import sys

# from tokenize import String
# print("python","java", file=sys.stdout)
# print("python", "java", file=sys.stderr)
# print(sys.version)


# sys.stdout.write("This is a message for you\n")
# sys.stderr.write("This is an error message for you")


# a = 15
# b = 15.6
# c = "hi there"
# d = ["ahrum", 50, "python"]

# print(sys.getsizeof(a))  # bytes 28
# print(sys.getsizeof(b))  # bytes 24
# print(sys.getsizeof(c))  # bytes 57
# print(sys.getsizeof(d))  # bytes 120


# print(sys.argv)  #failed. what the heck of this?!🤧

# scores = {"math": 10, "english": 20, "coding": 30}
# for (
#     subject,
#     score,
# ) in scores.items():
#     print(subject.ljust(8), str(score).rjust(8), sep="|")


# scores = {"math": 10, "english": 20, "coding": 30}
# for (
#     subject,
#     score
# ) in scores.items():
#     print(subject.ljust(10), str(score).rjust(4), sep=":")

# candidates = {"Feb": 8000, "Mar": 10000, "April" : 12000}
# for (
#     month,
#     salary
# ) in candidates.items():
#     print(month.ljust(5), str(salary).rjust(7), sep="|")
#     print("Rose achieved a lot of outcomes! congrats!🙂👍👍👍😁, You deserve it!")


# Practiced til 'line 942 at practice.py'


# for num in range(1,6):
#     print(" waiting number : " + str(num))

# for num in range(1,6):
#     print(" waiting number : " + str(num).zfill(3))


# answer = input("let me know your numbers : ")
# print("Your favourite number is " + answer)

# print("{0: >+10}".format(50))
# print("{0: >+10}".format(-50))

# print("{0: <-10}".format(50))
# print("{0: <-10}".format(-50))


# print("{0: <+10}".format(50))
# print("{0:_<+10}".format(50))
# print("{0:&<+10}".format(50))
# print("{0:*<+10}".format(50))


# print("{0:,}".format(1000000000))
# print("{0:+}".format(1000000000))

# print("{0:<+30,}".format(-10000000000000000))


# print("{0:2f}".format( 3/ 4))

# score_file1 = open("score1.txt", "w", encoding="utf8")
# print("math : 0", file=score_file1)
# print("english : 40", file=score_file1)
# score_file1.close()



#######################################################

# employee_file = open("employee.txt", "w", encoding="utf8")
# print("name: ahrum", "position: staff", file=employee_file)
# print("name: jack", "position: engineer", file=employee_file)
# employee_file.close()


# # practice til line 1007 of practice.py

# employee_file = open("employee.txt", "a", encoding="utf8")
# employee_file.write("name: Miranda position: CEO")
# employee_file.write("\nname: Gabrielle position:CIO")
# employee_file.close()

# very interesting point. "w" and "a" modes are different to write something. there is no need to put "," as "w" function has above.


# employee_file = open("employee.txt", "r", encoding="utf8")
# print(employee_file.read())
# employee_file.close()

# Well... 자꾸 터미널 오류가 일어나서, 아무리 보아도, 코드가 맞는데 이상하다 싶으면, 터미널 강.종하고 다시 시작해보도록
# 생각보다 error가 자주일어날 수있음을 명심하도록. 디버깅 실력이 매우 중요하다.


# employee_file = open("employee.txt", "r", encoding="utf8")
# print(employee_file.readline())
# print(employee_file.readline())
# # print(employee_file.readline())
# # print(employee_file.readline())

# employee_file.close()

# if I recall the information individually from external text, the difference between lines, having a space 🤔 because this function focuses on each line, not a whole paragraph.


# employee_file = open("employee.txt", "r", encoding="utf8")
# while True:  # while은 무한루프
#     line = employee_file.readline()
#     if not line:
#         break  # 라인이 다 끝나면, 종료하고 나와라라는 뜻
#     # print(line)
#     print(line, end="")  # if you dont want to put a space between lines
# employee_file.close()


#Line 1057 at practice.py