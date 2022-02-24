import time
import calendar
import datetime
import locale
locale.setlocale(locale.LC_ALL, "uz_Latn_UZ")
# t = time.time() # 1970 dan hozirgi kungacha qancha sekund otganini aniqlaydi
# t = time.gmtime()
# print(t.tm_year)

# t = time.localtime() #Yil oy bla bla bugungi sana
# print(type(t))
# print(t)

# y = t[0]
# m = t[1]
# d = t[2]
# h = t[3]
# mi = t[4]
# print(f"bugun : {y}:{m}:{d} soat : {h}:{mi}")
# dt = datetime.datetime.now()
# print(dt.year)
# print(dt.month)
# print(dt.day)
# print(dt.hour)
# print(dt.seconde)
# print(dt.minute)


# dt = datetime.datetime.now()
# print(dt.hour - 2 ,":" ,dt.minute)

# l = time.localtime()
# print(l[3] - 2, ":", l[4])

# %a hafta kunining qisqartirilgan nomi.

# %A hafta kunining toʻliq nomi.

# %b oyning qisqartirilgan nomi.
print("%Y.%B.%c")

# %B toʻliq oy nomi.

# %c tegishli sana va vaqt ko'rinishi.

# %d O'nlik raqam sifatida oyning kuni [01,31].

# %H Soat (24 soatlik soat) kasr soni sifatida [00,23].

# %I Soat (12 soatlik soat) kasr soni sifatida [01,12].

# %j O'nlik raqam sifatida yil kuni [001,366].

# %m Oy kasrli raqam sifatida [01,12].

# %M O'nlik son sifatida daqiqa [00,59].

# %p Mahalliy tilning AM yoki PM ekvivalenti.

# %S Ikkinchi o'nlik raqam sifatida [00,61].

# %U Yilning hafta raqami (haftaning birinchi kuni yakshanba) kasr soni sifatida [00,53]. Birinchi yakshanbadan oldingi yangi yildagi barcha kunlar 0-haftada hisoblanadi.


# %w Hafta kuni kasr soni sifatida [0(yakshanba),6].

# %W Yilning hafta raqami (haftaning birinchi kuni dushanba) kasr soni sifatida [00,53]. Birinchi dushanbadan oldingi yangi yildagi barcha kunlar 0-haftada hisoblanadi.



# %x Mahalliy tilning tegishli sanasi.

# %X Mahalliyning tegishli vaqt ko'rinishi.

# %y O'nlik son sifatida asrsiz yil [00,99].

# %Y O'nlik son sifatida asr bilan yil.

# %z Vaqt mintaqasi ofseti UTC/GMT dan +HHMM yoki -HHMM koʻrinishidagi ijobiy yoki salbiy vaqt farqini koʻrsatadi, bunda H oʻnlik soat raqamlarini, M esa oʻnlik daqiqa raqamlarini ifodalaydi [-23:59, +23:59]. 1

# %Z Vaqt mintaqasi nomi (agar vaqt mintaqasi mavjud bo'lmasa, belgilar yo'q). Eskirgan. 1

#%% Haqiqiy '%'xarakter.#
