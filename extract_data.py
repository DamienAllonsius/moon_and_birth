"""
extract INSEE data
T79JNAIS : Répartition quotidienne des naissances vivantes
"""
from collections import defaultdict
import datetime
import csv
from moonphase import get_phase_from_date


translate_month = {"Janvier": 1, "Février": 2, "Mars": 3, "Avril": 4, "Mai": 5, "Juin": 6, "Juillet": 7, "Août": 8,
                   "Septembre": 9, "Octobre": 10, "Novembre": 11, "Décembre": 12}


def get_moon_phases_number_births(file_path_csv, lang):
    moon_phase = defaultdict(lambda: 0)
    with open(file_path_csv, newline="") as csv_file:
        date = datetime.datetime(1968, 1, 1)

        spamreader = csv.reader(csv_file)
        for row in spamreader:
            for nb_births in row[2:]:
                if nb_births != "so":
                    moon_phase[get_phase_from_date(date, lang)] += int(nb_births)
                    date += datetime.timedelta(days=1)

    return dict(moon_phase)

#
# moon_phase = get_moon_phases_number_births("naissances_clean_2.csv")
# print(moon_phase)
