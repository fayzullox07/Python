# PYTHON DATA TYPE
# >>>
# bool , NoneType, int , float , complex , str, bytes, bytearray, list,
# tuple, dict
# range, set , frozenset, ellipsis, function, module, type,
# 1. int >> 1, 89, -96
# 2. float >> 23.3, 10.3 , -56.3
# 3. bool >> True, False
# 4. str >> 'Hello', "Hello", """Hellooo"""

# Operators
# and or is in is not not in not

# print(1 and 0) # >> birinchi false
# print(1 or 0) # >> birinchi true
# print("a" in "abc") # >> abc qator ichida a bor
# print(not True)
# print(not False)
# print(not 0) 
# print("s" not in "abc") #true
# y = 10
# x = 10
# print(x is not y) #True



# type() >> qiymat turini aniqlash funlsiya
#x = 10 # + , - , * , / , %
#y = -5



# Arifmetic 
# x = 10
# x += 1
# print(x)
# x -= 1
# print(x)
# x *= 2
# print(x)
# x //= 2
# print(x)
# x **= 2
# print(x)




# float o'nlik son
# weight = 89.5
# height = 182.6
# print(weight + height)





#Bool True False
# is_admin = True #  int 1
# is_user = False # int 0
# print(True + False)
# print(type(is_user))







#Str Qator
# name = 'Abdullo'
# name2 = "abdullo " \
#         "Abdullo2"
# name3 = """Рекомендую выбирать
# только версию Home или Pro (или обе),
#  в зависимости от ваших потребностей. Нажмите
#   на кнопку Next, чтобы продолжить."""
# Maxsus belgilar
# text = " lorem \n ipsum" # yangi qatorga otish \n
# text = "text\tabzats" # \t abzats ong tomonga surish
# text = " lorem \"ipsum\" dolor"
# text = 'don\'t : \a'
# print(text)

# print(ord('w'))
# print(chr(74))

# height = int(input("Bo'yini kirit")) 
# print(f"Siz uchun ideal vazn {height - 100} kg")

# Foydalanuvchidan malumot olish 
# input() >> Userdan malumot qabul qilish
# name = input("Ismingiz nima?") # str formatda belgilarni qabul qilish
# print(type(name))
# print('Salom', name)
# String METHODS



# s = " 1python1"
# l = [1,2,3,4,5,6]
# # print(len(s)) uzunligini qaytaradi
# print(s.strip("1")) # berilgan strni massiv qiladi
# print(s.split())
# print("".join(["a","b", "c"]))

# print(r"Qatorrda maaxsus belgi ishlamaydi")

# Transform 
# print(s.lower())
# print(s.upper())
# print(s.capitalize())
# print(s.title())

# d = "Dockecr"
# print(d.find("k")) # indexini oladi
# print(d.index("o")) # indexini oladi
# print(d.count('c'))

# print(d.startswith("D"))
# print(d.endswith("D"))
# print(d.replace("Doc", "Soc"))

# f = "with"
# print(f.isalnum()) # True False
# print(f.isalpha()) # Faqat harf bolsa true 
# print(f.isdigit()) # Faqat sonlardan iborat bo'lsa 
# print(f.isdecimal()) # Natural sonlar bo'lsagina
# import keyword
# print(keyword.iskeyword("with"))

# mystr = 'The Quick BROWN fox jumps over the lazy dog.'

#print(mystr.capitalize())
#print(mystr.lower())
#print(mystr.upper())
#print(mystr.swapcase())
#print(mystr.title())

#print(mystr.count('O'))
#print(mystr.endswith('dog'))
#print(mystr.startswith('The'))
#print(mystr.find('cat'))
#print(mystr.rfind('he'))
#print(mystr.index('cat'))

#print('123AC'.isalnum())
#print('abcABC'.isalpha())
#print('abcABC'.isascii())
#isdecimal, isdigit, islower, isnumeric, isspace, istitle, isupper

#print(mystr.center(100))
#print(mystr.ljust(100, '-'))
#print(mystr.rjust(100, '-'))

#mystr = '      The Quick BROWN fox jumps over the lazy dog.           '
#print(mystr.strip())

#print(mystr.partition('he'))
#print(mystr.rpartition('he'))
#print(mystr.split('he'))

