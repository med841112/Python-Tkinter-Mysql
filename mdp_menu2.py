from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from subprocess import call
import tkinter
from cProfile import label
from tkcalendar import *

class acceuil():
        def __init__(self):

                #Ma fenetre
                self.root = Tk()
                self.root.title("MDPSOFT 1.0")
                self.root.geometry("400x300+600+350")
##              self.root.iconphoto(False, tk.PhotoImage(file='MDPICONE.png'))
                self.root.resizable(False, False)
                self.root.configure(background="#091821")
                #Ajouter le titre
                lbltitre = Label(self.root, borderwidth = 3, relief = SUNKEN
                                 , text= "Acceuil MDPSOFT", font=("Sans Serif", 25), background = "#091821", fg="white")
                lbltitre.place(x=0, y=0, width = 400)
                #Bouton CLIENT
                btnclient = Button(self.root, text="CLIENT", font=("Arial", 16), bg="#FF4500", fg="white", command=self.client)
                btnclient.place(x=100, y=130, width=200)
                #Bouton VENTE
                btnvente = Button(self.root, text="VENTE", font=("Arial", 16), bg="#FF4500", fg="white", command=self.vente )
                btnvente.place(x=100, y=180, width=200)
                self.root.mainloop()

                #Fonction choisir bouton
        def client(self):
                self.root.destroy()
                fen_client()

        def vente(self):
                self.root.destroy()
                fen_vente()

def fen_client(): # Fenetre ajout clients

        # Bouton retour
        def Retour():
            root.destroy()
            acceuil()
        
        def maj(ligne):
            trv.delete(*trv.get_children())
            for i in ligne:
                trv.insert("", "end", values=i)

        def recherche():
            q2 = q.get()
            requete = "select id, nom, tel from client where nom like '%"+q2+"%' or tel like '%"+q2+"%'"
            cursor.execute(requete)
            ligne = cursor.fetchall()
            if ligne == []:
                    messagebox.showinfo(message="Ce client n'existe pas...")
            else:    
                    maj(ligne)
        def effacer():
            requete= "select * from client"
            cursor.execute(requete)
            ligne=cursor.fetchall()
            maj(ligne)

        def getrow(event):
            rowid = trv.identify_row(event.y)
            item = trv.item(trv.focus())
            t1.set(item['values'][0])
            t2.set(item['values'][1])
            t3.set(item['values'][2])


        def maj_client():
            nnom = t2.get()
            tel = t3.get()
            idcli = t1.get()

            if messagebox.askyesno(" Confirmer SVP", "Etes-vous sure de Vouloir mettre a jour cet enregistrement?"):
               requete = "update client set nom = %s, tel = %s where id = %s"
               cursor.execute(requete, (nnom, tel, idcli))
               mabd.commit()
               effacer()
            else:
                return True

        def ajout_client():
            nnom = t2.get()
            tel = t3.get()
            requete = "select id, nom, tel from client where tel like '%"+tel+"%'"
            cursor.execute(requete)
            ligne = cursor.fetchall()
            if ligne == []:
                    requete = "insert into client(id, nom, tel) values(null,%s, %s)"
                    cursor.execute(requete, (nnom, tel))
                    mabd.commit()
                    messagebox.showinfo(title="Ajout client", message="Client Ajouté avec Succés")
                    effacer()    
            else:    
            
                    messagebox.showinfo("ATTENTION!!!", message="Ce Numéro existe déja veuillez chosir un autre...")

        def supp_client():
            id_client = t1.get()
            if messagebox.askyesno("Confirmer la Suppression?", "Etes-vous sure de vouloir supprimer cet ennregistrement?"):
              requete = "delete from client where id = "+id_client
              cursor.execute(requete)
              mabd.commit()
              effacer()
            else:
                return True

        def reinitialiser():
