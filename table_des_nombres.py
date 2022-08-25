from tkinter import *

def addition():
    nombre=int(input.get())
    label['text']=" "
    label2['text']=" "

    mon_message="Table de " + str(nombre)
    label['text']=label['text'] + " " + str(mon_message)
    for i in range(0,13):
        
        label2['text']=label2['text'] + " " + str(nombre) + " + " + str(i) + " = " + str(nombre+i)  + "\n"

def sosustraction():
    nombre=int(input.get())
    label['text']=" "
    label2['text']=" "

    mon_message="Table de " + str(nombre)
    label['text']=label['text'] + " " + str(mon_message)
    for i in range(0,13):
        
        label2['text']=label2['text'] + " " + str(nombre) + " - " + str(i) + " = " + str(nombre-i)  + "\n"

def multiplication():
    nombre=int(input.get())
    label['text']=" "
    label2['text']=" "

    mon_message="Table de " + str(nombre)
    label['text']=label['text'] + " " + str(mon_message)
    for i in range(0,13):
        
        label2['text']=label2['text'] + " " + str(nombre) + " X " + str(i) + " = " + str(nombre*i)  + "\n"

def division():
    nombre=int(input.get())
    label['text']=" "
    label2['text']=" "

    mon_message="Table de " + str(nombre)
    label['text']=label['text'] + " " + str(mon_message)
    for i in range(1,13):
        
        label2['text']=label2['text'] + " " + str(nombre) + " / " + str(i) + " = " + str(nombre/i)  + "\n"
    

fenetre=Tk()

# je configure ma fenetre graphique
# definie ma couleur de fond pour la fenetre et le reste des composants
background="#41B77E"
# definie ma couleur du texte pour les composants
fg="white"

fenetre.title("Table des nombres")
fenetre.geometry("720x580")
fenetre.config(background=background)

# je creer mon label
label=Label(fenetre,text="Entrer le nombre",font=('Helvetica',30),bg=background,fg="white")
label.pack()

# je cree mon input
input=Entry(fenetre,font=('Helvetica',30),bg=background,fg="white")
input.pack(pady=12)

# je cree ma frame (une boite qui contiendra mes boutons)
frame_1=Frame(fenetre,bg='white')
buton_plus=Button(frame_1,text='+',padx=40,pady=20,command=lambda:addition()).pack(side=LEFT)
buton_moins=Button(frame_1,text='-',padx=40,pady=20,command=lambda:sosustraction()).pack(side=LEFT)
buton_fois=Button(frame_1,text='X',padx=40,pady=20,command=lambda:multiplication()).pack(side=LEFT)
buton_div=Button(frame_1,text='/',padx=40,pady=20,command=lambda:division()).pack(side=LEFT)
frame_1.pack()

# je creer mon label2
label2=Label(fenetre,font=('Helvetica',15),bg=background,fg="white")
label2.pack()


fenetre.mainloop()