# text = '''Anthony created Pretty Printed in
# the year 2015.'''

# print(text.splitlines())











# Xatoliklar 
# SyntaxError, IndentationError, TypeError
# int() , str(), float(), bool()
#height = int(input("Bo'yingiz ?")) # faqat int qiymatni qabul qiladi
# height = int(height)
# print(type(height))
#optimal_weight = height - 100 # TypeError
#print('Siz uchun optimal vazn ', optimal_weight, 'kg')
# .format() f"{height}"
# age = 25
# weight = 89
# info1 = "Mening yoshim {0}da Vaznim esa {1}kg \n".format(age,weight) # Python 2.7
# info2 = f"Mening yoshim {age}da Vaznim esa {weight}kg" # Python 3.5
# print(info1,info2)






# x = 10 # int
# x = str(x) # str
# y = '10' # str
# y = int(y) # int
# z = 1
# z = bool(z) # True
# a = 0
# a = bool(a) # False
# f = ''
# print(bool(f))


# If-else
# user = int(input(" n: "))
# if user > 10:
#     print("OK")     
# elif True:
#     print("ERROR") 
# else:
#     print("Else block")
    
    
    
    
    
    
    
# for in 
# range() sonlar diapozoni >> sonlari oralig'i

# x = 0
# for i in 'str':
#     x += 1
#     print(i)
# print(x)

# arr = []
# for i in range(len(arr)) or range(10):
#     print("Olma")


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# arr = [x for row in matrix for x in row]
# # for i in matrix:
# #     for x in i:
# #         arr.append(x)
# print(arr)

# a = 'apple'
# n = 1
# s = 2
# print(a[n:s])
# while
# x = True
# while x:
#     password = input("Parolni kiriting \n >> \a")
#     if password != '':   
#         if password == 'gandi123':
#             print("Parol to'g'ri")
#             x = False
#         else:
#             print('False')
#     else:
#         print("Yozing")









# from ast import operator
# from codecs import utf_16_be_decode
# from concurrent.futures import process
# from encodings import utf_8
# from posixpath import split
# import random

# import faker #: random ishlaydi
# print(arr[3:]) - pichoq
# range() - bu diapazon
# print() - chop etish
# # print(list(range(51))) # qisqaroq - 50 gacha sonlar chiqadi
# print(random.randint(2,10)) # berilgan sonlar ichidan random sonlar oladi
# s = 'Python'
# print(random.choice(s)) # tasodifiy elementni oladi
# a = [1,2,3,4,5]
# random.shuffle(a) # massiv indexlarini chalkashtiradi poluchudes
# print(a)
# b = random.sample(a, 3) # Kerma    
# print(b)












# List() bu massiv


# arr.append(6) #oxiriga qiymat qo'shadi

# print(any([0,1,2, False])) # faqat bir dona true bolsaxam true qaytadi

# print(all([0,1,True])) # Hammmasi true bosa true

# arr1 = arr.copy()
# print(arr1)

# arr.extend(arr2) #kengaytiradi

# l = ['py' , "js" , "ph", 'c++']
# arr.insert(5, "6 soni") siz ko'rsatgan indexga siz ko'rsatgan qiymatni qo'shadi faqat bitta qiymatni
# l.insert(0, "C")
# print(l)
# arr.pop(5) # Siz ko'rsatgan index bo'yicha elemni o'chiradi qiymat bermasagiz oxirgini o'chiradi va ruyhatdan elem ni ctrl x qiladi agar elem bemasez oxirgini topolmasa index eroeeerrrrrrrrrrrrrr

# del arr[0]  # Siz ko'rsatgan index bo'yicha elemni o'chiradi

# arr.remove(9) range dan tashaqari son berilsa ValueError aks xolda tartib bo'yicha o'chiradi //bu yana berilgan qiymat ikkita bolsa 1-o'chiradi

# arr.clear() istalgan massiv tozzalaydi []

# print(arr.index(5)) elemdi indexini qaytaradi Agar topolmasa sokinadi value errrorrrrrrrrrrrr

# print(max(arr))

# print(min(arr))

# arr[:] === ctrl c

# sort sortirovka qiladi

# reverse - teskari qiladi

# s = (1,2,3,4) == o'zgarmas kortej class tuple


# set = Betartib qiymatlar extensionlar:

# s.union(set("yto")) #kengaytirish

# s.udapte(set("to")) #yangilaydi va qoshadi

# s.add(22) #elem qo'shish

# a.remove(22) #ochirish

# a.discard("A") #agar bo'lsa o'chiradi bo'lmasa hech qanday so'kinmaydi

# s.pop() #tasodifiy elemni o'chiradi

# s.clear #tozlaydi

# set2 = frozensent("str") muzlatilgan set

# enumerate() # indexi va elemni qaytaradi


# matrix = [[1,2,3], [4,5,6],[7,8,9]]
# for arr in enumerate(matrix):
#     print(arr) 



# for i in range(100,500,13):
#     print(i)
# s = [["py"], ["THON"]]
# l = [i for x in s for i in x]
# import random 
# for i in range(20):print(random.randrange(100,500,20))


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# d = [num for matrixElem in matrix for num in matrixElem if num % 2 == 1]
# print(d)


# Tuples 
# eslatma tuple xech qachon 1 ta elemtdan iborat bolmaydi
# t = ("1")
# print(t)

# tuple ozgarmas
# user , age = input(), input()
# print(user)

# new_age = user[0]
# print(new_age + "2")
# yaratish uchun (), tuple(range(5))


# SET , queryset >> Data Base query 
# s1 = set(["a", "af", "db"]) 
# s2 = {1,2,3,3}
# # print(len(s1)
# # Set methods
# print(s1.union(s2)) # extendi ukasi
# print(s1.update(4)) # elem qo'shadi
# s3 = s1.copy()
# s1.add(5)
# s1.remove(10) #key error
# s1.discard(10) #Agar bosa ochiradi bomasa qoshadi

# print(1 in s1)
# print(1 not in s1) 

# QIRQISH



# DICT() object eslatma!!! pythondagi object keyi faqat str bo'ladi 
# d = dict() OR d = {} > key + value
# d2 = {
#     "x":8, 
#     "y":15,
#     "e":5,
#     "z":13,
#     "f":7
#     }
# print(d2["key"])
# print(d2["name"])
# print(type(d2))

# Metohds
# print(d2.get("name")) # agar keyi bosa oladi bomasa None

# for i in d2: # Kalitini olish
    # print(i)

# for i in d2.items(): # valuesini olish
#     print(i)

# for x in sorted(d2.items()): # Sortirovka qilish
#     print(x)


# for x in sorted(d2.values()): # keylarini Sortirovka qilish
#     print(x)

# massivni dict qilish
# k = ["a", "b"]
# v = [1,2]
# d = dict(zip(k,v))
# print(d)

# d2.pop("x") # ko'rsatilgan key bo'yicha o'chirish

# d2.popitem() # oxiridan bitta o'chirish

# d2.clear() # tozalash

# d2.update({"b":"B value"}) # d2.update(c="c Value") #d2.update(("d", True))  # dict ga append qilish

# d3 = d2.setdefault('g', "E value")






# FUNCTION def
# funksiya argument qabul qiladi va ular ustida amal bajardi
# return bu funksiyada biror bir narsani qaytarish 
# funksiya nomi inglizcha mantiqan to'gri va ikki va undan ortiq bolsa _ belgisi bilan ajratish shart

# def str_func(s):
#     s = s.strip()
#     s = split(" ")
#     s = ",".join(s)
#     return s
# user = input()
# print(str_func(user))

# print(8 + None)

# *args
# bitta * lik metod bu berilayotgan argumentlarni tuple ga joyledi
# **kwargs ikkitalik * lim metod berilyatgan argumentlarni dict qilib qaytaradi



# Decorators
# Decorator bu biror bir funtionni ishlashiga tasir otqizadgan boshqa bir
# functionga aytiladi, masalan function ishga tushishidan avval biror bir
# ishni qilishi kerak bolsa decorator buni unga qildira oladi

# pin = input("PIN kodni kiriting..")
# def check_pinCode(pin):
#     def deco(f):
#         if pin == "1234":
#             return f
#         else:
#             return lambda : "Sizga ruxsat yo'q !"
#     return deco
#
# @check_pinCode(pin)
# def getMoney():
#     m = int(input("Qancha yechamiz ?"))
#     balance = 100
#     print("Chekni oling: balans=",balance-m)
#
# @check_pinCode(pin)
# def addMoney():
#     m = int(input("Qancha soamiz ?"))
#     balance = 100
#     print("Chekni oling: balans=", balance + m)
#
# print(getMoney())
# print(addMoney())



