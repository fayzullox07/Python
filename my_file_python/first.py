import random
import locale
import datetime
import time
import platform

import calendar


# first.py
# import keyword
# print(keyword.kwlist)




# x = 10 #integer
# y = 10.2 #float
# print(x, y)
# s = "python"
# s2 = 'java'
# s3 = """
# Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
# Qui saepe sequi non eius reprehenderit inventore quisquam 
# obcaecati sapiente beatae architecto.

# """
# print(s , s2 ,s3)


# st = "\t\tpython \n\n java \a"
# print(st)


# n = "4"
#s = 12
# print(type(n))
# print(type(s))

#  print(str(s) * int(n))

# t = true
# f = false
#print(t + f)

# print(10 + 10)
# print(10 - 5)
# print(10 * 5)
# print(10 / 2)
# print(7 // 3)
# print(7 % 2)
# print(2 ** 2)

# s = "Python"
# print("t" not in s) #true
# print("t" in s) #false

# first.py

# print("olma" in "olma va behi mevalari")

# var = "may Var"
# x = 10
# x += 1
# x = x + 1
# print(x) #12

# x /= 2
# x //= 2
# x %= 2 
# x *= 2
# x **= 2
# print(x) 

# print(10 > 5)
# print(10 < 5)
# print(10 >= 5)
# print(10 <= 5)
# print(10 == 5)
# print(10 != 5)

# print(10 and 10)
# print(10 or 10)


# if 10 and 0:
#     print("Python")

# if 10 > 5:
#     print("If block")
#     elif 5 > 6:
#         print("elif block")
#         else:
#             print("Else block")


# user = int(input())
# if user % 2 == 0:
# print("Juft son")
# else:print("toq son")

# first.py
#task1
# user = input()
# if user == "1":
#     print("Windows")
# elif user == '2':
#     print("Linux")
# elif user == '3':
#     print("MacOs")
# elif user == '2':
#     print("Symbian OS")        


# for i in "python":
#     print(i , end='')
# else:
#     print("\n Sikl tugadii")


# for i in range(10):
#     if i % 2 == 0:
#         print(i) #juft sonlar

# arr = [1,2,3,4,5]
# for i in range(10):
# pass
# else:
#         print(i)


# arr = []
# for i in range(10):
#     arr.append(i)
#     print(arr)


# print([x for x in range(10)])



# first.py




# user = input()
# if user == "1":
#     print("Windows")
# elif user == '2':
#     print("Linux")
# elif user == '3':
#     print("MacOs")
# elif user == '4':
#     print("Symbian OS")        



# if 10 > 5:
#     print(10)
# else:
#     print(5)

# for i in range(10,30,5):
#     print(i)
# while True:
#     print("Python")
# i = 1
# while i <  101:
#     print(i)
#     i += 1
# x = True
# while x:
#     fruit = input("mevani kiriting")
#     if fruit == "stop":
#         x = False
#     else:
#         print(f"Meva nomi = {fruit}")

# summa = 0
# while True:
#     n = input("Sonni kiriting \n:")
#     if n == "stop":
#         break
#     n = int(n)
#     summa += n
# print(summa)

# for i in range(10):
#     if i % 2 == 1:
#         continue
#     else:
#         print(i)
# print(int(15.5)) #15
# print(float(1))#1.0
# print(round(1.5236,2))#1.52
# print(abs(-12))#12
# print(pow(2,2)) #4
# print(max(1,5,6,8,9))
# print(min(1,5,6,8,9))
# print(sum([1,2,3]))
# import math
# print(math.pi)
# print(math.ceil(63.5))
# print(math.floor(63.9))

# import random
# print(random.random())
# print(random.randint(0,10))
# print(random.randrange(0,10))
# arr = [1,2,3,4,5,6,7,8,9]
# random.shuffle(arr)
# str = "assalomalaykum"
# print(random.sample(str,5))

# print(random.sample(range(300),5))
# arr = [1,2,3,4,5]
# print(random.choice(arr))
# s = "python"
# arr = [1,2,3,4,5]
# # print(s[0],s[1],s[2],s[3],s[4],s[5])
# # print(s[10]) #IndexError:
# print(s[::-1]) # reverse
# print(s[0:2]) # py
# print(arr[2:4]) # [3, 4]

