# Atlanti elettorali, sezione per sezione

Due mappe navigabili delle sezioni elettorali italiane, pubblicate su GitHub Pages:
<https://alessandroalberti-researchunit.github.io/atlanti-elettorali/>

| Mappa | Tornata | Sezioni | Cosa contiene |
|---|---|---|---|
| [`roma-2021/`](roma-2021/) | Comunali di Roma, 3-4 ottobre 2021 | 2.597 | 38 liste comunali, 22 candidati sindaco, presidente e liste dei 15 municipi, preferenze di 1.648 candidati al consiglio comunale |
| [`europee-2024/`](europee-2024/) | Europee, 9 giugno 2024 | 7.946 in 10 città | affluenza, voti di lista, preferenze, divario di genere |

Ogni pagina è un file HTML autosufficiente: geometrie e risultati stanno dentro il
file, non serve un server e non c'è nessuna chiamata a un'API. Dalla rete arrivano
soltanto i caratteri tipografici (Google Fonts) e le tessere del fondo cartografico
(Esri World Light Gray Canvas), scaricate una alla volta mentre si naviga. Senza rete
le pagine si aprono lo stesso, con caratteri di sistema e senza fondo sotto le sezioni.

Sono file pesanti (2 MB e 4 MB): il primo caricamento richiede qualche secondo.

## Provenienza

**Risultati.** Europee 2024: file per sezione del Ministero dell'Interno. Comunali di
Roma 2021: verbali dell'ufficio centrale di Roma Capitale, modelli ministeriali
300/I-AR (sindaco), 301-AR (liste comunali), 302-AR (preferenze), 311-M (presidente di
municipio), 312-M (liste municipali). Ogni prospetto è stato quadrato contro i totali
stampati sui verbali stessi, riga per riga e colonna per colonna.

**Geometrie.** Ufficiali dove il Comune le pubblica (Bologna, Genova, Firenze, Modena,
Cesena), altrove ricostruite per prossimità agli indirizzi dei seggi a partire da
[SEI, Sezioni Elettorali Italiane](https://github.com/gabrielepinto/dati-sezioni-elettorali)
di Gabriele Pinto, CC-BY-SA 4.0 (citazione richiesta: Gabriele Pinto (2023),
DOI 10.1080/2474736X.2023.2185158).

**Le geometrie ricostruite non sono confini amministrativi.** Vanno bene per mappe
tematiche e aggregazioni per zona, non per affermare che un dato edificio ricade in una
data sezione.

**Fondo cartografico.** Esri World Light Gray Canvas (Esri, HERE, Garmin, FAO, NOAA,
USGS), usato secondo i termini Esri: nessuno scarico in blocco, attribuzione visibile
in basso a destra sulla mappa. Le tessere si fermano al livello di zoom 16, il massimo
pubblicato dal servizio.

## Avvertenze

1. **Le sezioni speciali non hanno perimetro** e restano fuori dalla mappa: sono le
   ospedaliere e simili, a zero elettori. Pesano fra lo 0,000% e lo 0,277% dei voti a
   seconda della città; il riquadro Provenienza dentro ogni mappa riporta il dato esatto.
2. **Nella mappa di Roma 2021 la metrica si chiama partecipazione, non affluenza.** I
   verbali pubblicano i voti validi, non i votanti: bianche e nulle restano fuori dal
   numeratore, quindi il numero sta sotto l'affluenza vera. Per Roma vale 47,2%
   (1.113.677 voti validi al sindaco su 2.359.248 iscritti).
3. **I colori delle liste sono una scelta di leggibilità, non un dato.** Servono a far
   riconoscere le aree sulla mappa.
4. **Le geometrie non sono sempre dello stesso anno dei risultati.** Il collegamento per
   numero di sezione è stato verificato, ma un ridisegno delle sezioni fra le due date
   non sarebbe visibile.

## Come si aggiorna

Questo repository contiene solo il sito pubblicato. Le due mappe si costruiscono
altrove, ciascuna dalla propria cartella di lavoro, e poi si copiano qui con:

```
python aggiorna_sito.py
```

Lo script prende `Atlante_Roma_2021/atlante_roma2021.html` e
`Atlante_Sezioni/atlante.html` dalla cartella di lavoro che contiene questa e li scrive
in `roma-2021/index.html` e `europee-2024/index.html`. Se le cartelle di partenza non
ci sono, lo dice e non tocca niente.

## Licenza

I dati elettorali sono pubblici (Ministero dell'Interno, Roma Capitale). Le geometrie
SEI sono CC-BY-SA 4.0 e vanno citate come sopra.
