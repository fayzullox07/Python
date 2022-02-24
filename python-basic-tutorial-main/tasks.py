# task 1
# input :  arr = [2,3,4,5,6,7,8]
# user numbers (index, step) 0 , 3
# output :  arr = [3,4,5,2,6,7,8]
# 2
# arr = [3,4,5,2,6,7,8] massivda istalgan sonni tanlasam shu sonni onga yoki chapga suruvchi functiuon yozing
# masalan men 2 bilan 3 ni kiritsam function mendan sorasin 2-indexdagi elementni 3 ta index onga suremi yoki chapga deb chapga desam chapga sursin
# # task 2
# input: arr = [2,4,6,7,9]
# output: max sum and min sum

# task 3
# input: arr = list(random nums : 20)
# output: max sum and min sum

# task 4
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# massivni ichida 5 dan kichik barcha sonni chiqaring

# task 5
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# ikkala massivda ham qatnashgan sonlarni chiqaring

# task 6
# dict ni qiymatlari osishiga qarab saralang
# masalan : d = {'a':12, 'b':7} >> d = {'b':7, 'a':12}

# task 7
# user dan sonlarni vergul orqali kiritlgan string qabul qiling
# ushbu sonlardan int qiymatidagi tuple ni qaytaring
# u = "1,2,3"
# t = (1,2,3)
# def func(a : int,b : int) -> int:
#     return a * b
# task 8
# qator palindrom yoki palindrom emasligini aniqlan
# masalan alla palindrom u chunki onga ham chapga ham bir hil oqiladi

# task 9
# user kiritgan sonlar oraligida nechta aynan usha sonlarga
# qoldiqsiz bolinuvchi son borligini aniqlang
# masalan 2,10 >> 10 uchun 2 ga qadar 5 bor yani  1 ta

# task 10
# user kiritgan qator ichidan raqamlarni ajratib oladigan
# function yozing

# task 11
# random belgilar ketma ketligidan user kiritgan miqdorda unikal kod
# xosil qilib uni tuple da saqlaydigan getRandomCode() function ni yozing
# maslan user = 3
# t = ("dddas54f5","asfddv6c","cncnku5d52")

# Selection sort
# arr = [10,23,-8,6,-1,0,2,3,7]
# N = len(arr)
# for i in range(N - 1):
#     m = arr[i]
#     p = i
#     for j in range(i+1, N):
#         if m > arr[j]:
#             m = arr[j]
#             p = j
#     if p != arr[i]:
#         t = arr[i]
#         arr[i] = arr[p]
#         arr[p] = j
# print(arr)


# input: assalomu alaykum
# ouput: alkmosu

# task 1
# Petya va Vasya karta oynayapti, ular o'radan butun musbat sonlar
# biriktirlgan kartalarni tortishadi keyin qiymatlarini tekshirishadi
# kimda kam qiymat bolsa u yana karta tortadi va kartani ozida olib qoladi
# kartalar tugashi bilan kimda eng kam qiymat bolsa u yutgan boladi
# oyin oxirida golibni ismini va ochkolarini maglubni ismi va ochkolarini
# chiqaradgan dastur tuzing

# input: kartalar soni 52 ,biriktirilishi mumkin bolgan sonlar: 3 < n < 999
# output : winner = Vasya 12, looser=Petya 23

# a = 1
# try:
#     a = 2
#     print(a)
#     raise Exception()
# except:
#     a = 3
#     print(a)
#     raise
# else:
#     a = 4
#     print(a)
# finally:
#     a = 5
#     print(a)

# d1 = {
#     "a":1
# }
# d2 = {
#     "b":2
# }
# d1.update(d2)
# print(d1)
# print(tuple(range(10)))

# def mergeDict(*dicts):
#     d = {}
#     for i in dicts:
#         d.update(i)
#     return d
# print(mergeDict(d1,d2, {"c":3}))

# s = "alla"
# count a  ?
# def func(letter, word):
#     return print(word.count(letter))

# func("a", "alla")

# def sum_two_number(x,y):
#     print(x+y)
# MAX_VALUE = 100
# apple = "Stive Jobs"