# a = 12
# n = "John, age = %s" %a #2.7
# print(n)
#
# x = 12
# y = "David, age = {0}".format(x) #2.7
# print(y)
#
# age = 12
# name = f"Abdullo , age = {age*2}" # 3.5
# print(name)
# print("Python".center(15))
# s = "*Lorem ipsum dolor amet sit*"
#print(len(s)) # 28
# print(s.strip("*"))
# print(s.lstrip("*"))
# print(s.rstrip("*"))
# print(s.split(" ")) # massiv qilish
# print(s.rsplit(" ")) # massiv qilish
# print("".join(["str", "str2"]))
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# s = "*Lorem ipsum dolor amet sit*"
# print(s.startswith("*Lorem")) # True
# print(s.endswith("sit*")) # True
# print(s.replace("amet", "dolor"))
# print(s.find("ipsum"))
# print(s.index("L"))
# print(s.count("o"))
# s = "*Lorem ipsum dolor amet sit*"
# print(s.isalnum()) # faqat son va harf
# print(s.isalpha()) # faqat  harf
# print(s.isdigit()) # faqat  son
# print(s.isnumeric()) # faqat son va rim raqamlari . 10 xonali sonlar ham
# print(s.isupper())
# print(s.islower())
# print(s.istitle())
# print(s.isprintable()) # print () orqali print qsa boladgan str lar
# import random
# letters_a = "abcdefghjklmnopqrstuzx"
# letters_A = letters_a.upper()
# symbols = "@#$%^&*()_+=/"
# numbers = "1234567890"
#
# p = letters_A + letters_a + symbols + numbers
#
# passwords_count = int(input("Nechta parol ? \n:"))
# letters_count = int(input("Nechta belgi ? \n:"))
#
# for i in range(passwords_count):
#     password = ""
#     for k in range(letters_count):
#         pLetter = random.choice(p)
#         password += pLetter
#     print(password)


# first.py
#KROS

# if 10 > 20:
#     print("Hello")
# elif 10 > 5:
#     print("Hi")
# else:
#         print("Bye")

# name = input("Your Name ?")
# if name.lower

# s = "Python"
# print(s[0] s[-1])

# for letter in s:
#     print(letter)

# for i in range(10,100,10):
#     print(i)

# s = "javascript"
# # print(len(s))
# for i in range(len(s)):
#     print(s[i])

# for i in range(10):
#     print(i)
# else:
#     print("Siklingiz tugadii")

# i = 0

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)



# while True:
#     i += 1
#     print(i)
#     if i == 100:
#         break



# first.py

# list()
# s = "Python"
# l = list(s)
# print(type(l))
# print("P" in l)
# r = range(0, 110, 10)
# for i in r: print(i, end=" ")
# arr = list("12345")
# arr = [1,2,3,4,5]
# arr[4] = 6
# # for i in arr:
#     print(i)

# arr2 = [7,8,9]
# arr.append(6) #oxiriga qiymat qo'shadi
# arr.extend(arr2) #kengaytiradi
# print(arr)
# # first.py
# arr.insert(5, "6 soni") siz ko'rsatgan indexga siz ko'rsatgan qiymatni qo'shadi
# arr.pop(5) # Siz ko'rsatgan index bo'yicha elemni o'chiradi
# del arr[0]  # Siz ko'rsatgan index bo'yicha elemni o'chiradi
# arr.remove(9) #range dan tashaqari son berilsa ValueError aks xolda tartib bo'yicha o'chiradi
# print(arr.count)
# print(all([1, 0, 0])) listda 1 ta elem true bo'lsa ham true qaytaradi aks holda false qaytaradi
# print(any([1, 0, 0])) listda hamma elem true bo'lsa true qaytaradi aks holda false keladi
# arr = [1,2,3,4,5]
# # arr.reverse() massivdi teskari qiladi

# rArr = reversed(arr)
# print(list(rArr))



# num = []
# for i in range(50):
#     num.append(i)
# print(num) # uzunroq

# print(list(range(51))) # qisqaroq

# # first.py

# from typing import Match

# print(random.sample(range(100),20))

# num = int(input("0-20 orasida son kirit \n:>>>>"))
# for i in range(10):
#     r = random.choice(range(1, 10))
#     if num == r:
#         print("Yutiz")       
# else:
#     print("Topilmadi")



