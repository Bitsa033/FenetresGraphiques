from ctypes.wintypes import SIZE
from sqlite3 import Date
from sre_compile import isstring
from tkinter import *
from math import factorial

def overture_du_navigateur():
    n=int(input.get())
    date=Date(2022,8,5)
    if len(str(n))>3:
        input2.delete(0,END)
        label3['text']="Votre age est invalide "
    elif n<1:
        input2.delete(0,END)
        label3['text']="l'age ne doit pas etre inferieur à 0 "
    else:
        label3['text']="Date de naissance"
        input2.delete(0,END)
        input2.insert(0,date.year-n)

fenetre=Tk()

# je configure ma fenetre graphique
# definie ma couleur de fond pour la fenetre et le reste des composants
background="#41B77E"
# definie ma couleur du texte pour les composants
fg="white"

fenetre.title("Date de naissance")
fenetre.geometry("720x580")
fenetre.config(background=background)

# je creer mon label
label=Label(fenetre,text="Entrer l'age",font=('Helvetica',30),bg=background,fg="white")
label.pack()
# je creer mon label2
label2=Label(fenetre,text="Ex: 13",font=('Helvetica',15),bg=background,fg="yellow")
label2.pack()

# je cree mon input
input=Entry(fenetre,font=('Helvetica',30),bg=background,fg="white")
input.pack(pady=12)
# je creer mon label2
label3=Label(fenetre,text="Date de naisssance",font=('Helvetica',15),bg=background,fg="yellow")
label3.pack()
# je cree mon input2
input2=Entry(fenetre,font=('Helvetica',30),bg=background,fg="white")
input2.pack(pady=12)

# je cree ma frame (une boite qui contiendra mes boutons)
frame_1=Frame(fenetre,bg='white')

buton_pass=Button(frame_1,text='Calculer',padx=40,pady=20,command=overture_du_navigateur).pack(side=LEFT)
buton_pass=Button(frame_1,text='Effacer',padx=40,pady=20,command=lambda:input.delete(0,END)).pack(side=LEFT)
buton_pass=Button(frame_1,text='Enregistrer',padx=40,pady=20).pack(side=LEFT)

frame_1.pack()

fenetre.mainloop()