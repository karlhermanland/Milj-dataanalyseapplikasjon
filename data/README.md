# Om data-mappen

Mappen `data/` inneholder alle datasett brukt i prosjektet, og er delt inn i to hovedkategorier:

- `raw/`: Rådata hentet direkte fra API-er (Frost og NASA)
- `clean/`: Renset og bearbeidet data klart til analyse og modellering

---

## Innhold

| Mappe / Fil                                | Beskrivelse                                                             |
|--------------------------------------------|-------------------------------------------------------------------------|
| `raw/frost_data.csv`                       | Lokale værdata hentet fra Frost API (MET, Oslo-Blindern)                |
| `raw/nasa_extended_data.csv`               | Globale klimaverdier fra NASA POWER (solinnstråling, trykk, fuktighet)  |
| `clean/merged_data.csv`                    | Sammenstilt og renset datasett brukt som input i analysen               |
| `README.md`                                | Denne beskrivelsen                                                      |

---

## Bruksområde

- Data i `raw/` er kun til dokumentasjon og backup, og skal ikke redigeres manuelt. Filene kan oppdateres gjennom ny datainnhenting via egne Python-skript.
- `clean/merged_data.csv` er den bearbeidede datastrukturen som benyttes i hele prosjektet: visualisering, modelltrening og prediksjon.

