Gjennom dette prosjektet har vi jobbet med et komplett datavitenskapelig løp – fra innhenting og rensing av værdata, til analyse og prediksjon av fremtidige miljøforhold. Prosjektet ga oss innsikt i hvordan åpne API-er kan benyttes til å hente sanntidsdata, og hvordan disse kan kombineres og analyseres for å gi ny innsikt i værmønstre. I tillegg fikk vi erfaring med å bruke ulike verktøy innen dataanalyse og maskinlæring i Python.

Datainnsamling og behandling: Et sentralt læringspunkt i prosjektet var hvordan vi henter data fra både Frost API (MET) og NASA POWER. Vi utviklet egne Python-moduler for dette, og lærte hvordan man håndterer API-nøkler, strukturerer requests og lagrer resultatene i egnet CSV-format. Frost-dataene ga oss lokale observasjoner fra Blindern, mens NASA-dataene supplerte med verdier som solinnstråling, trykk og fuktighet. En utfordring var at datastrukturen og tidsoppløsningen ikke alltid matchet, noe som krevde nøye transformasjoner før de kunne slås sammen.

Gjennom clean_data.py utviklet vi en funksjonell pipeline for å rense og kombinere dataene. Dette inkluderte å konvertere datotidspunkt, aggregere per dag, håndtere manglende verdier og sikre at variablene var sammenlignbare. Vi oppdaget tidlig at enkelte kolonner hadde flere manglende verdier, og ble derfor nødt til å droppe eller fylle dem med snittverdier.

Analyse og visualisering: I analysefasen opprettet vi en egen modul (train_data.py) som først trente en lineær regresjonsmodell på den sammenslåtte dataen, og deretter introduserte vi Support Vector Regression (SVR) for å predikere temperatur og solinnstråling 365 dager frem i tid. Vi la også til sesongvariabler som Month, Sin_Day og Cos_Day for å fange årstidseffekter. Dette forbedret prediksjonene betraktelig.
Vi brukte Matplotlib og Seaborn for å lage flere informasjonsrike grafer, som:
•	Predikert vs faktisk ComfortIndex
•	Feilfordeling (residualer)
•	Temperatur vs ComfortIndex med fargekodet luftfuktighet
•	Fremtidsprediksjon av temperatur og solinnstråling, glattet med rullende gjennomsnitt
Disse visualiseringene hjalp oss å tolke modellenes ytelse, identifisere avvik, og forstå koblingen mellom miljøvariabler og opplevd komfort.

Ferdigheter vi har utviklet: Prosjektet har gitt oss praktisk erfaring med flere sentrale Python-biblioteker:
•	Pandas for datamanipulering og rensing
•	NumPy for numeriske beregninger og vektorisering
•	Matplotlib og Seaborn for visualisering
•	Scikit-learn for modelltrening, prediksjon og evaluering
•	Subprocess og sys for å integrere analysen i en automatisert pipeline (main.py)
Vi har også lært om konseptene bak standardisering, feature engineering (tid som sinuskurver), overtrening, og bruk av regresjon vs ikke-lineære modeller som SVR.

Utfordringer: En stor utfordring var å få prediksjonene til å gi realistiske verdier over tid. Før vi la til sesongfunksjoner, predikerte modellen synkende temperatur mot sommeren. Vi løste dette ved å bruke sinus- og cosinusbaserte representasjoner av tid på året. I tillegg opplevde vi at SVR-modellen krevde nøye skalering og variert input for å unngå statiske eller trappetrinnsaktige prediksjoner.
En annen utfordring var å forstå hvilke variabler som faktisk påvirket ComfortIndex, og hvordan man kunne velge de mest informative features uten å gjøre modellen for kompleks.

Samarbeid og arbeidsflyt: Prosjektet ble gjennomført i gruppe på to, der vi fordelte oppgaver etter kompetanse og interesse. Noen fokuserte på API-integrasjon, andre på datarensing og analyse. Kommunikasjonen foregikk effektivt gjennom korte arbeidsmøter og bruk av felles Git-repositorium. Det var særlig nyttig å jobbe med en tydelig mappestruktur og skille src, data, scripts og visualiseringer.

Vurdering av resultater: Vi er svært fornøyde med sluttresultatet. Modellene ga forståelige og visuelle prediksjoner, og ComfortIndex-analysen oppnådde god nøyaktighet (R² på rundt 0.79). Grafene som ble generert var både informative og oversiktlige, og vi opplevde at datasettet faktisk ga meningsfull innsikt i klima og komfort.

Videre forbedringer og forskning: Prosjektet kan videreutvikles ved å:
•	Legge til flere stasjoner og geografiske områder
•	Bruke LSTM eller annen sekvensiell modell for mer avansert tidsprediksjon
•	Lage interaktive dashboards med f.eks. Plotly eller Dash
•	Integrere eksterne værvarsler for sammenligning

Oppsummering: Gjennom dette prosjektet har vi fått en helhetlig forståelse for hvordan et datavitenskapelig prosjekt kan bygges opp – fra rådata til analyse og innsikt. Det har styrket vår forståelse for programmering, datarensing og maskinlæring, og gitt oss konkrete verktøy vi tar med videre både i videre studier og i en fremtidig jobbsammenheng. Erfaringen med å jobbe med reelle data og se konkrete resultater av modellene våre har vært svært motiverende og lærerik.
