import json
def read_json(file_name: str):
    """
    Lit un fichier JSON et retourne son contenu sous forme de dictionnaire.
    :return:
    """
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError as e:
        print(f"Erreur: Le fichier {file_name} n'a pas été trouvé.")
        raise e