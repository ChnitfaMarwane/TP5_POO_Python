from gestion_reservation import Evenement, ReservationException

if __name__ == '__main__':
    event = Evenement("Festival de Gnawa", 5)
    event.afficher()

    print("\n--- Scénario de tests ---")

    try:
        event.reserver("flan lani", 2)
    except ReservationException as e:
        print(f"ÉCHEC 1 : {e}")

    try:
        event.reserver(" ", 1)
    except ReservationException as e:
        print(f"SUCCÈS 2 : Erreur traitée : {e}")

    try:
        event.reserver("fartlan", 0)
    except ReservationException as e:
        print(f"SUCCÈS 3 : Erreur traitée : {e}")

    try:
        event.reserver("blanlan", 4)
    except ReservationException as e:
        print(f"SUCCÈS 4 : Erreur traitée : {e}")

    print("\n--- Statut final de l'événement ---")
    event.afficher()