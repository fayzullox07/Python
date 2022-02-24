# Exception - Dastur davomida vujudga kelgan xatoliklar haqida bildirishlar
# 1- SyntaxError - dasturda sintaksis xatolik (yozma)
# 2- Mantiqiy - dastur mantigidagi xatolik
# 3- Bajarish vaqtidagi xatoliklar

# try except else finally
# x = 1 / 0
# try:
#     x = 1 / 0
# except ZeroDivisionError as zr:
#     print("Error", zr)
#     x = 0
# print(x)

# n = int(input())
# print(n)
# try:
#     n = int(input())
# except (ValueError, NameError):
#     print("Xatolik...")

# try:
#     n = int(input()) #xattolik bor code
# except ValueError as vr:
#     print("Xatolik", vr)    
# else:
#     print("Xato Yo'q davom etamiz")
# finally:
#     print("Farqi yo ishledi")
    
# print("Davom etadi")


try:
    n = 1 / 0
except:
    raise ZeroDivisionError("1 0 ga bo'linmaydi")


# exceptions.py
# try: # Xatolikni qidiradi
#     x = 1 / 0.5
# except ZeroDivisionError as error: # xato bosa qilinishi kerak bolgan ishlar
#     print(error)
# else: # xato bomasa qilinishi kerak bolgan ishlar
#     print("else Block")
# finally: # har doim qilinishi kerak bolgan ishlar
#     print("Block finally ... every time!")
