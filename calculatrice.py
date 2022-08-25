from email import message
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

fenetre=Tk()

fenetre.title("Calculatrice")

e=Entry(fenetre,font=("Helvetica",20),bd=5)
e.pack(padx=10,pady=10)

frame_1=Frame(fenetre,bg='white')
buton_7=Button(frame_1,text='7',padx=40,pady=20,command=lambda:button_click('7')).pack(side=LEFT)
buton_8=Button(frame_1,text='8',padx=40,pady=20,command=lambda:button_click('8')).pack(side=LEFT)
buton_9=Button(frame_1,text='9',padx=40,pady=20,command=lambda:button_click('9')).pack(side=LEFT)
buton_fois=Button(frame_1,text='X',padx=40,pady=20,command=lambda:button_click('*')).pack(side=LEFT)
frame_1.pack()

frame_2=Frame(fenetre,bg='white')
buton_4=Button(frame_2,text='4',padx=40,pady=20,command=lambda:button_click('4')).pack(side=LEFT)
buton_5=Button(frame_2,text='5',padx=40,pady=20,command=lambda:button_click('5')).pack(side=LEFT)
buton_6=Button(frame_2,text='6',padx=40,pady=20,command=lambda:button_click('6')).pack(side=LEFT)
buton_moins=Button(frame_2,text='-',padx=40,pady=20,command=lambda:button_click('-')).pack(side=LEFT)
frame_2.pack()

frame_3=Frame(fenetre,bg='white')
buton_1=Button(frame_3,text='1',padx=40,pady=20,command=lambda:button_click('1')).pack(side=LEFT)
buton_2=Button(frame_3,text='2',padx=40,pady=20,command=lambda:button_click('2')).pack(side=LEFT)
buton_3=Button(frame_3,text='3',padx=40,pady=20,command=lambda:button_click('3')).pack(side=LEFT)
buton_plus=Button(frame_3,text='+',padx=40,pady=20,command=lambda:button_click('+')).pack(side=LEFT)
frame_3.pack()

frame_4=Frame(fenetre,bg='white')
buton_div=Button(frame_4,text='/',padx=40,pady=20,command=lambda:button_click('/')).pack(side=LEFT)
buton_0=Button(frame_4,text='0',padx=40,pady=20,command=lambda:button_click('0')).pack(side=LEFT)
buton_c=Button(frame_4,text='C',padx=40,pady=20,command=lambda:delete_value()).pack(side=LEFT)
buton_egal=Button(frame_4,text='=',padx=40,pady=20,command=lambda:equal()).pack(side=LEFT)
frame_4.pack()

fenetre.mainloop()