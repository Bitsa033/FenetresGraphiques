from random import choice
from tkinter import *

def mot_de_passe():
    chaine1='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    chaine2='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chaine3='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    nombre1='0123456789'
    nombre2='102030405060708090'
    nombre3='100101102103104105106107108109'
    caractere1='+-=/.;...&#@!()_]{[}?/<>"|'
    caractere2=',\~+-=/.;...&#@!()_]{[}?/<>"|'
    input.delete(0,END)
    input.insert(0,choice(chaine1)+choice(chaine2)+choice(nombre1)+
    choice(caractere1)+choice(chaine3)+choice(nombre2)+choice(nombre3)+choice(caractere2)
    )


fenetre=Tk()

# je configure ma fenetre graphique
# definie ma couleur de fond pour la fenetre et le reste des composants
background="#41B77E"
# definie ma couleur du texte pour les composants
fg="white"

fenetre.title("Generateur de mot de passe")
fenetre.geometry("720x580")
fenetre.config(background=background)

# je creer mon label
label=Label(fenetre,text="Mot de passe",font=('Helvetica',30),bg=background,fg="white")
label.pack()

# je cree mon input
input=Entry(fenetre,font=('Helvetica',30),bg=background,fg="white")
input.pack(pady=12)

# je cree ma frame (une boite qui contiendra mes boutons)
frame_1=Frame(fenetre,bg='white')
buton_pass=Button(frame_1,text='Generer',padx=40,pady=20,command=lambda:mot_de_passe()).pack(side=LEFT)
buton_pass=Button(frame_1,text='Effacer',padx=40,pady=20,command=lambda:input.delete(0,END)).pack(side=LEFT)
buton_pass=Button(frame_1,text='Eneregistrer',padx=40,pady=20).pack(side=LEFT)

frame_1.pack()

# je creer mon label2
# label2=Label(fenetre,font=('Helvetica',15),bg=background,fg="white")
# label2.pack()


fenetre.mainloop()