# begin 1
# a = int(input("Kvadratning tomonini belgilang:  "))
# print(4 * a,"sm")
# short form


# begin 2
# a = int(input("Kvadratni tomonini belgilang:  "))
# print(a ** 2,'sm')

# begin 3
# a,b = int(input("Kvadratni tomonini belgilang:  ")),int(input("Kvadratni tomonini belgilang:  "))
# print(f" Yuzi {a * b} sm \n Perimetri {2 * (a+b)}")

# begin 4
# d,pi = int(input("Aylananing diametrini belgilang:  ")),3.14
# print(f"Aylananing uzunligi {pi * d}")

# begin 5
# a = int(input("Aylananing diametrini belgilang:  "))
# print(f"  Hajmi {a ** 3} sm \n Sirti {6 * (a ** 2)} sm")

# begin 6
# a,b,c = int(input("Paralipipedning tomonini belgilang:  ")),int(input("Paralipipedning tomonini belgilang:  ")),int(input("Paralipipedning tomonini belgilang:  "))
# print(f" Hajmi {a * b * c} sm \n Sirti {2 * (a * b + b * c + a *c)}")


# begin 7 
# a,pi = int(input("R ni belgilang:  ")),3.14
# print(f"L = {2 * pi * a} sm S = {pi * (a ** 2)} sm")


# begin 8
# a,b = int(input("1 - sonni belgilang:  ")),int(input("2 - sonni belgilang:  "))
# print(f"O'rta arifmetigi {(a + b) // 2}")

# begin 10
# num_1,num_2 = int(input("1-sonni belgilang:  ")),int(input("1-sonni belgilang:  "))
# if num_1 == 0 and num_2 == 0:print("Xatolik siz 0 ni kiritdingiz")
# else: print(f"Yig'indisi {num_1 + num_2}ga Ko'paytmasi {num_1 * num_2} ga 1-sonni kvadrati {num_1 ** 2} ga 2-sonni kvadrati {num_2 ** 2} teng")

# begin  11
# num_1,num_2 = int(input("1-sonni belgilang:  ")),int(input("1-sonni belgilang:  "))
# if num_1 == 0 and num_2 == 0: print("Xatolik siz 0 ni kiritdingiz")
# else: print(f"Yig'indisi {num_1 + num_2}ga Ko'paytmasi {num_1 * num_2} ga 1-sonni moduli A{num_1} ga 2-sonni kvadrati A{num_2} teng")

#  begin 12
# a,b,c = int(input("1-sonni belgilang:  ")),int(input("2-sonni belgilang:  ")),a ** 2 + b ** 2
# print(f"c = {a ** 2 + b ** 2} ga P = {a + b +c} sm")

# pi = 3.14
# begin 13
# r1,r2 = int(input("1-sonni belgilang unutmang 1-son katta bo'lishi kerak :  ")),int(input("2-sonni belgilang:  "))
# if r1 <= r2:#     print("xatolik r1 kichkina son berildi iltimos to'g'irlab keyin urinib ko'ring")
# else:#     print(f"S1 = {pi * r1} sm S2 = {pi * r2} sm S3 = {r1-r2} sm")    

# begin 14
# l = int(input("l ni kiriting"))
# print(f"R = {2 * pi * l} sm S = {pi * (2*pi*l)}")

# begin 15 
# s = int(input("l ni kiriting"))
# print(f"d = {2 * pi * l} sm R = {pi * (2*pi*l)}")

# begin 16
# x2,x1 = int(input("x2 yozing katta bo'lsin")),int(input("x1 yozing kichik bo'lsin"));
# print(f"Masofasi = {x2 - x1}sm")


# begin 17
# a,b,c = int(input("A ni kiriting eslatma kamayish tartibida son kiriting")),int(input("B ni kiriting")),int(input("C ni kiriting"))
# print(f"AC kesma uzunligi = {a - c}sm, BC kesma uzunligi = {b - c}sm, Yig'indisi {(a - c) + (b - c)} ")