##           ent1.delete(0, END)
           ent2.delete(0, END)
           ent3.delete(0, END)   
              

        root = Tk()
        q= StringVar()
        t1 = StringVar()
        t2 = StringVar()
        t3 = StringVar()
        emball1 = LabelFrame(root, text="Liste Clients")
        emball2 = LabelFrame(root, text="Recherche Clients")
        emball3 = LabelFrame(root, text="Donnees Clients")

        emball1.pack(fill="both", expand="yes", padx=20, pady=10)
        emball2.pack(fill="both", expand="yes", padx=20, pady=10)
        emball3.pack(fill="both", expand="yes", padx=20, pady=10)

        trv = ttk.Treeview(emball1, columns=(1,2,3), show="headings", height="6")
        trv.pack()

        trv.heading(1, text= "ID Client")
        trv.heading(2, text= "Nom")
        trv.heading(3, text= "Telephone")

        trv.column(1, width=80, anchor=tk.CENTER)
        trv.column(2, width=150, anchor=tk.CENTER)
        trv.column(3, width=80, anchor=tk.CENTER)

        trv.bind('<Double 1>', getrow)

        mabd = mysql.connector.connect(host="localhost", user="root", password="Passer@1", database="applimdp", auth_plugin='mysql_native_password')

        cursor = mabd.cursor()

        requete = "select id, nom, tel from client"
        cursor.execute(requete)
        ligne = cursor.fetchall()
        maj(ligne)

        # Section Recherche
        lbl = Label(emball2, text="Recherche")
        lbl.pack(side=tk.LEFT, padx=10)
        ent = Entry(emball2, textvariable=q)
        ent.pack(side=tk.LEFT, padx=6)
        btn = Button(emball2, text="Rechercher", font=("Arial", 9), bg="#FF4500", fg="white",command=recherche)
        btn.pack(side=tk.LEFT, padx=6)
        cbtn = Button(emball2, text="Effacer", font=("Arial", 9), bg="#FF4500", fg="white",command=effacer)
        cbtn.pack(side=tk.LEFT, padx=6)

        #Section Donnees Clients
##        lbl1 = Label(emball3, text="ID Client")
##        lbl1.grid(row=0, column=0, padx=5, pady=3)
##        ent1 = Entry(emball3, textvariable=t1)
##        ent1.grid(row=0, column=1, padx=5, pady=3)

        lbl2 = Label(emball3, text="Nom")
        lbl2.grid(row=1, column=0, padx=5, pady=3)
        ent2 = Entry(emball3, textvariable=t2)
        ent2.grid(row=1, column=1, padx=5, pady=3)

        lbl3 = Label(emball3, text="Telephone")
        lbl3.grid(row=2, column=0, padx=5, pady=3)
        ent3 = Entry(emball3, textvariable=t3)
        ent3.grid(row=2, column=1, padx=5, pady=3)

##        img1 = PhotoImage(file="ICONEMDP.png")
##        img2 = img1.subsample(2, 2)
##        lbl4 =Label(emball3)
##        lbl4.grid(row = 4, column = 5 , columnspan = 2, rowspan = 5, padx = 5, pady = 5)

        maj_btn = Button(emball3, text="MAJ", font=("Arial", 9), bg="#FF4500", fg="white", command=maj_client)
        ajout_btn = Button(emball3, text="Ajouter", font=("Arial", 9), bg="#FF4500", fg="white",command=ajout_client)
        supp_btn = Button(emball3, text="Supprimer", font=("Arial", 9), bg="#FF4500", fg="white",command=supp_client)
        reinit_btn = Button(emball3, text="Reinitialiser", font=("Arial", 9), bg="#FF4500", fg="white",command=reinitialiser)
        retour_btn = Button(root, text="Retour", font=("Arial", 9), bg="#FF4500", fg="white",command=Retour)

        ajout_btn.grid(row=4,column=0, padx=5, pady=3)
        maj_btn.grid(row=4,column=1, padx=5, pady=3)
        supp_btn.grid(row=4,column=2, padx=5, pady=3)
        reinit_btn.grid(row=4, column=3, padx=5, pady=3)

        retour_btn.pack()

        root.title("MDPSOFT 1.0 ")
        root.geometry("800x700")
##        root.iconphoto(False, tk.PhotoImage(file='MDPICONE.png'))
        root.configure(background="#808080")
        root.mainloop()

