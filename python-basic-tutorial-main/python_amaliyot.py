# # ro'yhatlar bilan ishlash amaliyot
# nick_name = ["Ahmat", "Zizi", "samancha", "fonarchi ota", "chuppi", "jambil","boboy", "tico"] # Ro'yhat yarating
# print(len(nick_name)) # Ro'yxat uzunligi
# print(sorted(nick_name)) # Ro'yhaatni saralagan qilib chiqarish
# print(sorted(nick_name, reverse=True)) # Ro'yhatni teskari qilib saralab chiqarish
# print(nick_name) 
# nick_name.reverse() # Ro'yatni asl xolatda teskari qilish 
# print(nick_name)
# nick_name.sort() # Ro'yhatni aslini alifbo tartibida saralash
# print(nick_name)
# nick_name.sort(reverse=True) # Ro'yhat aslini teskari qilib saralash
# print(nick_name)
# nums = list(range(120,1201,2)) # 120 dan 1200 gacha bo'lgan juft sonlar
# print(sum(nums)) # sonlar yigindisi
# print(max(nums)) # ro'yhat ichida eng katta son di consolega chiqarish
# print(min(nums)) # ro'yhat ichida eng kichik son di consolega chiqarish
# print(len(nums)) # sonlar uzunligi
# center = len(nums) // 2
# r = center+20
# print(nums[:20])
# print(nums[-20:-1])
# print(nums[center:r])
# taomlar = []
# for i in range(5):
#     user = input("KIRIT")
#     taomlar.append(user)
# nonushta = taomlar[:]


# For sikliga oid amaliyot
# freinds = ["oyat", "farruh", "mohinur", "samandar", "gulgina",]
# for i in freinds:
#     print(f"Salom {i} yaxshimisiz")
# else:
#     print(f"Kod {len(freinds)} marta takroralandi")

# k = [i**3 for i in range(9,101,2) ]

# print(k)

# films = []
# for i in range(5):
#     user = input("kiriting")
#     films.append(user)

# user = int(input("Bugun nechta odam bilan uchrashdingiz"))
# freinds = []
# for i in range(len(user)):
#     n = input("Uchrashgan odamingizni ismini kiriting")
#     freinds.append(n)
# print(freinds)

# about = {
#     "Ism":'Ali',
#     "Familya":'Valiyev',
#     "Yosh":15,
#     "Hobby":'CS GO or FiFA 2021 and Pyton learning',
#     "Kasbi":'Dasturchi',
#     "Manzili":'Asaka yoli',
#     "Sevgan_qizi":"Gulgina",
#     "Yoqtigan dasturlash tili":"PYTON I love you"
# }

# for k,v in sorted(about.items()):
#     print(f"{k} {v}")
# else:
#     print("ALI VALIYEV HAQIDA LUG'AT")



colors = {"yashil", "oq", "ko'k"} 
colors.add("qora")
colors.update("qizil")
set1 = {10,20,30,40,50}
set2 = {30,70,40,50,50}
sets = set1|set2
print(sets)
print(set1.intersection(set2))