# arr = [1,2,3,4,5,6,8,9]
# print(arr[5:0])





# w = 200
# h = 200
# s = w * h
# print(f"{s} metr kvadrat")

# f = frozenset("Str")
# print(type(f))


# user = {
#     "name":"Abdullo",
#     "age": 12,
#     "is_admin":False
# }
# # user["name"] ="JOHN" #mavjud elemni o'zgartiradi
# # user["skil"] = ["HTML", "CSS"] #yangi elem qo'shadi
# # print("age" in user) #True
# # # print("age" not in user) #false
# # print(user.get("age")) #12 : key orqali value olish


# # for x in user: #Faqat keylari olinadi
# #     print(x)

# # for k in user.items(): #elemlar orqali tuple() ko'rinishida
# #     print(k)


# company = {
#     "Apple":"Iphone",
#     "Samsung":"Android",
#     "MI":"Redmi"
# }
# c = company.copy() #nusxa olish
# c.clear() #tozlash
# company.update({"nokia":"3110"}) #dict oxiriga key va value qo'shadi
# company.pop("nokia") 

# locale.setlocale(locale.LC_ALL, "uz-Latn-UZ")
# t = time.strftime("%H:%M %d.%m.%y %B")
# print(t)




# print(datetime.timedelta(weeks=1, days=2, hours=10, minutes=5, seconds=55))
# d1 = datetime.timedelta(days=3)
# d2 = datetime.timedelta(days=1)
# print(d1 - d2) #2 days, 0:00:00

# t = datetime.date
# print(t.today())
# print(t.year)
# # print(t.month)
# # print(t.day)

# n = datetime.datetime.now()
# print(n)


# for i in range(10):
#     print("Hello")
# time.sleep(4)    



# c = calendar.TextCalendar(0)
#
# uz_calendar = calendar.LocaleTextCalendar(0, "uz-Latn-Uz")
# print(c.format)
#

#
# def func(**k):
#     print(type(k))
#     for i in k:
#         print(i)
# func(a=1,b=2,c=3)
# func("Abdullo":)


#
# def superFunc(*args, **kwargs):
#     """Istalgan aargumentni qabul qiladi"""
#     for i in args:
#         print(i, end="0")
#     for j in kwargs.items():
#         print(j)
# superFunc(1,2,3,4,5, olti=6,yetti=7)





# f = lambda: 10 + 20

# t = tuple(range(10))
# print(type(t))


# python
# first.py

#
# def get_word():
#     user = input("Iltimos yozing")
#     if user[0] == user[-1]:
#         print(user)
#     else:
#         print("Palindronmas")
# get_word()
#
#
# def get_user_word(user1,user2):
#     return print(user1.count(user2))
#
# get_user_word("ALLA", "A")
#     # first.py
# Shaxsiy ro'yxat yarating
# 2. Ro‘yxat oxiriga str tipidagi yangi element qo‘shing
# 3. Indeksli joyga int tipidagi yangi element qo'shing
# 4. Ro‘yxat oxiriga yangi turdagi ro‘yxat elementini qo‘shing
# 5. Indeksli joyga tuple tipidagi yangi element qo'shing
# 6. Indeks bo'yicha elementni oling
# 7. Elementni olib tashlang
# 8. Ro‘yxat bandining takrorlanish sonini topin
# arr = [1,2,3,"ali",4,"vali",5,3]
# arr2 = [1,2,"bali"]
# arr.append(6)
# arr[0] = int(6)
# arr.extend(arr2)
# arr[3] = tuple("Alijon")
# print(arr[4])
# arr.remove(-1)
# print(arr.count(arr)
#
#
# Shaxsiy lug'at yarating
# 2. str tipidagi kaliti va int tipidagi qiymati bo'lgan yangi element qo'shing
# 3. Tuple tipidagi kalit va tip ro'yxati qiymati bilan yangi element qo'shing
# 4. Buyumni kalit bilan oling
# 5. Elementni tugma bo'yicha o'chirish
# 6. Lug'at kalitlari ro'yxatini oling

dicts = {"VALI":12,"Gani":13}
dicts["Ali"] = 12
dicts[-1] = ("ABdullla 13 yoshda")
print(dicts['VALI'])
    # python first.py