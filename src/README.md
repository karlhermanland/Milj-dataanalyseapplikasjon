# Om mappen

Mappen src/ inneholder all kildekoden som brukes for å hente inn, rense og bearbeide værdata i prosjektet. Dette er koden som utgjør kjernen i datainnhentings- og behandlingsprosessen. 


# Innhold 

**Filnavn**	            **Beskrivelse**
fetch_data_frost.py	    Funksjoner for å hente observasjonsdata fra Frost API.
fetch_data_nasa.py	    Funksjoner for å hente værdata fra NASA POWER API.
clean_data.py	        Funksjoner for å rense, strukturere og kombinere dataene.
train_data.py	        Kjører prediktiv analyse på værdata, trener SVR- og regresjonsmodeller, og genererer visualiseringer.
README.md	            Denne dokumentasjonen.


# Bruk

Disse filene brukes som moduler i hovedprogrammet main.py



