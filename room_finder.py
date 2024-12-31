import os
from datetime import datetime
from icalendar import Calendar
from utils import get_icals, generate_table, get_link

allowed_locations = ['Projet Vitrine', 'Amphi Chappe', 'Projet TD A', 'Projet TD B', 'TP Info B', 'TD C', 'TD D', 'TD E', 'TP Info C', 'TP Info D', 'TP Info E', 'TD F(LS)']

def open_groupe_ical(group):
    # Chemin du script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Chemin vers le fichier dans le dossier '2'
    file_path = os.path.join(script_dir, 'ical', f'{group}')

    try:
        with open(file_path, 'r') as file:
            # Charger le fichier .ical en utilisant icalendar
            ical_content = file.read()
            calendar = Calendar.from_ical(ical_content)
            print("Fichier chargé avec succès.")
            return calendar
    except FileNotFoundError:
        print(f"Le fichier '{file_path}' est introuvable.")

def get_index(heure_str):
    # Convertir l'heure donnée au format 'HH:MM' en objet datetime
    heure = datetime.strptime(heure_str, '%H:%M')

    # L'heure de début (08:00)
    debut_jour = datetime.strptime('08:00', '%H:%M')

    # Calculer la différence en minutes
    difference_minutes = (heure - debut_jour).seconds // 60
    
    # Calculer l'indice basé sur des intervalles de 30 minutes
    index = difference_minutes // 30
    
    return index

def get_courses(calendar, date):
    for component in calendar.subcomponents:
        if component.name == "VEVENT":
            # Récupérer les informations de l'événement
            start_time = component.get('DTSTART').dt
            end_time = component.get('DTEND').dt
            location = component.get('LOCATION')[2:]
            summary = component.get('SUMMARY')

            # Vérifier si l'événement est à la date donnée
            if start_time.strftime('%d/%m/%Y') == date:
                # Calcul de la durée de l'événement en demi-heures
                duration = (end_time - start_time).seconds // 1800
                begin_index = get_index(start_time.strftime('%H:%M'))
                # Ajout des salles à l'emploi du temps
                for halfhour in list(timetable.keys())[begin_index : begin_index + duration]:
                    if location not in timetable[halfhour] and location in allowed_locations:
                        timetable[halfhour].append(location)

def get_available_rooms(timetable, begin, span):
    # Trouver les salles disponibles pour une durée donnée
    available_rooms = allowed_locations.copy()
    duration_index = span * 2
    begin_index = get_index(begin)
    for halfhour in list(timetable.keys())[begin_index : begin_index + duration_index]:
        for room in timetable[halfhour]:
            if room in available_rooms:
                available_rooms.remove(room)
    return available_rooms

link = get_link()

date = '14/01/2025'
begin = '08:00'
span = 18
if span > 20:
    span_text = "toute la journée"
else:
    span_text = f"{span/2}h"

# Mettre à jour les fichiers .ical
UPDATE = False

if UPDATE:
    get_icals(link)
    print("Fichiers .ical mis à jour.")

# Initialiser l'emploi du temps
timetable = generate_table()

# Parcourir tous les groupes de fichiers .ical dans le dossier 'ical'
groups = os.listdir('ical')

for group in groups:
    group_table = open_groupe_ical(group)
    get_courses(group_table, date)

available_rooms = get_available_rooms(timetable, begin, span)
print(f"Le {date} à {begin} pendant {span_text}, Salles disponibles :")
print(available_rooms)