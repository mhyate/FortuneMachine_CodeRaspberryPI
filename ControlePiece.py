#verification qu'une piece a ete inserer pour ouvrir l'interface 

class LecteurPiece:
    def __init__(self):
        self.piece_inseree = False

    def inserer_piece(self):
        if not self.piece_inseree:
            print("Une pièce a été insérée dans le lecteur.")
            self.piece_inseree = True
        else:
            print("Une pièce est déjà présente dans le lecteur.")

    def retirer_piece(self):
        if self.piece_inseree:
            print("La pièce a été retirée du lecteur.")
            self.piece_inseree = False
        else:
            print("Il n'y a pas de pièce dans le lecteur.")