# begin 18
# a,b,c = int(input("A ni kiriting eslatma kamayish tartibida son kiriting")),int(input("B ni kiriting")),int(input("C ni kiriting"))
# print(f"AC kesma uzunligi = ${a - c}sm, BC kesma uzunligi = ${b - c}sm, Ko'paytmasi {(a - c) * (b - c)}")

# begin 20
# x1,x2,y1,y2 = int(input("x1 ni kiriting")),int(input("x2 ni kiriting")),int(input("y1 ni kiriting")),int(input("y2 ni kiriting"))
# print(f"Masofa = {(x2 - x1) ** 2 + (y2 - y1) ** 2 }")





# int 1
# m,user = 100,user = int(input('Kiriting '))
# print(f"{user / m} m")

# int 2
# t,user = 1000,int(input('Kiriting '))
# print(f"{user / t} Kb")

# int 3
# t,user = int(input('Kiriting ')),int(input('Kiriting '))
# print(f"{t-user} ta")

# # int 4
# t,user = int(input('Kiriting ')),int(input('Kiriting '))
# print(f"{(t/user) - user} ta")

# int 5
# t,user = int(input('Kiriting ')),int(input('Kiriting '))
# print(f"{(t/user) - user} ta")


# int 7
# user = input('Kiriting ')
# print(f"Yig'indisi {sum(user)}")

# int 8
# user = input('Kiriting ')
# print(f"Son = {user[1]}{user[0]}")

# int 9
# user = input('Kiriting ')
# print(f"Yuzligi {user[0]}")


# # int 10
# user = input('Kiriting ')
# print(f"Yuzligi {user[0]} o'nligi {user[1]} birligi {user[2]}")

# # int 15
# user = input('Kiriting ')
# print(f"Son {user[1]}{user[0]}{user[-1]}")

# # int 16
# user = input('Kiriting ')
# print(f"Son {user[0]}{user[2]}{user[1]}")

# int 17
# user = list(input('Kiriting '))
# print(f"Yuzligi {user[1]}")

# int 18
# user = list(input('Kiriting '))
# print(f"MIngligi {user[0]}")


# int 19
# user = int((input('Kiriting ')))
# print(f"{user // 60}")

# int 20
# user = int(input('Kiriting '))
# print(f"{user / 3600}")

# if 1
# num = int(input("Belgilang \n :"))
# if num > 0:print(f"son = {num + 1}")
# else:print(num)
    
    
# if 2
# num = int(input("Belgilang \n :"))
# if num > 0:print(f"son = {num + 1}")
# else:print(f"son = {num-2}")

# if 3
# num = int(input("Belgilang \n :"))
# if num > 0:print(f"son = {num + 1}")
# elif num < 0:print(f"son = {num-2}")
# else:print(f"son = {10}")
    
    
# if 4
# nums = list(int(input("Belgilang \n :")),int(input("Belgilang \n :")),int(input("Belgilang \n :")))
# if num[0] > 0:print(nums.len())

# if 5
# user1 = list([int(input("Son kirit")),int(input("Son kirit")),int(input("Son kirit"))])
# pl = 0
# min = 0
# for i in range(len(user1)):
#     if user1[i] > 0:pl+=1
#     else:min+=1
# print(f"{pl} ta musbat")
# print(f"{min} ta manfiy")


# if 6
# user1,user2 = int(input("Son kirit :")),int(input("Son kirit :")) 
# print(f"kattasi {max(user1,user2)} kichigi {min(user1,user2)}")

# if 7
# user1,user2 = int(input("Son kirit :")),int(input("Son kirit :")) 
# print(f"kattasi {max(user1,user2)} kichigi {min(user1,user2)}")

# if 8
# user1,user2 = int(input("Son kirit :")),int(input("Son kirit :"))
# print(f"kattasi {max(user1,user2)} kichigi {min(user1,user2)}")

# if 12
# user1,user2,user3 = int(input("Son kirit :")),int(input("Son kirit :")),int(input("Son kirit :"))
# print(min(user1,user2,user3))

# if 14
# user1,user2,user3 = int(input("Son kirit :")),int(input("Son kirit :")),int(input("Son kirit :"))
# print(max(user1,user2,user3))
# print(min(user1,user2,user3))

