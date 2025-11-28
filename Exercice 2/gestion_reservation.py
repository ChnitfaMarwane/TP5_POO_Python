class ReservationException(Exception):
    def __init__(self, message):
        super().__init__(message)

class CapaciteDepasseeException(ReservationException): pass
class NombreInvalideException(ReservationException): pass
class NomClientInvalideException(ReservationException): pass

class Evenement:
    def __init__(self, nom, capacite):
        self.nom = nom
        self.capacite = capacite
        self.places_reservees = 0

    def reserver(self, nom_client, nb_places):
        if not nom_client.strip():
            # Lever une exception spécifique pour le nom vide
            raise NomClientInvalideException("Le nom du client ne peut pas être vide.")
        
        if nb_places <= 0:
            # Lever une exception spécifique pour le nombre invalide
            raise NombreInvalideException(f"Le nombre de places doit être positif (reçu : {nb_places}).")

        if self.places_reservees + nb_places > self.capacite:
            places_disponibles = self.capacite - self.places_reservees
            # Lever une exception spécifique pour la capacité dépassée
            raise CapaciteDepasseeException(f"Capacité dépassée. Reste {places_disponibles} places disponibles.")

        self.places_reservees += nb_places
        print(f"Réservation confirmée pour {nom_client} ({nb_places} places).")

    def afficher(self):
        print(f"Événement: {self.nom} | Statut: {self.places_reservees}/{self.capacite} places réservées.")