def fen_vente(): #fenetre gestion des ventes(factures)
        
        # Bouton retour
        def Retour():
            root.destroy()
            acceuil()

        def maj(ligne):
            trv.delete(*trv.get_children())
            for i in ligne:
                trv.insert("", "end", values=i)

        def recherche():
            q2 = q.get()
            requete = "select id, client, qte, prix, somme, versement, reste, date from facture where client like '%"+q2+"%' or id like '%"+q2+"%'" 
            cursor.execute(requete)
            ligne = cursor.fetchall()
            if ligne==[]:
                    messagebox.showinfo(message="Ce client n'a pas de facture...")
            else:    
                    maj(ligne)

        def effacer():
            requete= "select * from facture"
            cursor.execute(requete)
            ligne=cursor.fetchall()
            maj(ligne)

        def getrow(event):
            rowid = trv.identify_row(event.y)
            item = trv.item(trv.focus())
            t1.set(item['values'][0])
            t2.set(item['values'][1])
            t3.set(item['values'][2])
            t4.set(item['values'][3])
            t5.set(item['values'][4])
            t6.set(item['values'][5])
            t7.set(item['values'][6])
            t8.set(item['values'][7])


        def maj_facture():
            idfact = t1.get()
            cclient = t2.get()
            qqte = t3.get()
            pprix = t4.get()
            ssomme = t5.get()
            vversement = t6.get()
            rreste = t7.get()
            ddate = t8.get()

            if messagebox.askyesno(" Confirmer SVP", "Etes-vous sure de Vouloir mettre a jour cet enregistrement?"):
               requete = "update facture set  client = %s, qte = %s, prix = %s, somme = %s, versement = %s, reste = %s, date = %s where id = %s"
               cursor.execute(requete, (cclient, qqte, pprix, ssomme, vversement, rreste, ddate, idfact))
               mabd.commit()
               effacer()
            else:
                return True

        def ajout_facture():
            id = t1.get()
            cclient = t2.get()
            qqte = t3.get()
            pprix = t4.get()
            ssomme = t5.get()
            vversement = t6.get()
            rreste = t7.get()
            ddate = t8.get()
            requete = "insert into facture(client, qte, prix, somme, versement, reste, date) values(%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(requete, (cclient, qqte, pprix, ssomme, vversement, rreste, ddate))
            mabd.commit()
            messagebox.showinfo(title="Ajout Facture", message="Facture Ajoutée avec Succés")
            effacer()

        def supp_facture():
            id_facture = t1.get()
            if messagebox.askyesno("Confirmer la Suppression?", "Etes-vous sure de vouloir supprimer cet ennregistrement?"):
              requete = "delete from facture where id = "+id_facture
              cursor.execute(requete)
              mabd.commit()
              effacer()
            else:
                return True

        def reinitialiser():
           #ent1.delete(0, END)
           ent2.delete(0, END)
           ent3.delete(0, END)
           ent4.delete(0, END)
           ent5.delete(0, END)
           ent6.delete(0, END)
           ent7.delete(0, END)
           ent8 = DateEntry(emball3, date_pattern="dd/mm/yy", textvariable=t8, state= 'readonly', width=17)

        def calculer():
           id = t1.get()
           cclient = t2.get()
           qqte = int(t3.get())
           pprix = int(t4.get())
           ssomme = (t5.get())
           vversement = t6.get()
           rreste = t7.get()
          # oobservation = t8.get()
           total = (qqte*pprix)
           t5.set(str(total))

        def reste():
           ssomme = int(t5.get())
           vversement = int(t6.get())
           rreste = (t7.get())
          # oobservation = t8.get()
           total =(ssomme) - (vversement)
           t7.set(str(total))
        
      
        mabd = mysql.connector.connect(host="localhost", user="root", password="Passer@1", database="applimdp", auth_plugin='mysql_native_password')

        cursor = mabd.cursor()

        root = Tk()
        q= StringVar()
        t1 = StringVar()
        t2 = StringVar()
        t3 = StringVar()
        t4 = StringVar()
        t5 = StringVar()
        t6 = StringVar()
        t7 = StringVar()
        t8 = StringVar()

        emball1 = LabelFrame(root, text="Liste Factures")
        emball2 = LabelFrame(root, text="Recherche Facture")
        emball3 = LabelFrame(root, text="Donnees Clients Facturés")

        emball1.pack(fill="both", expand="yes", padx=20, pady=10)
        emball2.pack(fill="both", expand="yes", padx=20, pady=10)
        emball3.pack(fill="both", expand="yes", padx=20, pady=10)

        trv = ttk.Treeview(emball1, columns=(1,2,3,4,5,6,7,8), show="headings", height="6")
        trv.pack()

        trv.heading(1, text= "ID Facture")
        trv.heading(2, text= "Client")
        trv.heading(3, text= "Quantité")
        trv.heading(4, text= "Prix")
        trv.heading(5, text= "Somme")
        trv.heading(6, text= "Versement")
        trv.heading(7, text= "Reste")
        trv.heading(8, text= "Date")

        trv.column(1, width=80, anchor=tk.CENTER)
        trv.column(2, width=150, anchor=tk.CENTER)
        trv.column(3, width=80, anchor=tk.CENTER)
        trv.column(4, width=50, anchor=tk.CENTER)
        trv.column(5, width=100, anchor=tk.CENTER)
        trv.column(6, width=100, anchor=tk.CENTER)
        trv.column(7, width=80, anchor=tk.CENTER)
        trv.column(8, width=80, anchor=tk.CENTER)

        trv.bind('<Double 1>', getrow)

        requete = "select id, client, qte, prix, somme, versement, reste, date from facture"
        cursor.execute(requete)
        ligne = cursor.fetchall()
        maj(ligne)

        reqcombo = " select distinct(nom) as nom from client" # liste deroulante champ client
        reqresult = cursor.execute(reqcombo)
        listereq=cursor.fetchall()
        listecombo=[r for r, in listereq]
        
        # Section Recherche Facture
        lbl = Label(emball2, text="Recherche")
        lbl.pack(side=tk.LEFT, padx=10)
        ent = Entry(emball2, textvariable=q)
        ent.pack(side=tk.LEFT, padx=6)
        btn = Button(emball2, text="Rechercher", font=("Arial", 9), bg="#FF4500", fg="white",command=recherche)
        btn.pack(side=tk.LEFT, padx=6)
        cbtn = Button(emball2, text="Effacer", font=("Arial", 9), bg="#FF4500", fg="white",command=effacer)
        cbtn.pack(side=tk.LEFT, padx=6)

        #Section Donnees facturation 
