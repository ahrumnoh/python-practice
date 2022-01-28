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
# print = [i+100 for i in students]
