# Om src-mappen

Mappen `src/` inneholder all kildekode som brukes til å hente, rense, strukturere og analysere vær- og klimadata. Dette utgjør kjernen i datainnhentings- og behandlingsprosessen i prosjektet, og brukes som grunnlag for analysene i notebookene og i hovedprogrammet `main.py`.

---

## Innhold

| Filnavn                | Beskrivelse                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `fetch_data_frost.py`  | Funksjoner for å hente observasjonsdata fra Frost API                       |
| `fetch_data_nasa.py`   | Funksjoner for å hente værdata fra NASA POWER API                           |
| `clean_data.py`        | Funksjoner for å rense, strukturere og kombinere data fra ulike kilder      |
| `README.md`            | Denne dokumentasjonen                                                       |
---

## Bruk

Filene i `src/` fungerer som moduler og byggesteiner i prosjektet, og kalles fra `main.py`. Hver modul har en avgrenset rolle: innhenting eller rensing og klargjøring av data. 


