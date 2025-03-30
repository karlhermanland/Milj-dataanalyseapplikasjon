

# Om prosjektet

Dette prosjektet samler inn, strukturerer og senere analyserer værdata fra to åpne API-er:

Frost API (MET Norway) – med times- eller døgnoppløste observasjonsdata fra Blindern stasjon.
NASA POWER API – med daglige data for solinnstråling, bakketemperatur, luftfuktighet og trykk.
Prosjektet består av flere faser:

Datainnhenting og strukturering

    - Hente rådata fra de to kildene, og lagre dem i et ryddig CSV-format i mappen data/raw/.

Rensing og sammenslåing

    - Bearbeide og kombinere datasettene, slik at de kan analyseres sammen.

Visualisering og analyse (kommer senere)

    - Utforske datasettet videre gjennom grafer, statistikk og eventuelle maskinlæringsmodeller.

Dette repoet er i første omgang fokusert på datainnhenting og strukturering, men vil etter hvert utvides med mer analyse og visualisering.


# Prosjektstruktur

.
├── data/
│   ├── clean/                         # Renset og kombinert data
│   │   └── merged_data.csv
│   ├── raw/                           # Rådata hentet fra API-ene
│   │   ├── frost_data.csv
│   │   └── nasa_extended_data.csv
│   └── README.md                      # Beskrivelse av datastruktur
│
├── notebooks/                         # Jupyter Notebooks for utvikling og testing
│   ├── data_clean.ipynb
│   ├── data_fetch.ipynb
│   ├── MiljoTest.ipynb
│   └── README.md
│
├── resources/                         # Eventuelle bilder og eksterne filer
│   ├── images/
│   └── README.md
│
├── src/                               # Kildekode for prosjektet
│   ├── clean_data.py                  # Rense og strukturere data
│   ├── fetch_data_frost.py            # Hente data fra Frost API
│   ├── fetch_data_nasa.py             # Hente data fra NASA POWER API
│   ├── visualize.py                   # Funksjoner for å visualisere data
│   └── README.md
│
├── tasks/                             # Oppgavebeskrivelser og prosjektlevering
│   ├── mappe_del_1.md
│   ├── mappe_del_2.md
│   └── mappe_generell_del.md
│
├── tests/                             # Tester for prosjektet
│   ├── test_clean_data.py
│   ├── test_fetch_data.py
│   └── README.md
│
├── main.py                            # Hovedfil som kjører hele pipeline
└── README.md                          # Hoveddokumentasjon (denne filen)

# Datakilder

https://frost.met.no/

https://power.larc.nasa.gov/