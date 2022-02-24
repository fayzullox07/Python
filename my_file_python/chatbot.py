#-*- coding: utf-8 -*-
from re import A


print("Salom meni ismim , R2D2")
name = input("Seni isming nima ?")
print(f"Salom , {name} \n Tanishganimdan hursandman!")
print(f"agar seni 3 yoshli bola chaqirganda ismini {name.upper()} bolar edi")

age = int(input("Yoshing nechada ?"))

if age > 18:
    print( "Katta bolekansan..")
else:
    print("Taxninan tengdosh ekanmiz !")
weight = int(input("Vazning necha kilo ?"))
if weight > 50:
    print("Semiz")
print(f"Agar sen oyda bolganingda vazning {weight // 6}kg bolar edi")
theme = input("Nimalarga qiziqasan: \n Sport, \n IT,\n Matematika,\n Multfilm\n >>>")
if theme == 'sport':
    print("Glory Glory United")
    fc = input("Sen qaysi jamoaga muxlissan")
    if fc == 'barsa':
        messi = input("savol messi qaysi jamoada oynaydi")
        if messi == 'barsa':
            print("Omad barsachi")
    elif fc == 'real':
        print("Gapim yo'q")
elif theme == 'it':
    print("Hello hello small proggrammist") 
    dev = input("sen qaysi biriga qiziqasan \n 1: Frontend Devoloper va 2:Backend Devoloper  ")
    if dev == 'frontend':
        print(f"Sen {dev} ga qiziqsang quyidagi dasturlash tillarini bilishing kerak \n 1. HTML, 2.CSS, 3.JavaScript  va hakozo")
        print("Yana sen shu tilni bilishing yana uni fream worklarini ham bilish kerak masalan:")
        print(" Python the best freamwork::: 1.Django 2.Flask 3.Dash 4.CherryPy 5.Tornado va hokazo")
    elif dev == 'backend':
        print("Senda tanlov yo'q albatta PYTHON dasturlash tilini o'rganishing shart \n keyin men ham pythonda yozilganman")    
        print("Yana sen shu tillarn bilishing yana ularni fream worklarini ham bilish kerak masalan:")
elif theme == 'matematika':
    print(f"Yaxshi shu misolni ishlab ko'rchi: >> 30 + 10 == ???????????")
    A = input("Javoni:  >")
    if A == "40":
        print("You are Victory ")
    else:
        print('Ha bilmasvoy')
        
elif theme == 'multfim':
    m = input("Mulfilmlarni bilsang qani savol:   Tom i jeri da kim kuchli")
    if m == 'jeri':
        print("xa xa senam jeriga oxshaysanmi")
    elif m == 'tom':
        print('Ha tom')
else:
    print("Qiziqishin yaxshi albatta")