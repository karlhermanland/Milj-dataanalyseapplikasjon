# Enhetstester for Miljødataanalyseapplikasjon

Denne mappen inneholder enhetstester for funksjonene som henter og renser miljødata i prosjektet. Testene er skrevet med `unittest`-rammeverket i Python.

## Innhold

| Filnavn                        | Hva den tester                                              |
|-------------------------------|-------------------------------------------------------------|
| `test_fetch_frost.py`         | Tester nedlasting av værdata fra FROST-API og filskriving  |
| `test_fetch_nasa.py`          | Tester henting og lagring av data fra NASA POWER API       |
| `test_clean_data.py`          | Tester hele prosessen for datarensing og sammenkobling     |

## Hvordan kjøre testene

Kjør følgende kommando fra prosjektets rotmappe:

```bash (lim inn og kjør denne i terminalen)
python -m unittest discover tests
