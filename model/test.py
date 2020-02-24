from tkinter import *
import time
# windows ------------
fenetre = Tk()
# ----Label----
fenetre.geometry('900x800')
fenetre.title('formulaire d\'enregistrement')
heading =Label(text="Page de connection",bg="grey",fg="black",width=500,height=3)
heading.pack()

# les données de du formulaire
url =Label(text="Enregistrez-vous", font=('bold', 24))
nom = Label(fenetre, text='nom', font=('bold', 14), pady=5)
prenom = Label(fenetre, text='prenom', font=('bold', 14), pady=5)
user = Label(fenetre, text='user', font=('bold', 14), pady=5)
password = Label(fenetre, text='password', font=('bold', 14), pady=5)
url.place(x=10,y=70)
nom.place(x=10,y=130)
prenom.place(x=10,y=190)
user.place(x=10,y=250)
password.place(x=10,y=310)

# fonction de definition de chaine de caratere
nom= StringVar()
prenom =StringVar()
user =StringVar()
password =StringVar()

# partie de  saisi de données
nom_entre= Entry(textvariable=nom,width='50')
prenom_entre= Entry(textvariable=prenom,width='50')
user_entre= Entry(textvariable=user,width='50')
password_entre= Entry(textvariable=password  ,width='50')
nom_entre.place(x=10,y=160)
prenom_entre.place(x=10,y=220)
user_entre.place(x=10,y=280)
password_entre.place(x=11,y=340)

# ----buttom-----pi
bouton2 = Button(text="connecter", font="2em", command='verifier')
quiter = Button(text="quiter", command="exit", font="2em")
bouton2.place(x=0,y=380)
quiter.place(x=200,y=380)

# --- call of main fonction--
fenetre.mainloop()



