from tkinter import *
import webbrowser


def overture_du_navigateur():
    mon_domaine=input.get()
    if mon_domaine=="":
        label['text']='Votre formulaire est vide !'
    elif len(mon_domaine)<10:
        label['text']='Votre nom de domaine est invalide !'
    else:
        webbrowser.open("https:"+mon_domaine)

fenetre=Tk()

# je configure ma fenetre graphique
# definie ma couleur de fond pour la fenetre et le reste des composants
background="#41B77E"
# definie ma couleur du texte pour les composants
fg="white"

fenetre.title("Ouverture du navigateur")
fenetre.geometry("720x580")
fenetre.config(background=background)

# je creer mon label
label=Label(fenetre,text="Entrer le nom de domaine",font=('Helvetica',20),bg=background,fg="white")
label.pack()
# je creer mon label2
label2=Label(fenetre,text="Ex: www.google.com",font=('Helvetica',15),bg=background,fg="yellow")
label2.pack()

# je cree mon input
input=Entry(fenetre,font=('Helvetica',30),bg=background,fg="white")
input.pack(pady=12)

# je cree ma frame (une boite qui contiendra mes boutons)
frame_1=Frame(fenetre,bg='white')

buton_pass=Button(frame_1,text='Ouvrir',padx=40,pady=20,command=overture_du_navigateur).pack()

frame_1.pack()

fenetre.mainloop()