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


from contextlib import redirect_stderr
from gc import get_threshold
from random import *

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
# such a new field. I have never thought that I am doing something in computer
# Omg.....
# I cannot believe..
# How have I been here so far..
# In my life,
# I have never thought about studying or learning computer.


# What a coincidence! Is this real coincidence or destiny? 😐🤔
# I am super duper curious.
# Sometimes... it makes me so laughing.
# why?
# Because...unbelievable!
# How dare..? how come...? I do computer!!! OMG..
# Even I do computer, I cannot believe this is real or not.

# Only my interests were art, education and finance before.


# .
# .
# .
# .

# For me..
# Such a miracle!


# How could I be accepted by Harvard??
# How could I get in computer world?

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


name = "Roseb is beaitufil, wow excellent"
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


client1 = ["rose", 27, "sydney", "single", False]
client2 = ["great", 25, "seoul", "married", True]

# print(client1)
# print(client2)

# extend clients

additionalInfo = ["graduated Uni", "Accounting"]
client1.extend(additionalInfo)
# what is different of
additionalInfo.extend(client1)

print(client1)
print(additionalInfo)

# 🙂🙂🙂🙂🙂✍️