##        lbl1 = Label(emball3, text="ID Facture")
##        lbl1.grid(row=0, column=0, padx=5, pady=3)
##        ent1 = Entry(emball3, textvariable=t1)
##        ent1.grid(row=0, column=1, padx=5, pady=3)

        lbl2 = Label(emball3, text="Client")
        lbl2.grid(row=1, column=0, padx=5, pady=3)
        ent2 = ttk.Combobox(emball3, values=listecombo, textvariable=t2, width=17)
        ent2.grid(row=1, column=1, padx=5, pady=3)
        ent2.current()

        lbl3 = Label(emball3, text="Quantité")
        lbl3.grid(row=2, column=0, padx=5, pady=3)
        ent3 = Entry(emball3, textvariable=t3)
        ent3.grid(row=2, column=1, padx=5, pady=3)

        lbl4 = Label(emball3, text="Prix")
        lbl4.grid(row=3, column=0, padx=5, pady=3)
        ent4 = Entry(emball3, textvariable=t4)
        ent4.grid(row=3, column=1, padx=5, pady=3)

        lbl5 = Label(emball3, text="Somme")
        lbl5.grid(row=4, column=0, padx=5, pady=3)
        ent5 = Entry(emball3, textvariable=t5)
        ent5.grid(row=4, column=1, padx=5, pady=3)

        lbl6 = Label(emball3, text="Versement")
        lbl6.grid(row=5, column=0, padx=5, pady=3)
        ent6 = Entry(emball3, textvariable=t6)
        ent6.grid(row=5, column=1, padx=5, pady=3)

        lbl7 = Label(emball3, text="Reste")
        lbl7.grid(row=6, column=0, padx=5, pady=3)
        ent7 = Entry(emball3, textvariable=t7)
        ent7.grid(row=6, column=1, padx=5, pady=3)

        lbl8 = Label(emball3, text="Date")
        lbl8.grid(row=7, column=0, padx=5, pady=3)
        ent8 = DateEntry(emball3, date_pattern="dd/mm/yy", textvariable=t8, state= 'readonly', width=17)
        ent8.grid(row=7, column=1, padx=5, pady=3)
        

        maj_btn = Button(emball3, text="MAJ", font=("Arial", 9), bg="#FF4500",fg="white", command=maj_facture)
        ajout_btn = Button(emball3, text="Ajouter", font=("Arial", 9), bg="#FF4500", fg="white", command=ajout_facture)
        supp_btn = Button(emball3, text="Supprimer", font=("Arial", 9), bg="#FF4500", fg="white",command=supp_facture)
        reinit_btn = Button(emball3, text="Reinitialiser", font=("Arial", 9), bg="#FF4500", fg="white",command=reinitialiser)
        retour_btn = Button(root, text="Retour", font=("Arial", 9), bg="#FF4500", fg="white",command=Retour)
        calculer_btn = Button(emball3, text="Calculer", font=("Arial", 9), bg="#FF4500",fg="white", command=calculer)
        reste_btn = Button(emball3, text="Reste", font=("Arial", 9), bg="#FF4500",fg="white", command=reste)
  

        ajout_btn.grid(row=9,column=0, padx=5, pady=3)
        maj_btn.grid(row=9,column=1, padx=5, pady=3)
        supp_btn.grid(row=9,column=2, padx=5, pady=3)
        reinit_btn.grid(row=9, column=3, padx=5, pady=3)
        calculer_btn.grid(row=4, column=2, padx=5, pady=3)
        reste_btn.grid(row=6, column=2, padx=5, pady=3)

        retour_btn.pack() # bouton retour

        root.title("MDPSOFT_vente")
        root.geometry("800x700")
##        root.iconphoto(False, tk.PhotoImage(file='MDPICONE.png'))
        root.resizable(False, False)
        root.configure(bg="#808080")
        root.mainloop()

s = acceuil()

