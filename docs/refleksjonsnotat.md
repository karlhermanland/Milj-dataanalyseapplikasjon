Samarbeid

Samarbeidet vårt har fungert veldig bra gjennom hele prosjektet. Vi var to i gruppa, og selv om vi fordelte oppgavene ut fra interesse og styrker, hvor én jobbet mer med API-integrasjon og kodestruktur, og den andre med analyse og visualisering, har vi hele tiden hatt god kommunikasjon og sørget for at begge har hatt oversikt over hele prosessen. Vi jobbet ikke helt adskilt, men så heller over hverandres kode og diskuterte løsninger jevnlig. På den måten kunne vi lære av hverandre og fange opp ting som kunne forbedres tidlig.
Vi brukte Git aktivt, både for versjonskontroll og samarbeid. Å ha en strukturert mappestruktur og tydelige commit-meldinger hjalp oss mye, og vi jobbet med egne branches og merges for å unngå konflikter. En forbedringsmulighet er at vi i begynnelsen kunne vært enda flinkere til å ha små, jevnlige synkroniseringsmøter. Spesielt under datarensingsfasen endte vi opp med noe dobbeltarbeid fordi vi ikke hadde en klar nok plan for hvem som gjorde hva. Etter hvert fikk vi inn en god rutine med korte avklaringer før vi jobbet videre, og det gjorde resten av samarbeidet mer effektivt og oversiktlig.
Det viktigste vi tar med oss er at godt samarbeid ikke bare handler om å dele på oppgavene, men å ha et felles eierskap til hele prosjektet og være åpne for å lære av hverandre. Det har vært motiverende og lærerikt å jobbe i et team hvor begge er engasjerte og villige til å bidra i alle deler av prosjektet.

Resultater

Vi ble fornøyde med resultatene vi oppnådde. ComfortIndex-modellen vår fikk en R²-verdi på 0.99, og MAE var lav, noe som viser at modellen fanget opp mønstrene i dataene godt. Samtidig lærte vi at noen metrikker ikke alltid gir mening: MAPE-verdien ble ekstremt høy på grunn av datapunkter nær null, og det minnet oss på hvor viktig det er å tolke evalueringsmålinger i kontekst og ikke bare se på tallene isolert.
Visualiseringene vi lagde var avgjørende for å forstå modellens ytelse. Vi brukte blant annet scatterplots for faktisk vs. predikert ComfortIndex, residualplott for å avdekke skjevheter, og kombinasjoner av temperatur og luftfuktighet for å illustrere komfortnivåer. Det ga oss ikke bare innsikt i modellens styrker og svakheter, men også en dypere forståelse for hvordan visualisering kan være et viktig verktøy i modellvalidering.

Forbedringer

Hvis vi skulle videreutviklet prosjektet, er det flere ting vi ville gjort annerledes eller lagt til. For det første ville vi utforsket bruk av LSTM-modeller eller andre sekvensielle modeller for å fange opp tidstrender bedre. Vi ville også forsøkt å sammenligne våre prediksjoner med faktiske værvarsler for å evaluere modellens praktiske nytteverdi. En annen idé er å lage et interaktivt dashboard i Dash eller Plotly, slik at brukere kan utforske dataene selv og se hvordan prediksjonene endres over tid eller sted.
I tillegg ser vi at dataflyten mellom main.py og Jupyter-notebooks kunne vært bedre. Vi ville forbedret dataflyten mellom main.py og notebookene, slik at de samme resultatene kunne reproduseres både som script og som interaktiv rapport.

Læring

Vi har lært utrolig mye gjennom dette prosjektet, både faglig og teknisk. Fra starten, hvor vi satte opp utviklingsmiljøet og lærte å bruke Git, til vi jobbet med datahenting fra API-er, rensing, analyser og til slutt modellering og visualisering. Spesielt det å jobbe med ekte og rotete datasett har gitt oss en helt annen forståelse for datakvalitet og hva som skal til for å få brukbare resultater. Det er stor forskjell på teori og praksis, og dette prosjektet har vist oss hvor viktig det er å tenke gjennom hvert steg i dataflyten.
Vi har fått trening i bruk av biblioteker som Pandas, NumPy, Matplotlib, Seaborn og scikit-learn. I tillegg har vi lært hvordan man gjør feature engineering, hvordan man tolker modeller, og hvordan man bygger en pipeline som faktisk funker fra start til slutt. Prosjektet har også gjort oss tryggere på feilsøking, testing og dokumentasjon, og hvordan man skriver kode som både fungerer og er lett å forstå for andre.
Vi føler at vi har fått et tydeligere bilde av hva datavitenskap faktisk innebærer i praksis, og vi føler oss mye bedre rustet til videre prosjekter, både i studier og senere i arbeidslivet.

Fremtidig relevans

Alt vi har jobbet med i dette prosjektet, fra API-håndtering og datarensing, til modellering og formidling, er direkte relevant for både videre studier og jobber innen alt fra analyse og utvikling til forvaltning og beslutningsstøtte. Vi har sett hvordan data kan brukes til å gi innsikt i komplekse spørsmål som klima og komfort, og hvordan små tekniske valg kan ha stor innvirkning på sluttresultatet.
Det viktigste vi tar med oss videre er trygghet i verktøyene vi har brukt, en forståelse for hele prosessen fra rådata til innsikt, og en erfaring med samarbeid som vi vet vil være nyttig uansett hva vi jobber med i fremtiden.