# Om prosjektet

Dette prosjektet henter inn, strukturerer og analyserer vær- og klimadata fra to åpne API-er:

- **Frost API** (MET Norway): gir times- eller døgnoppløste observasjoner fra stasjonen Oslo – Blindern.
- **NASA POWER API**: leverer daglige data for solinnstråling, bakketemperatur, luftfuktighet og trykk.

Prosjektet gjennomføres som et helhetlig datavitenskapelig løp – fra datainnhenting til prediktiv modellering og visualisering av innsikt.

## Faser i prosjektet

1. **Datainnhenting og strukturering**  
   Python-moduler henter rådata fra begge API-er og lagrer dem som `.csv`-filer i `data/raw/`.

2. **Rensing og sammenslåing**  
   Rådata transformeres og kombineres ved hjelp av `clean_data.py`. Det rensede datasettet lagres i `data/clean/`.

3. **Analyse og visualisering**  
   Utføres i `data_analyse.ipynb`, med utforskning av variabler, korrelasjoner og grafer. Visualiseringene genereres direkte i notebooken.

4. **Prediktiv modellering**  
   Utført i `prediction_model.ipynb`, som trener SVR-modeller for temperatur og solinnstråling og lineær regresjon for ComfortIndex. Visualiseringene genereres direkte i notebooken.

## Prosjektstruktur
```
├── data/
│ ├── clean/ # Renset og kombinert data
│ │ └── merged_data.csv
│ ├── raw/ # Rådata hentet fra API-ene
│ │ ├── frost_data.csv
│ │ └── nasa_extended_data.csv
│ └── README.md # Beskrivelse av datastruktur
│
├── notebooks/ # Jupyter Notebooks for utvikling og analyse
│ ├── data_analyse.ipynb # Visualisering og analyse av datasettet
│ ├── prediction_model.ipynb # Prediktiv modellering og evaluering
│ ├── test_notebooks/ #Notebooks for utvikling og testing
│ │ ├── data_clean.ipynb
│ │ ├── data_fetch.ipynb
│ │ └── MiljoTest.ipynb
│ └── README.md # Beskrivelse av notebooks
│
├── src/ # Kildekode for prosjektet
│ ├── clean_data.py # Rensing og strukturering
│ ├── fetch_data_frost.py # Henting av data fra Frost API
│ ├── fetch_data_nasa.py # Henting av data fra NASA POWER API
│ └── README.md # Beskrivelse av SRC-mappen
│
├── tasks/ # Oppgavebeskrivelser
│ ├── mappe_del_1.md
│ ├── mappe_del_2.md
│ └── mappe_generell_del.md
│
├── tests/ # Enhetstester for koden
│ ├── test_clean_data.py
│ ├── test_fetch_frost.py
│ ├── test_fetch_nasa.py
│ └── README.md # Beskrivelse av enhetstester
│
├── docs/ # Dokumentasjon
│ ├── KI_deklarasjon_Karl_Herman.pdf
│ ├── KI_deklarasjon_Aleksander.pdf
│ └── refleksjonsnotat.md # Refleksjonsnotat med læringsutbytte og erfaringer
│
├── main.py # Hovedfil som kjører via src/
├── .gitignore # Filer/mapper som skal ignoreres av git
├── requirements.txt # Prosjektavhengigheter
└── README.md # Hovedbeskrivelse av prosjektet (denne filen)
```


## Datakilder

- [Frost API – MET Norway](https://frost.met.no/)
- [NASA POWER API](https://power.larc.nasa.gov/)

## Bruk

Installer nødvendige pakker:
pip install -r requirements.txt

Innsamling og rensing av data gjennomføres via `main.py`, som automatisk henter, strukturerer og lagrer datasettet. Analyse, visualisering og prediktiv modellering utføres interaktivt i notebookene i `notebooks/`, der alle resultater og grafer genereres og vises direkte. Refleksjonsnotat finnes i `docs/refleksjonsnotat.md`.

