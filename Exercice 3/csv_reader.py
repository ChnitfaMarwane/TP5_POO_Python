import csv
import os

class CsvException(Exception):
    pass

class FichierIntrouvableException(CsvException):
    def __init__(self, chemin):
        super().__init__(f"Le fichier CSV est introuvable au chemin : {chemin}")

class LigneInvalideException(CsvException):
    def __init__(self, ligne_num, message):
        super().__init__(f"Ligne {ligne_num} invalide : {message}")

class PrixNegatifException(CsvException):
    def __init__(self, ligne_num, prix):
        super().__init__(f"Ligne {ligne_num} : Le prix {prix:.2f} MAD est négatif ou nul.")


def charger_csv(chemin):
    if not os.path.exists(chemin):
        raise FichierIntrouvableException(chemin)
    
    articles = []
    
    try:
        with open(chemin, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            
            next(reader, None)

            for i, row in enumerate(reader, 2): # i commence à 2 (ligne de données 1 après l'en-tête)
                
                if not any(row):
                    continue

                if len(row) != 3:
                    raise LigneInvalideException(i, f"Attendu 3 colonnes, trouvé {len(row)}.")
                
                item_id, nom, prix_str = row
                
                try:
                    prix = float(prix_str)
                except ValueError:
                    raise LigneInvalideException(i, f"Le prix '{prix_str}' n'est pas un nombre valide.")
                
                if prix <= 0:
                    raise PrixNegatifException(i, prix)

                articles.append({
                    "id": item_id.strip(),
                    "nom": nom.strip(),
                    "prix": prix
                })

    except CsvException:
        raise 
    
    except Exception as e:
        raise CsvException(f"Erreur inattendue lors de la lecture du fichier : {e}")

    return articles