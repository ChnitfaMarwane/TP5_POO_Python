class FondsInsuffisants(Exception):
    def __init__(self, message):
        super().__init__(message)

class CompteBancaire:
    def __init__(self, nom, solde=0):
        self.nom = nom
        self._solde = solde

    def deposer(self, montant):
        if montant > 0:
            self._solde += montant

    def retirer(self, montant):
        if montant > self._solde:
            # Lever une exception personnalisée avec un message explicite
            raise FondsInsuffisants(f"Retrait de {montant:.2f} MAD impossible. Solde actuel: {self._solde:.2f} MAD.")
        self._solde -= montant

    def afficher(self):
        print(f"Compte: {self.nom}, Solde: {self._solde:.2f} MAD")