# if 15
# user1 = [int(input("Son kirit :")),int(input("Son kirit :")),int(input("Son kirit :"))]
# print(f"Yig'indi {sum(user1)}")

# if 16
# user1 = int(input("Son kirit :")),int(input("Son kirit :")),int(input("Son kirit :"))
# if user1 < user2 < user3:print(f"A = {user1 ** 2} B = {user2 ** 2} C = {user3 ** 2}")
# else:print(user1,user2,user3)    

# if 17
# user1,user2,user3 = int(input("Son kirit :")),int(input("Son kirit :")),int(input("Son kirit :"))
# if user1 < user2 < user3:print(f"A = {user1 ** 2} B = {user2 ** 2}" C = {user3 ** 2}"")
# elif user1 > user2 > user3:print(f"A = {user1 ** 2} B = {user2 ** 2} C = {user3 ** 2}")
# else:print(user1,user2,user3)    


# if 18
# user1 = int(input("Son kirit :")),int(input("Son kirit :")),int(input("Son kirit :"))


# # for 1
# k,n = int(input('Kiriting ')),int(input('Kiriting '))
# if n > 0:
#     for num in range(n):print(k)

# for 2
# a,b = int(input('Kiriting ')),int(input('Kiriting '))
# nums = 0
# if a < b:
#     for num in range(a, b+1):
#         nums += 1
#         print(f"son {nums} sonlar soni {nums}")
        
        
# for 3
# a,b = int(input('Kiriting ')),int(input('Kiriting '))

# nums = list(range(a,b))
# nums.sort(reverse=True)
# print(f"sonlar {nums} sonlar soni {len(nums)}")
        

# for 4
# user = int(input("Kiriting "))
# for i in range(1, 11):
#     price = i * user
#     print(f"{i} kg konfet narxi {price} so'm")
    

# for 5
# user = int(input("Kiriting "))
# fl = 0.1
# for i in range(1, 11):
#     price = i * user
#     fl += 0.1
#     print(f"{fl} kg konfet narxi {price} so'm")
    
# for 6
# user = int(input("Kiriting "))
# fl = 1.2
# for i in range(1, 11):
#     price = i * user 
#     print(f"{fl} kg konfet narxi {price} so'm")
#     fl += 0.2

# for 7
# a,b = int(input("KIRITING:  ")),int(input("KIRITING:  "))
# print(sum(range(a,b)))

# for 8
# a,b = int(input("KIRITING:  ")),int(input("KIRITING:  "))
# for i in range(a,b):
#     sqr = i * i
# print(sqr)


# for 9
# a,b = int(input("KIRITING:  ")),int(input("KIRITING:  "))
# kv = []
# for i in range(a,b):
#     kv.append(i**2)
# print(sum(kv))
# # print(sum(kv))   




# for 10
# n = int(input("Kiriting"))
# num = 0
# for i in range(1,n):
#     if n > 0:
#         s = 1 + 1 / i
#         num += s
# print(num)


# for 11
# n = int(input("Kiriting "))
# r = 0
# for i in range(1,n):
#     n2 = n**2 + ((n+1)**2)
#     r+=n2
# print(r)


# for 12
# n = int(input("Kiriting "))
# f = float(1)
# for i in range(n):
#     f += 0.1
#     r = f*f
# print(r)


# for 13
# n = int(input("Kiriting "))
# fl = float(1)
# fl += 0.1
# for i in range(n):
#     if fl == 1.1:
#         r = fl-(fl+i) + (fl+i) - (fl+i) + (fl+i) - (fl+i) + (fl+i) - (fl+i)
# print(r)


# for 14 
# n = int(input("Kiriting "))
# for i in range(1,n,2):
#     n2 = n**2
#     r =  i + (i+2)
# print(r)

# # for 15
# n,a = int(input("Kiriting ")),int(input("Kiriting "))
# for i in range(1,n):
#     kv = a ** n
# print(kv)


# for 16
# n,a = int(input("Kiriting ")),int(input("Kiriting "))
# for i in range(1,n):
#     r = a**i
#     print(r)


