# n=int(input("Kerakli summani kiriting = "))
# if n<12:
#     s=n*10.5
#     print(f"{s} rubl ")
# elif n<144:
#     s=(n//12)*102.5+(n%12)*10.5
#     print(f"{s} rubl")
# else:
#     s1 = n // 144
#     s2 = (n-144*s1) // 12
#     s3 = n - 144 * s1 - 12 * C
#     s = s1 * 1140 + s2 * 102.5 + s3 * 10.5
#     print(f"{s} rubl")
from tkinter import Tk, Label, Button
import time


app_window = Tk()
app_window.title("Mening soatim")
app_window.geometry("420x150")
app_window.resizable(1,1)


text_font = ("RoadTest", 68, 'bold')
background = "#f2e750"
foreground = "#363529"
border_with = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_with) 
label.grid(row=0, column=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)
    
digital_clock()
app_window.mainloop()
# Paypoqni Juftni 10 руб. 50 коп
# Boglam (12 juft) narxi 102 руб. 50 коп.
# Quti (12 boglam) narxi 1140 руб.

# User kiritgan juft ga qarab narxini chiqarib bering