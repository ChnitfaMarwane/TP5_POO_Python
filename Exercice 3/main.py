import logging
from csv_reader import charger_csv, CsvException

logging.basicConfig(filename='erreurs.log', level=logging.WARNING,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    chemin_fichier = 'articles.csv'
    
    try:
        print(f"Tentative de chargement du fichier : {chemin_fichier}")
        articles = charger_csv(chemin_fichier)
        
        print("\n--- Succès du chargement (MAD) ---")
        for art in articles:
            print(f"ID: {art['id']} | Nom: {art['nom']} | Prix: {art['prix']:.2f} MAD")

    except CsvException as e:
        print(f"\n--- ERREUR DE CHARGEMENT ---")
        print(f"Action requise : {e}")
        logging.error(f"Erreur métier interceptée : {e}")
        
    except Exception as e:
        print("\n--- ERREUR CRITIQUE ---")
        print("Une erreur inattendue est survenue. Veuillez contacter le support.")
        logging.critical(f"Erreur inattendue : {e}", exc_info=True)

if __name__ == '__main__':

    with open('articles_ok.csv', 'w', encoding='utf-8') as f:
        f.write("id;nom;prix\n")
        f.write("A01;Caftan flan;5000.50\n")
        f.write("A02;Théière fartlan;250.00\n")
        f.write("A03;Tapis blanlan;1200.75\n")
    
    with open('articles_err_prix_txt.csv', 'w', encoding='utf-8') as f:
        f.write("id;nom;prix\n")
        f.write("A01;Article Ok;100.00\n")
        f.write("A02;Prix Texte;abc\n") # Erreur ici
        f.write("A03;Article Ok 2;200.00\n")

    with open('articles_err_prix_neg.csv', 'w', encoding='utf-8') as f:
        f.write("id;nom;prix\n")
        f.write("A01;Article Ok;100.00\n")
        f.write("A02;Prix Négatif;-50.00\n") # Erreur ici
    
    
    print("====================================")
    print("--- Test 1 : Fichier Valide ---")
    main.chemin_fichier = 'articles_ok.csv'
    main()
    
    print("\n====================================")
    print("--- Test 2 : Fichier Absent ---")
    main.chemin_fichier = 'fichier_absent.csv'
    main()

    print("\n====================================")
    print("--- Test 3 : Prix Invalide (Texte) ---")
    main.chemin_fichier = 'articles_err_prix_txt.csv'
    main()

    print("\n====================================")
    print("--- Test 4 : Prix Négatif ---")
    main.chemin_fichier = 'articles_err_prix_neg.csv'
    main()