# for 17
# n,a = int(input("Kiriting ")),int(input("Kiriting "))
# arr = []
# for i in range(1,n):
#     r = a**i
#     print(r)
#     arr.append(r)
# result = 1+a 
# print(f"Yig'indisi {result + sum(arr)}")
    
# for 19
# n = int(input("Kiriting "))
# for i in range(1,n):
#     if n > 0:
#         print(f"{n} * {i} = {n*i}")







#1 
# user = input("Yozing: ")
# if 't' in user:print("Bor")
# else:print("Yo'q")


#2 
# user = int(input("Yozing: "))
# if user % 2 == 0:    print('musbat')
# else:    print('Manfiy')


#3
# user = input("Kiriting: ")
# if user == 'windows':
#     print("Microsoft")
# elif user == 'linux':
#     print("Ubuntu")
# elif user == 'macOs':
#     print("apple")
# else:
#     print("Xatolik")


# 1
# user = input("Kiriting")
# for i in user:
#     for k in i:
#         print(k)
# 2
# user = int(input("Kiriting "))
# weigth = 0
# for i in range(user): 
#     weigth += 3
# print(weigth)

# 3
# for i in range(3):
#     num = int(input("Son ?"))
#     if num == i:
#         print("You are victory")
#     if num > i:
#         print("Kotta")
#     elif num < i:
#         print("Kichik")



# 4
# import random
# x = True
# myNum = random.randint(0, 10)
# while x:
#     num = int(input("Son ? \n:"))
#     if myNum== num:
#         x = False
# print("Topting")


# 5
# x = True
# num = 0
# arr = []
# while x:
#     user = input("Kiriting")
#     if user == 'stop':
#         x = False
#     else:
#         arr.append(int(user))
# print(sum(arr))


# 6
# x = True
# arr = []
# while x:
#     user = input("Kiriting ")
#     if 'k' in user and 'k' in user:
#         print('ALERT')
#         x = False
#     else:
#         print("keyingi son")
#         user = input("Kiriting ")
        


# user = int(input("Kiriting "))
# if user > 4 and user < 10:print(print(print(print(print()))))
#     print("Xayrli tong")  
# elif user > 10 and user < 17:
#     print("Xayrli kun")  
# elif user > 17 and user < 23:
#     print("Xayrli tun")  


# num = 17
# while num < 101: 
#     num += 1
#     print(num)


# user1,user2,user3 = int(input("KIriting ")),int(input("KIriting ")),int(input("KIriting "))
# if user1 < user2 < user3:
#     print(f"Yig'indi {user1+user2+user3}")
# else:
#     print(f"{user1}{user2}{user3}")

# user1 = int(input("KIriting "))
# if user1[0] == 'a' or user1[0] == 'A':
#     print('Yes')
# else:
#     print("FALSE")



# user1 = input("KIriting ")
# nums = len(user1) // 2 - 1
# if nums == nums:
#     print('Yes')
# else:
#     print("O NO") 

# user1 = int(input("kiriting"))
# user2 = int(input("kiriting"))
# user3 = int(input("kiriting"))
# user4 = int(input("kiriting"))
# user5 = int(input("kiriting"))
# if sum(user1,user2,user3,user4,user5) == sum(user1,user2,user3,user4,user5):
#     print("YEs")
# else:
#     print("O no")


# lorem = "Lore_mipsu_mdolorsit=amet43consectetur_adipisicing_elit34_olorumdeserunt_3234assumenda"
# import random
# arr = ''
# pas = random.sample(lorem, 8)
# print("".join(pas))
# large form
# for i in range(8):
#     st = random.choice(lorem)
#     arr += st

# print(arr)


# tropger 1
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print([elem for elem in a if elem < 5])



# tropger 2
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# matrix = []
# matrix.extend(a)
# matrix.extend(b)
# print(set(matrix))

# tropger 3
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print(dict(sorted(d.items())))
# print(dict(sorted(d.items(), reverse=True)))

