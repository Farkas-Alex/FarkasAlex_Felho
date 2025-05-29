#Diagram készítő bekéri a napok számát és a hőmérsékeltet
def keszit_diagram_sort(nap_szama, homerseklet):
#A csillagok számát a hőmérséklettel teszi egyenlővé
    csillagok_szama = int(homerseklet)
#Diagram megjelenését adja meg a csillagok száma alapján
    csillagok = '*' * csillagok_szama
    sor = f"Nap {nap_szama:2}: {csillagok} ({homerseklet}°C)"
    return sor

#Diagramot készít az átlag napi hőmérsékletekről
def rajzolj_diagram(homersekletek):
    print("Napi átlaghőmérséklet diagram (°C)")
    print("-" * 40)

# A hőmérsékelteket diagramokba szedi majd kiírja
    for i in range(len(homersekletek)):
        nap = i + 1  # Napok számozása 1-től indul
        sor = keszit_diagram_sort(nap, homersekletek[i])
        print(sor)


napi_atlaghomersekletek = [12, 15, 14, 16, 13, 17, 18]

#Behívja az adott funkciót
rajzolj_diagram(napi_atlaghomersekletek)