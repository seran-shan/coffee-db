
# TDT4145 - DB2

Databaseapplikasjon implementert i Python.
Lager modeller, skriver SQL og aksesserer databasen bygd med SQLite3 gjennom Python.

## Utviklere

- [Julius Birkevold](https://github.com/juliusbirkevold)
- [Seran Shan](https://github.com/seran-shan)
- [Hammad Siddiqui](https://github.com/hammadsi)

## Bygd Med
- Python
- SQLite3
## Forutsetninger
Bindeleddet mellom Python og SQLite er sqlite3, en modul som baserer seg på Pythons 
offisielle database-API-spesifikasjon (PEP 249). Dette må installeres på forhånd.

```bash
  pip3 install pep249
```
## Installasjon

Kjør prosjektet gjennom Python.

```bash
  python coffe_db.py 
```
    
## Optimaliseringer og Konvensjoner

Unngår strenginterpolasjon for å unngå SQL-injeksjonsangrep.

Så istedenfor:

```bash
  cursor.execute("SELECT * FROM person WHERE navn = '%s'" % navn)
```

benyttes heller:


```bash
  cursor.execute("SELECT * FROM person WHERE navn = ?", [navn])
```   

## Dokumentasjon - Løsning for Brukerhistorier

#### 1. En bruker smaker kaffen Vinterkaffe 2022 fra Trondheims-brenneriet Jacobsen & Svart (brent 20.01.2022), gir den 10 poeng og skriver «Wow – en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!». Kaf- fen er lysbrent, bærtørket Bourbon (c. arabica), kommer fra gården Nombre de Dios (1500 moh.) i Santa Ana, El Salvador, har en kilopris på 600 kr og er ifølge brenneriet «En velsmakende og kompleks kaffe for mørketiden». Kaffen ble høstet i 2021 og gården fikk utbetalt 8 USD per kg kaffe. Input fra brukerens side er brenneri, kaffenavn, poeng og smaksnotat.
#### Løsning:

#### 2. En bruker skal kunne få skrevet ut en liste over hvilke brukere som har smakt flest unike kaffer så langt i år, sortert synkende. Listen skal inneholde brukernes fulle navn og antallet kaffer de har smakt.
#### Løsning:

#### 3. En skal kunne se hvilke kaffer som gir forbrukeren mest for pengene ifølge KaffeDBs brukere (høyeste gjennomsnittsscore kontra pris), sor- tert synkende. Listen skal inneholde brennerinavn, kaffenavn, pris og gjennomsnittsscore for hver kaffe.
#### Løsning:

#### 4. En bruker søker etter kaffer som er blitt beskrevet med ordet «floral», enten av brukere eller brennerier. Brukeren skal få tilbake en liste med brennerinavn og kaffenavn.
#### Løsning:

#### 5. En annen bruker er lei av å bli skuffet av vaskede kaffer og deres tid- vis kjedelige smak, og ønsker derfor å søke etter kaffer fra Rwanda og Colombia som ikke er vaskede. Systemet returnerer en liste over brennerinavn og kaffenavn.
#### Løsning:

### De tekstlige resultatene for brukerhistorienes spørringer blir:

#### 1.
#### 2.
#### 3.
#### 4.
#### 5.