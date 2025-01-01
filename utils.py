from datetime import datetime, timedelta
import requests
import os

classes =[('3', '1'), ('3', '2'), ('3', '3'), ('3', '4'), ('4', '1'), ('4', '2'), ('4', '3'), ('4', '4'), ('5', '1'), ('5', '2'), ('5', '3'), ('5', '4'), ('CYNU', '1'), ('IST', '1'), ('RESA', '1'), ('RESA', '2'), ('RESA', '3'), ('RESA', '4'), ('RESA', '5'), ('RESA', '6')]

def get_link():
    try:
        with open("link.txt", "r") as file:
            link = file.readline().strip()
            return link
    except FileNotFoundError:
        print("Le fichier 'link.txt' est introuvable.")

def get_ical(link, promo, group):

    # Vérifiez si le dossier existe, sinon créez-le
    dossier_ical = "ical"  # Assurez-vous que ce dossier existe
    if not os.path.exists(dossier_ical):
        os.makedirs(dossier_ical)

    # URL du fichier iCalendar
    url = link.format(promo=promo, group=group)
    # Dossier de destination où le fichier .ical sera sauvegardé

    # Nom du fichier .ical à enregistrer
    nom_fichier = f"{promo}TC{group}.ical"

    # Télécharger le fichier .ical
    response = requests.get(url)

    # Vérifiez si la requête a réussi (code 200)
    if response.status_code == 200:
        # Enregistrer le contenu du fichier dans le dossier spécifié
        chemin_complet = os.path.join(dossier_ical, nom_fichier)
        with open(chemin_complet, 'wb') as f:
            f.write(response.content)
        print(f"Fichier téléchargé avec succès et sauvegardé sous : {chemin_complet}")
        return True
    else:
        print(f"Échec du téléchargement. Code de statut : {response.status_code}")
        return False

def get_icals(link):
    # Promos et groupes
    icals_ok = True
    for promo, group in classes:
        icals_ok=icals_ok and get_ical(link, promo, group)
    if icals_ok:
        return True
    else:
        return False

def generer_heures(debut, fin, pas=30):
        heures = []
        heure_actuelle = datetime.strptime(debut, '%H:%M')
        heure_fin = datetime.strptime(fin, '%H:%M')
        
        while heure_actuelle <= heure_fin:
            heures.append(heure_actuelle.strftime('%H:%M'))
            heure_actuelle += timedelta(minutes=pas)
        
        return heures

def generate_table():

    # Générer les heures de 8h00 à 17h30
    plages_horaires = generer_heures('08:00', '17:30')

    # Initialiser la structure de l'emploi du temps
    table = {heure: [] for heure in plages_horaires}
    # Afficher la structure de base
    return table