# tropger 4
# r = {}
# dict_1 = {1:10, 2:20}
# dict_2 = {3:30, 4:40}
# dict_3 = {5:50, 6:60}
# for i in (dict_1, dict_2, dict_3):
#     r.update(i)

# tropger 5
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# result = sorted(my_dict, reverse=True)[:3]
# print(result)




# import random
# import math
# print(max(random.randint(10_000, 100_000),random.randint(10_000, 100_000),random.randint(10_000, 100000)) - min(random.randint(10000, 100000),random.randint(10000, 100000),random.randint(10000, 100000)))

# s = 2
# l = 3
# user = input("Kiriting")
# print(int(user[::-1])d))



# 1
# a,b = 4,5
# print(a+b)


# 3
# a,b,c = int(input("Kiriting")),int(input("Kiriting")),int(input("Kiriting"))
# if a*b==c:
#     print("YES")
#     print(8*54)
# else:
#     print("NO")

# 5
# a,b = int(input("Kiriting")),int(input("Kiriting"))
# if a < b:
#     print("< ")
# elif a > b:
#     print(">")
# else:
#     print("=")


# 6
# a,b = int(input("Kiriting")),int(input("Kiriting"))
# print(f"garri {10 - a} ta larri {10-b} ta ota olmagan")

# 7
# f = True
# c=max=0;
# while f:
#     x = '00101110000110'
#     if '0' in x:
#         c=c+1 
#         f = False
#     else:
#         c=0
#         if c>max:
#             max=c;
# print(max);

# Chisla E
# n = int(input("Kiriting "))
# e = '2.7182818284590452353602875'
# if 0 <= n <= 25:
#     print(e[:n])


# Keyboard
# k = 'qwertyuiopasdfghjklzxcvbnmq'
# u = input("Kiriting ")
# if u in k:
#     a = k.index(u) + 1 
#     print(k[a])
    
    
#  Dom shkola dom
# h = input("Kiriting")
# n = int(input("Kiriting"))
# if h == 'uy' and n % 2 == 0:
#     print("OK")
# elif h == 'maktab' and n % 2 != 0:
#     print("NO")
# else:
#     print("BIG ERROR")



# #Arbuzi 
# n = int(input("Kiriting "))
# x = [4,7,15,8]
# print(f"Buvisi uchun {min(x)}  O'zi uchun {max(x)} ta arbuz oldi")

# # Turna
# j = int(input("kiriting ")) 


# # Kar telefon
# print(int(input("kiriting")))



# s1 = {i for i in range(1,21)}
# print(s1)


# a,b,c = int(input('Kiriting ')),int(input('Kiriting ')),int(input('Kiriting '))
# for i in range(a):
#     b = b+c+1
#     if b >= 100:
#         print("Yetib bordi")
#         break
# else:
#     print("Avariya")


# user = int(input('Kiriting '))
# gues = int(input('Kiriting '))

# if user // gues:
#     print("OK")
# else:
#     print("NO")



from itertools import count
import random
# m = [random.randint(0,200) for i in range(50)]
# j = []
# t = []
# for i in m:
    # if i % 2 == 0:
        # j.insert(0,i)
        # print(f"O'ng tomoni {i}")
    # elif i % 2 != 0:
        # j.append(i)
        # print("chap tomoni {i}")
    
# print(f"Juftlar {j} toqlar{t}")

# def get_num(s):
#     for i in s:

# print(get_num("gandi123"))


# user = int(input("kiriting"))
# for i in user:
#     if user[1] % user[0] == user[1] % user[0] == 0:        
#         print("bor")
    

# def 1
# def power_a3(num):
#     return num ** 3
# user = int(input("kiriting "))
# print(power_a3(user))

# def 2
# def powerA234(num):
#     return f"kvadrati {num ** 2} kubi {num ** 3} 4-darajasi {num ** 4}"
# user = int(input("kiriting "))
# print(powerA234(user))

# def 3
# def mean(a,b,c,d):
#     return f"ab ning o'rta afigmetigi {(a + b)//2}vac ning o'rta afigmetigi {(a + c)//2}vad ning o'rta afigmetigi {(a + d)//2}"
# user1 = int(input("kiriting "))
# user2 = int(input("kiriting "))
# user3 = int(input("kiriting "))
# user4 = int(input("kiriting "))

