# Om notebook-mappen

Mappen `notebooks/` inneholder Jupyter Notebooks som er brukt i prosjektet for utvikling, testing og analyse. Innholdet er delt inn i to hoveddeler:

- `test_notebooks/`: inneholder notebooker brukt til testing, prototyping og eksperimentering underveis i utviklingen.
- Øvrige notebooker (f.eks. `data_analyse.ipynb` og `prediction_model.ipynb`) inneholder den faktiske analysen, prediktiv modellering og visualisering som inngår i sluttproduktet.

---

## Innhold

### Hovednotebooks (analyse og modellering)

| Filnavn                    | Beskrivelse                                                     |
|----------------------------|-----------------------------------------------------------------|
| `data_analyse.ipynb`       | Analyse og visualisering av datasettet                          |
| `prediction_model.ipynb`   | Modellering og prediksjon av værdata                            |

### Testnotebooks (under utvikling)

| Filnavn                           | Beskrivelse                                                  |
|-----------------------------------|--------------------------------------------------------------|
| `test_notebooks/data_clean.ipynb` | Testing av ulike strategier for datarensing                  |
| `test_notebooks/data_fetch.ipynb` | Eksperimentering med datainnhenting fra ulike API-er         |
| `test_notebooks/MiljoTest.ipynb`  | Testing av miljø og pakkeavhengigheter                       |

| Filnavn                           | Beskrivelse                                                  |
|-----------------------------------|--------------------------------------------------------------|
| `README.md`                       | Denne beskrivelsen                                           |
---

## Bruksområde

Notebookene er brukt til:
- Interaktiv datarensing og strukturering
- Testing av API-integrasjon og datastrømmer
- Trening og evaluering av prediktive modeller
- Analyse og visualisering av resultater

Merk: Kun notebookene utenfor `test_notebooks/` representerer den ferdige og strukturerte delen av prosjektet.
