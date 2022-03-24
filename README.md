
# TDT4145 - DB2

Databaseapplikasjon implementert i Python.
Lager modeller, skriver SQL og aksesserer databasen bygd med SQLite3 gjennom Python.

## Utviklere

- [Julius Birkevold](https://github.com/juliusbirkevold)
- [Seran Shanmugathas](https://github.com/seran-shan)
- [Hammad Siddiqui](https://github.com/hammadsi)

## Bygd Med
- Python
- SQLite3
## Forutsetninger
Bindeleddet mellom Python og SQLite er sqlite3, en modul som baserer seg på Pythons 
offisielle database-API-spesifikasjon (PEP 249). Dersom dette ikke allerede er på PC-en kan de installeres med følgende kommando.

```bash
  pip3 install pep249
```
## Installasjon

Kjør prosjektet gjennom Python.

```bash
  python3 coffee_cli.py 
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

 1. En bruker smaker kaffen Vinterkaffe 2022 fra Trondheims-brenneriet Jacobsen & Svart (brent 20.01.2022), gir den 10 poeng og skriver «Wow – en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!». Kaffen er lysbrent, bærtørket Bourbon (c. arabica), kommer fra gården Nombre de Dios (1500 moh.) i Santa Ana, El Salvador, har en kilopris på 600 kr og er ifølge brenneriet «En velsmakende og kompleks kaffe for mørketiden». Kaffen ble høstet i 2021 og gården fikk utbetalt 8 USD per kg kaffe. Input fra brukerens side er brenneri, kaffenavn, poeng og smaksnotat.
#### Løsning:
> Brukeren vil bli bedt om å gge inn brenneri, kaffenavn, poeng og smaksnotat. 
> 
> Tast inn følgende for velutført test - 
> <br> For brennerinavn: "Oslo-brenneri"
> <br> For kaffenavn: "OsloKaffen"
> <br> For poeng: [valgfritt tall mellom 1-10]
> <br> For notat: [valgfri beskrivelse]
>
> Ved korrekt utførelse vil brukere få respons om at kaffen er lagt til. Dersom man legger inn en smaking på en kaffen man allerede har smakt vil brukeren motta en feilmelding.

 2. En bruker skal kunne få skrevet ut en liste over hvilke brukere som har smakt flest unike kaffer så langt i år, sortert synkende. Listen skal inneholde brukernes fulle navn og antallet kaffer de har smakt.
#### Løsning:
> Tast inn 2, og motta en liste med brukere som har smakt flest unike kaffer

 3. En skal kunne se hvilke kaffer som gir forbrukeren mest for pengene ifølge KaffeDBs brukere (høyeste gjennomsnittsscore kontra pris), sortert synkende. Listen skal inneholde brennerinavn, kaffenavn, pris og gjennomsnittsscore for hver kaffe.
#### Løsning:
> Tast inn 3, og motta en liste med mest verdifulle kaffe basert på score

 4. En bruker søker etter kaffer som er blitt beskrevet med ordet «floral», enten av brukere eller brennerier. Brukeren skal få tilbake en liste med brennerinavn og kaffenavn.

#### Løsning:
> Tast inn 4, deretter tast inn følgende: 
> <br> Search word: floral
> 
> Motta en liste med kaffe beskrevet som floral

 5. En annen bruker er lei av å bli skuffet av vaskede kaffer og deres tidvis kjedelige smak, og ønsker derfor å søke etter kaffer fra Rwanda og Colombia som ikke er vaskede. Systemet returnerer en liste over brennerinavn og kaffenavn.
#### Løsning:
> Tast inn 5, og motta en liste med mest verdifulle kaffe basert på score

### De tekstlige resultatene for brukerhistorienes spørringer blir:

> <br> 1. New tasting added! 
> <br>    Something went wrong! <- If the same tasting is added more than once
>
> <br> 2. Users with most unique coffee tasting -
> <br>    [{'full_name': 'Sensor Sensorsen', 'count': 3}, {'full_name': 'Julius', 'count': 1}]
>
> <br> 3. Most valuable coffe per kg -
> <br>    [{'roastery_name': 'Oslo-brenneri', 'name': 'OsloKaffen', 'price/kg': 23, 'score': 0.13043478260869565}, 
> <br>    {'roastery_name': 'Trondheims-brenneri', 'name': 'TrondheimsKaffen', 'price/kg': 30, 'score': 0.05}, 
> <br>    {'roastery_name': 'Tromso-brenneri', 'name': 'TromsoKaffen', 'price/kg': 40, 'score': 0.025}]
>
> <br> 4. Results -
> <br>    [{'roastery_name': 'Tromso-brenneri', 'coffee_name': 'TromsoKaffen'}]
>
> <br> 5. Unwashed coffees from Rwanda and Colobmia -
> <br>    [{'roastery': 'Tromso-brenneri', 'coffee_name': 'TromsoKaffen'}, {'roastery': 'Trondheims-brenneri',  
> <br>    'coffee_name': 'TrondheimsKaffen'}, {'roastery': 'Nidaros-brenneri', 'coffee_name': 'NidarosCoffee'}]
