import tkinter as tk
import os
import sys
from PIL import Image, ImageTk
from tkinter import messagebox


# Ajouter le chemin de l'image de fond
cheminBGImage = '/Users/mouhamadouyate/Desktop/Gestion de projet Fortune Machine_Bureau/3_Realisation/Codes/Code de la Raspberry/FortuneMachine_CodeRaspberryPI-main/Interface/background.png'

class InterfaceGraphique:
    def __init__(self, printer=None):
        self.root = tk.Tk()
        self.root.title("Choisissez le thème de votre fortune")
        self.root.attributes('-topmost', True)  # Place toujours la fenêtre au premier plan
        self.printer = printer
        self.canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.update_background()

        # Cadre des boutons
        self.button_frame = tk.Frame(self.canvas, bg='white')
        self.button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def update_background(self):
        """Met à jour l'image de fond"""
        bg_image = Image.open(cheminBGImage)
        bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
        bg = ImageTk.PhotoImage(bg_image)
        self.canvas.create_image(0, 0, image=bg, anchor=tk.NW)
        self.canvas.image = bg

    def afficher_message(self, texte):
        """Affiche un message à l'écran"""
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        
        label = tk.Label(self.button_frame, text=texte, font=("Helvetica", 30), bg='white', fg='black', wraplength=800)
        label.pack(pady=20)

        retour_button = tk.Button(self.button_frame, text="Retour", font=("Helvetica", 16), command=self.reinitialiser_interface)
        retour_button.pack(pady=10)

    def demander_impression(self, theme):
        """Demande à l'utilisateur s'il veut imprimer ou afficher"""
        message = self.recuperer_message_api(theme)
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        label = tk.Label(self.button_frame, text="Voulez-vous imprimer la fortune ?", font=("Helvetica", 30), bg='white', fg='black')
        label.pack(pady=20)

        # Bouton Oui
        oui_button = tk.Button(self.button_frame, text="Oui", font=("Helvetica", 16), command=lambda: self.imprimer_fortune(message))
        oui_button.pack(side=tk.LEFT, padx=20)

        # Bouton Non
        non_button = tk.Button(self.button_frame, text="Non", font=("Helvetica", 16), command=lambda: self.afficher_message(message))
        non_button.pack(side=tk.RIGHT, padx=20)

    def afficher_menu(self):
        """Affiche le menu principal avec les thèmes"""
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        themes = ["Amour", "Meteo", "Horoscope", "Santé", "Chance", "Fortune"]
        for i, theme in enumerate(themes):
            button = tk.Button(self.button_frame, text=theme, font=("Helvetica", 16), width=25, height=5,
                             command=lambda t=theme: self.demander_impression(t),
                             bg='white', relief='flat', borderwidth=0,
                             activebackground='#f0f0f0')
            button.grid(row=i // 3, column=i % 3, padx=10, pady=10)

    def imprimer_fortune(self, texte):
        """Imprime la fortune si une imprimante est connectée"""
        if self.printer:
            self.printer.print(texte)
            self.printer.feed(2)
            print(f"Fortune imprimée : {texte}")
            self.afficher_message("Votre fortune a été imprimée avec succès.")
        else:
            self.afficher_message("Aucune imprimante connectée.")

    def recuperer_message_api(self, theme):
        """Simule la récupération d'un message depuis l'API"""
        messages_api = {
            "Amour": "L'amour est la clé de votre bonheur.",
            "Meteo": "Demain, un grand soleil brillera dans votre cœur.",
            "Horoscope": "Les étoiles brillent pour vous aujourd'hui.",
            "Santé": "Prenez soin de vous, vous êtes précieux.",
            "Chance": "Un événement inattendu changera votre vie.",
            "Fortune": "Votre avenir est rempli de succès."
        }
        return messages_api.get(theme, "Message non disponible.")

    def reinitialiser_interface(self):
        """Retourne à l'interface principale"""
        # Efface tous les widgets actuels
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        
        # Réaffiche le menu principal
        self.afficher_menu()

    def demarrer(self):
        """Lancer l'interface"""
        self.afficher_menu()
        self.root.mainloop()
