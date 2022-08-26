from math import factorial,exp
from tkinter import *

def button_click(number):

    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+ str(number))

def delete_value():

    e.delete(0,END)

def equal():

    number=e.get()
    e.delete(0,END)
    e.insert(0,eval(number))

def factoriel():
    n=int(e.get())
    e.delete(0,END)
    e.insert(0,factorial(n))

def exponentiel():
    n=int(e.get())
    e.delete(0,END)
    e.insert(0,exp(n))

fenetre=Tk()

fenetre.title("Calculatrice")
fenetre.config(bg='#41B77E')

e=Entry(fenetre,font=("Helvetica",20),bd=5)
e.pack(padx=20,pady=10)

frame_0=Frame(fenetre,bg='white')
buton_fact=Button(frame_0,text='F',bg='#41B77E',padx=40,pady=20,command=lambda:factoriel()).pack(side=LEFT)
buton_exp=Button(frame_0,text='E',bg='#41B77E',padx=40,pady=20,command=lambda:exponentiel()).pack(side=LEFT)
buton_c=Button(frame_0,text='C',bg='#41B77E',padx=40,pady=20,command=lambda:delete_value()).pack(side=LEFT)
buton_div=Button(frame_0,text='/',bg='#41B77E',padx=40,pady=20,command=lambda:button_click('/')).pack(side=LEFT)
frame_0.pack()

frame_1=Frame(fenetre,bg='white')
buton_7=Button(frame_1,text='7',bg='#41B77E',padx=40,pady=20,command=lambda:button_click('7')).pack(side=LEFT)
buton_8=Button(frame_1,text='8',bg='#41B77E',padx=40,pady=20,command=lambda:button_click('8')).pack(side=LEFT)
buton_9=Button(frame_1,text='9',bg='#41B77E',padx=40,pady=20,command=lambda:button_click('9')).pack(side=LEFT)
buton_fois=Button(frame_1,text='X',bg='#41B77E',padx=40,pady=20,command=lambda:button_click('*')).pack(side=LEFT)
frame_1.pack()

frame_2=Frame(fenetre,bg='white')
buton_4=Button(frame_2,text='4',bg='#41B77E',padx=40,pady=20,command=lambda:button_click('4')).pack(side=LEFT)
buton_5=Button(frame_2,text='5',bg='#41B77E',padx=40,pady=20,command=lambda:button_click('5')).pack(side=LEFT)
buton_6=Button(frame_2,text='6',bg='#41B77E',padx=40,pady=20,command=lambda:button_click('6')).pack(side=LEFT)
buton_moins=Button(frame_2,text='-',bg='#41B77E',padx=40,pady=20,command=lambda:button_click('-')).pack(side=LEFT)
frame_2.pack()

frame_3=Frame(fenetre,bg='white')
buton_1=Button(frame_3,text='1',bg='#41B77E',padx=40,pady=20,command=lambda:button_click('1')).pack(side=LEFT)
buton_2=Button(frame_3,text='2',bg='#41B77E',padx=40,pady=20,command=lambda:button_click('2')).pack(side=LEFT)
buton_3=Button(frame_3,text='3',bg='#41B77E',padx=40,pady=20,command=lambda:button_click('3')).pack(side=LEFT)
buton_plus=Button(frame_3,text='+',bg='#41B77E',padx=40,pady=20,command=lambda:button_click('+')).pack(side=LEFT)
frame_3.pack()

frame_4=Frame(fenetre,bg='white')
buton_pm=Button(frame_4,text='+/-',bg='#41B77E',padx=40,pady=20,command=lambda:button_click('-')).pack(side=LEFT)
buton_0=Button(frame_4,text='0',bg='#41B77E',padx=40,pady=20,command=lambda:button_click('0')).pack(side=LEFT)
buton_c=Button(frame_4,text=',',bg='#41B77E',padx=40,pady=20,command=lambda:button_click('.')).pack(side=LEFT)
buton_egal=Button(frame_4,text='=',bg='#41B77E',padx=40,pady=20,command=lambda:equal()).pack(side=LEFT)

frame_4.pack()

fenetre.mainloop()