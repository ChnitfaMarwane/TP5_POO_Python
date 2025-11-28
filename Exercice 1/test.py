from gestion_exception import CompteBancaire, FondsInsuffisants

if __name__ == '__main__':
    compte = CompteBancaire("flan fartlan", 100.00)

    compte.afficher() 

    try:
        compte.retirer(30.00)
        print(f"Retrait réussi. Nouveau solde : {compte._solde:.2f} MAD")
    except FondsInsuffisants as e:
        print(f"Erreur traitée: {e}")

    try:
        compte.retirer(100.00)
    except FondsInsuffisants as e:
        print(f"Erreur traitée: {e}")