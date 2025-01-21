import tkinter as tk
import os
import sys
from PIL import Image, ImageTk
from tkinter import messagebox
from Classes.CNQuotes import CNQuotes
from Classes.Meteotry import Meteotry
from Classes.Horoscope import Horoscope
from Classes.Blagues import Blagues
import platform

# Ajouter le chemin de l'image de fond
cheminBGImage = os.path.join(os.path.dirname(__file__), 'background.png')

class InterfaceGraphique:
    def __init__(self, printer=None):
        print("Initialisation de l'interface graphique...")
        self.root = tk.Tk()
        self.root.title("Fortune Machine")
        
        # Configuration plein écran
        print("Configuration du mode plein écran...")
        self.root.attributes('-fullscreen', True)  # Force le mode plein écran
        
        # Cache le curseur uniquement sur Raspberry Pi
        if platform.system() != 'Darwin':  # Si ce n'est pas macOS
            print("Configuration du curseur (masqué)...")
            self.root.config(cursor="none")
        else:
            print("Configuration du curseur (visible)...")
        
        # Capture la touche Escape pour quitter le plein écran (utile pour le développement)
        self.root.bind('<Escape>', lambda e: self.root.attributes('-fullscreen', False))
        
        self.printer = printer
        print("Création du canvas...")
        self.canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        print("Chargement de l'image de fond...")
        self.update_background()

        # Cadre des boutons
        print("Création du cadre des boutons...")
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

        # Afficher d'abord le message de la fortune
        message_label = tk.Label(self.button_frame, text=message, font=("Helvetica", 24), bg='white', fg='black', wraplength=800)
        message_label.pack(pady=20)

        # Ajouter un peu d'espace
        spacer = tk.Frame(self.button_frame, height=20, bg='white')
        spacer.pack()

        # Ensuite afficher la question d'impression
        label = tk.Label(self.button_frame, text="Voulez-vous imprimer la fortune ?", font=("Helvetica", 30), bg='white', fg='black')
        label.pack(pady=10)

        # Frame pour les boutons
        button_frame = tk.Frame(self.button_frame, bg='white')
        button_frame.pack(pady=10)

        # Bouton Oui
        oui_button = tk.Button(button_frame, text="Oui", font=("Helvetica", 16), command=lambda: self.imprimer_fortune(message))
        oui_button.pack(side=tk.LEFT, padx=20)

        # Bouton Non
        non_button = tk.Button(button_frame, text="Non", font=("Helvetica", 16), command=lambda: self.afficher_message(message))
        non_button.pack(side=tk.RIGHT, padx=20)

    def afficher_menu(self):
        """Affiche le menu principal avec les thèmes"""
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        themes = ["Météo", "Chuck Norris", "Horoscope", "Blagues"]
        for i, theme in enumerate(themes):
            button = tk.Button(self.button_frame, text=theme, font=("Helvetica", 16), width=25, height=5,
                             command=lambda t=theme: self.demander_impression(t),
                             bg='white', relief='flat', borderwidth=0,
                             activebackground='#f0f0f0')
            button.grid(row=i // 2, column=i % 2, padx=10, pady=10)

    def imprimer_fortune(self, texte):
        """Imprime la fortune si une imprimante est connectée"""
        if self.printer:
            # Afficher le message d'impression en cours
            self.afficher_message("Impression...")
            # Attendre 3 secondes puis retourner au menu
            self.root.after(3000, self.afficher_menu)
            # Simuler l'impression dans la console
            print(f"Fortune imprimée : {texte}")
        else:
            self.afficher_message("Aucune imprimante connectée.")

    def recuperer_message_api(self, theme):
        """Récupère un message depuis l'API correspondante au thème choisi"""
        try:
            message = None
            if theme == "Météo":
                api = Meteotry()
                message = api.run()
            elif theme == "Chuck Norris":
                api = CNQuotes()
                message = api.run()
            elif theme == "Horoscope":
                api = Horoscope()
                message = api.run()
            elif theme == "Blagues":
                api = Blagues()
                message = api.run()
            
            if not message:
                return None
            return message
        except Exception as e:
            print(f"Erreur lors de la récupération du message: {e}")
            return None

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