# Python operators
# global o'zgaruvchini global qiladi









# Fayllar bilan ishlash
# -*- coding: utf-8 -*-
# import os
# print(os.path)
# file = open("bloknot.txt", "a") # 1 param file path , 2 param bu rejim (r,a,b,w)
# print(file.read())# file ni o'qish
# file.close() # file ni yopish
# print(os.path.abspath("test.txt")) # file ning absolute manzili

# import os,sys
# print(f"Fayl : {os.path.abspath(__file__)}")
# print(f"Katalog : {os.getcwd()}")
# print(f"Import uchun katalog : {sys.path[0]}")
# print(f"TXT Faylga olib boruvchi path : {os.path.abspath('test.txt')}")

# open("fayl yolini", "rejim")
# # rejimlar:
# # r - oqish
# r+ - oqish + yozish
# w - yozish
# w+ - oqish + yozish
# a - qoshish
# a+ - qoshish + oqish
# x - xosil qilish
# x+ - xosil qilish agar oldindan mavjud bosa FileExistsError kotarish

# f = open("test.txt", "r")
# # print(f.readlines()) #List lines
# s = 0
# for i in f.readlines():
#     s += int(i.split("-")[1])
# print(s)


# import random as r
# for i in range(30):
#     rn = r.randint
#     with open("test.txt") as file:
#         file.writelines(f"{rn}")
# # with as : file ni as operatori orqali nomlab ochish va avtomatik yopiladi
# # with open(r"test.txt", "r") as f:
# #     print(f.write(ran_num))
    



# from faker import Faker
# fake = Faker()
# for i in range(10):
#     n = f.name()
#     a = f.address()
#     print(f"name : {n} - address : {a}")
    
# with open(r"texts.txt", "w+") as user_name:
#     for i in range(10):
#         user_name = f.name()
#         print(user_name)


# with open(r"test.txt", "w+") as file:
#     for i in range(300):
#         n = fake.name()
#         file.writelines(f"name : {n}\n")
#     # file.read()
# l = list(n)
# print(l.count("John"))



# users = []
# user_about = {}
# with open(r"test.txt", "w+") as file:
#     for i in range(10):
#         n = fake.name()
#         l = n.split(" ")
#         names = l[0]
#         sore_name = l[1]
#         user_about['name'] = names
#         user_about["surename"] = sore_name
#         users.append(user_about)
#         # users.append()
#         file.writelines(f"{user_about}\n") 
# print(user_about)





# users = []
# user_about = {}
# with open(r"test.txt", "a+") as file:
#     for i in range(10):
#         n = fake.name()
#         l = n.split(" ")
#         names = l[0]
#         sore_name = l[1]
#         adres = fake.address()
#         user_about['name'] = names
#         user_about["surename"] = sore_name
#         user_about["adress"] = adres
#         users.append(user_about)
#         file.writelines(f"{user_about}\n") 
# print(user_about)





# Exception
# with open("test.txt", "w") as f:
#     f.write("Mening faylim")
# with open("test.txt", "r") as read:
#     print(read.read())

# BaseException
# 1-Sytax
# 2-Logical
# 3- in process
# h = [x for x in range(10000 * 100)]
# try:
#     h = [x for x in range(10000 * 100)]
# except Exception as r:
#     print(r)
#     print(h)
# import requests



# try:    
#     with open("tesadst.txt", "w") as f:
#         f.write("Mening faylim")
#     with open("tesdast.txt", "r") as read:
#         print(read.read())
# except Exception as error:
#     print(error)
# print("ishladu")]


# url = 'https://docs.aiogram.dev/en/latessfd/efw'
# try:
#     r = requests.get(url)
#     print(r.status_code)
# except Exception as e:
#     print(e)
#     url = 'https://docs.aiogram.dev/en/latest/'
#     print("Please loading")
#     print(r.status_code)


# try:
#     s = "python"
#     for i in range(len(s)):
#         print(s[i+1])
# except IndexError as e:
#     print("Index ishib ketti")

# try:
#     str = "qator"
#     print(str)

