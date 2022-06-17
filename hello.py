# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 02:45:23 2022

@author: alper
"""

from tkinter import *
window = Tk()

# Pencere Başlığı
window.title("Vücut Kütle Endeksi")

# Pencereye ikon ekleme
# window.iconbitmap('sm.ico')

window.geometry("390x320")

# Pencerenin yeniden boyutlandırılmasını engelledik
window.resizable(width=False, height=False)


def hesapla():
    
    try:
        hesap=(int(E1.get())*10000)  / ( int(E2.get())*int(E2.get()))
        hesap=round(hesap,2)
        if  hesap<18:
            analize="Zayıf"
        elif hesap<25:
            analize="İdeal kilo"
        elif hesap<30:
            analize="Fazla Kilolu"
        elif hesap<35:
            analize="Şişman 1. Derece obez"
        elif hesap<45:
            analize="Şişman 2. derece Obez"
        else       : analize="Şişman 2. derece Obez"
        
        # lbl["text"] = "Kitle indeksi: "+str(hesap)+" "+analize
        L3["text"]="Kitle indeksi: "+str(hesap)+" "+analize
        
    except:
        lbl["text"] = ("BİRŞEYLER YANLIŞ GİTTİ")




L1 = Label(window, text="Kilo")
L1.place(x=75, y=15)

E1 = Entry(window, width=25)
E1.place(x=77,y=45)

L2 = Label(window, text="Boy")
L2.place(x=75, y=80)

E2 =  Entry(window, width=25)
E2.place(x=77, y=110)

L3 = Label(window, text="Verileri girin")
L3.place(x=75, y=145)

# E3 =  Entry(window, width=25)
# E3.place(x=77, y=175)

bt = Button(window, text="HESAPLA", padx="20",pady="5", command=hesapla)
bt.place(x=75,y=175)

lbl = Label(window)
lbl.pack()

window.mainloop()