# print(mean(user1,user2,user3,user4,))

# def 4
# def triangle(a,b,c):
#     return f"Perimetri {a + b + c} Yuzasi {a / (b * c) }"
# user1 = int(input("kiriting "))
# user2 = int(input("kiriting "))
# user3 = int(input("kiriting "))

# print(triangle(user1,user2,user3))

# def 5




# def 6
# def digit_count_sum(a,b,c):
#     nums = [a,b,c]
#     return f"kirilgan raqamlar soni {len(nums)} Kiritilgan raqamlar yig'indisi {sum(nums)}"
# print(digit_count_sum(1,2,3))

# # def 7
# def inver_digit(*nums):
#     r = nums[::-1]
#     return r
# print(inver_digit(1,2,3))


# def 8
# def add_left_digit(k,r,l=0,s=0):
#     arr = []
#     if k < 0 or r < 0 or l < 0 or s < 0:
#         arr.insert(k, 0)
#         arr.insert(r, 0)
#         arr.insert(l, 0)
#         arr.insert(s, 0)
#     else:
#         arr.append(k)        
#         arr.append(r)        
#         arr.append(l)        
#         arr.append(s)        
#     return arr
# k = int(input("KIRITING "))
# r = int(input("KIRITING "))
# s = int(input("KIRITING "))
# g = int(input("KIRITING "))
# print(add_left_digit(k,r,s,g))


# # def 9
# def add_left_digit(k,r,l=0,s=0):
#     arr = []
#     if k < 0 or r < 0 or l < 0 or s < 0:
#         arr.append(k)
#         arr.append(r)
#         arr.append(l)
#         arr.append(s)
#     else:
#         arr.insert(k, 0)        
#         arr.insert(r, 0)        
#         arr.insert(l, 0)        
#         arr.insert(s, 0)        
#     return arr
# k = int(input("KIRITING "))
# r = int(input("KIRITING "))
# s = int(input("KIRITING "))
# g = int(input("KIRITING "))
# print(add_left_digit(k,r,s,g))

# def 11
# def min_max(a,b,c,d):
#     x = []
#     y = []
#     arr = [a,b,c,d]
#     arr.sort()
#     x.append(arr[0])
#     x.append(arr[1])
#     y.append(arr[-1])
#     y.append(arr[-2])
#     return f"x da {x} y da {y} "
# print(min_max(1,22,34,5))        


# def 12
# def sorts(a,b,c):
#     arr = [a,b,c]
#     arr.sort()
#     return arr 
# print(sorts(5,6,8))


#  def 13
# def sorts(a,b,c):
#     arr = [a,b,c]
#     arr[0] = max(arr)
#     arr[-1] = min(arr)
#     return arr 
# print(sorts(5,6,8))


# # def 14
# def shift(a,b,c):
#     a = b
#     b = c
#     c = a
#     return f"a {a} b {b} c {c}"
# print(shift(5,6,8))


# # def 15
# def shift(a,b,c):
#     a = c
#     b = a
#     c = b
#     return f"a {a} b {b} c {c}"
# print(shift(5,6,8))

# def 16
# def get_num(nums):
#     if nums > 0:
#         print("musbat")
#     if nums < 0:
#         print("manfiy")
#     else:
#         print(0)    
# print(get_num(-3))


# def 18
# def sum_s(a,b,c):
#     PI = 3.14
#     return f"birinchi doirani yuzi {PI * (a**2)} ikkinchi doirani yuzi {PI * (b**2)} 3chi doirani yuzi {PI * (c**2)}"

# def 19
# def rings(r1,r2):
#     PI = 3.14
#     r_1 = PI * (r1 ** 2)
#     r_2 = PI * (r2 ** 2)
#     return f"tushmaydigan qismi {r_1 - r_2} sm"
# print(rings(5,3))


# def 20
# def triangle(a,b):
#     return f"perimetri {a+b} sm"
# print(triangle(2,10))