# d = {
#         "key1":"Value"
#         }
# try:
#     print(d["aifdnia"])
# except KeyError:
#     print("Bunday kalit yo'q")
# finally:
#     print("Please loading")

# user = input("Kiriting")
# user[0].upper()
# user[1].upper()
# # a = len(user) // 2
# # user[a].upper()
# print(user)




# MALUMOTLAR OMBORI SQLITE3
# -*- coding: utf-8 -*-
import sqlite3

# SQL  >> Structed Query Language
# Jadval korinishida info larni saqlash
# Create a new table >> CREATE TABLE <table name>(
#     Create a new column >> <column name> INTEGER,TEXT,REAL,BLOB,NULL
# )
# INTEGER >> int values
# TEXT >>  str values
# REAL >> float values
# BLOB >> binary values
# NULL >> null values

# malumot joylash
# INSERT INTO <table name>(
#     VALUES (value1, value2 ...)
# )
# Tanlash
# SELECT * FROM <table name>

# Tanlab ochirish
# DELETE FROM <table name> WHERE id=2

# Jadvalni ochirish
# DROP TABLE <table name>


# sql = """\
#     CREATE TABLE musics(
#         song_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         song_name TEXT,
#         author TEXT
#     );
# """





con = sqlite3.connect("pupils.db")
cur = con.cursor()




sql = """\
    CREATE TABLE pupils_list(
        name TEXT,
        class TEXT,
        code TEXT
    );
"""

classes = ["8-a","8-a","8-b","8-b","8-b","8-a", "6-d", "7-a" ,"5-a ","6-d"]
pupil_name = ["Abdullayev A.", "Bahromov Sh.", "Davronov H.", "Davronova Z.", "Muhiddinov M." ,"Naimov K." ,"Noilov H." ,"Saidahmedov S.", "Sirojov S.", "To'laganov B."]
ids = ["1121", "1127", "1168", "1170", "1176", "1129", "875 ","960", "666", "891"]
for i in range(len(pupil_name)-1):
    sql = f"""\
        INSERT INTO pupils_list(name,class,code)
        VALUES('{pupil_name[i]}', '{classes[i]}', '{ids[i]}')
    """
    try:
        cur.execute(sql)
    except sqlite3.DatabaseError as e:
        print(e)
    else:
        print("CREATE TABLE users")
        con.commit()





cur.close()
con.close()







# import sqlite3
# from faker import Faker

# sql = """\
#     CREATE TABLE users_about(
#         name TEXT,
#         surname TEXT,
#         address TEXT
#     );
# """




# fake = Faker()

# for i in range(10):
#     name = fake.name().split(" ")[0]
#     surname = fake.name().split(" ")[1]
#     add = fake.address()

#     sql = f"""\
#         INSERT INTO users_about(name,surname,address)
#         VALUES('{name}','{surname}','{add}')
#     """
    
#     try:
#         cur.execute(sql)
#     except sqlite3.DatabaseError as e:
#         print(e)
#     else:
#         print("CREATE TABLE users")
#         con.commit()
# cur.close()
# con.close()








# try:
#     cur.execute(sql)
# except sqlite3.DatabaseError as err:
#     print(err)
# else:
#     # print("Person data is created.")
#     print(" data is created.")
#     con.commit() # malumotlarni tasdiqlab saqlash
# cur.close()
# con.close()


# import sqlite3
# print(sqlite3.version) # 2.6
# agar db fayl bolsa unga boglanish bolmasa uni xosil qilish
# conn = sqlite3.connect("myDb.db")
# # db ustidan boshqaruv uchun cursor() metodiga murojaat qilinadi
# cur = conn.cursor()
# # sql = """\
# #     CREATE TABLE user(
# #     id INTEGER PRIMARY KEY AUTOINCREMENT,
# #     email TEXT,
# #     password TEXT);
# # """
# sql = """\
#     INSERT INTO user(email)
#     VALUES('yoki@yoki.ru');
# """
# try:
#     cur.execute(sql)
# except sqlite3.Error as err:
#     print("Xatolik", err)
# else:
#     print("user TABLE siga yoki@yoki.ru emaili qoshildi")

# # db ustidan amallar bitganidan keyin u bilan aloqani uzamiz
# cur.close()
# conn.close()








