

import csv
from datetime import datetime
import os
import matplotlib.pyplot as plt


def til_tall(tekst): #
    tekst = tekst.replace(",", ".").strip()
    if tekst == "-" or tekst == "":
        return 0.0
    return float(tekst)


def til_dato(tekst):
    tekst = tekst.strip()
    try:
        return datetime.strptime(tekst, "%Y-%m-%d")
    except ValueError:
        try:
            return datetime.strptime(tekst, "%d.%m.%Y")
        except ValueError:
            return None



csv_sti = "sinnes_2014_2025.csv"

with open(csv_sti, "r", encoding="utf-8") as fil:

    valgt_år = input("Skriv inn et årstall (Data fra 2014-2025): ").strip()

datoer = []
temperaturer = []
nedbor_liste = []
vind_liste = []
snodybder = []

try:
    with open(csv_sti, "r", encoding="utf-8") as fil:
        leser = csv.reader(fil, delimiter=";")
        next(leser, None)
        
        for rad in leser:
            if len(rad) < 7:
                continue
            
            dato_obj = til_dato(rad[2])
            if dato_obj is None:
                continue
            
            if str(dato_obj.year) == valgt_år:
                datoer.append(dato_obj)
                temperaturer.append(til_tall(rad[3]))
                nedbor_liste.append(til_tall(rad[4]))
                vind_liste.append(til_tall(rad[5]))
                snodybder.append(til_tall(rad[6]))

except FileNotFoundError:
    print(f"Finner ikke filen: {csv_sti}")


if datoer:
    fig, aksene = plt.subplots(4, 1, figsize=(10, 8), sharex=True)
    
    aksene[0].plot(datoer, snodybder, color="blue")
    aksene[0].set_ylabel("Snødybde (cm)")
    aksene[0].set_title(f"Værdata for Sinnes ({valgt_år})")
    aksene[0].grid(True)
    
    aksene[1].plot(datoer, nedbor_liste, color="cyan")
    aksene[1].set_ylabel("Nedbør (mm)")
    aksene[1].grid(True)
    
    aksene[2].plot(datoer, temperaturer, color="red")
    aksene[2].set_ylabel("Middeltemp (°C)")
    aksene[2].grid(True)
    
    aksene[3].plot(datoer, vind_liste, color="green")
    aksene[3].set_ylabel("Middelvind (m/s)")
    aksene[3].set_xlabel("Dato")
    aksene[3].grid(True)
    
    fig.autofmt_xdate()
    plt.tight_layout()
    plt.show()
else:
    print(f"Ingen data funnet for {valgt_år}.")