# def 21
# def sum_range(a,b):
#     if a < b:
#         nums = list(range(a,b))
#         return sum(nums)
#     else:
#         return 0
# print(sum_range(2,8))

# def 22
# def arifmetic(a,b):
#     n1 = a - b
#     n2 = a * b
#     n3 = a // b
#     n4 = a + b
#     return f"birinchi amal {n1} ikkinchi amal {n2} uchinchi amal {n3} to'rtchi amal {n4}"
# print(arifmetic(4,6))

# def 24    
# def even(k):
#     if k % 2 == 0:
#         print("True")
#     else:
#         print("False")
# print(even(10))

# def 25
# def get_kvadrat(k):
#     r = []
#     for i in range(1,50):
#         r.append(i)    
#     if k in r:
#         return "True"
#     else:
#         return "False"
# print(get_kvadrat(25))

# def 26
# def get_kvadrat(k):
#     r = []
#     for i in range(1,10):
#         r.append(5**i)    
#     if k in r:
#         return "True"
#     else:
#         return "False"
# print(get_kvadrat(24))

# def 27
# def get_kvadrat(k,n):
#     r = []
#     for i in range(1,10):
#         r.append(n**i)    
#     if k in r:
#         return "True"
#     else:
#         return "False"
# print(get_kvadrat(25,4))

# def 28
# def odd_numbers(n):
#     if n % 2 == 0:return "TRUE"    
#     else: return "FALSE"
# print(odd_numbers(3))


# def 29
# def sum_range(k):
#     nums = list(range(1,k))
#     print(len(nums))
# print(sum_range(7))

# def 31
# def is_palindrom(s):
#     name = 'ada'
#     if name.find(name[::-1])==0:
#         print("palindrom")
#     else:
#         print("palindrommas")

# user = list(input("Kiriting "))
# result = []
# for i in range(len(user)-2):
#     if user[i] == user[i+1]:
#         user.remove(user[i+1])
#     result.append(user)
# print("".join(result[0]))


# user = list(input("kiriting "))
# s = []
# for i in range(1,len(user)):
#     if user[i] % 2 == 0:
#         user[i].lower()
#         user[i-1].upper()
#     s.append(user)
# print("".join(s))



# alpha = list("abcdefghijklmnopqrstuvwxyz")
# # print(alpha)
# user = input("kiriting ")
# for i in enumerate(user)
#     if user in alpha:
#         print(i)



# print(result)
# print(set(user))
# def 37
# def power(a,b):
#     return f"Qiymat {a ** b}"

# print(power(5,2))        



# def 38
# def power2(a,n):
#     res = 0
#     if n > 0:
#         for i in range(n):
#             res = a * a
#     elif a < 0:
#         for i in range(n):
#             res = 1 / (a*a)
#     return res
# print(power2(-3,2))        



# def 39
# def power3(a,n):
#     if n <= 0:
#         return power(a,n)
#     else:
#         return power2(a,n)
# print(power3(4,2))


# def 40


# s = 'apple'
# chrs = []
# for i in s:
#     ch = ord(i)
#     chrs.append(ch)
# print(chrs)


# wovels = "aeiou"
# user = list(input("KIriting: "))
# # arr = []
# for i in range(len(user)):
#     if user[i] in wovels:
#         user.insert(i, user[i])
#         print(user[i])
# print(user)


# import datetime
# import time
# ch1 = time.now()
# user1 = input("kiriting")
# ch2 = time.now()
# user2 = input("Kiriting")
# print(ch1-ch2)

# t1 = '18:32'
# t2 = '18:13'

# def clock(c):
#     s = "22:30"
#     r = int(input("kiriting : "))
#     return f"{}"


# time_1 = input("kiriting").split(":")
# time_2 = input("kiriting").split(":")



# user = input("KIRTING ").split("-")
# def css_find(code):
#     r = f"{code[0]}"
#     for i in range(len(code)):
#         if i:
#             r+=code[i].title()
#     return r
# print(css_find(user))

import random

def get_random_nums(froms,to,counts):
    nums = list(range(froms,to))
    return random.sample(nums,counts)
print(get_random_nums(1,50,10))

