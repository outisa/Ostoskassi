### Sovelluksen asennus ja käyttöönotto paikallisesti

Valitse Ostoskassi repositiosta **_Clone or download_** -valikosta **_Download ZIP_**.
Pura lataamasi ZIP-tiedosto koneellasi, jonka jälkeen siirry kansioon, johon latasit projektin ja siellä kansioon Ostoskassi komennolla:

`cd Ostoskassi-master`

tai kloonaa repositio (vaatii SSH avaimen) komennolla:

`git clone git@github.com:outisa/Ostoskassi.git`

jonka jälkeen siirry kansioon Ostoskassi

`cd Ostoskassi`
 
Luo ensin Python3 virtuaaliympäristö ja siirry virtuaaliympäristöön suorittamalla komennot:

`python3 -m venv venv`

`source venv/bin/activate`

Lataa sovelluksen vaatimat riippuvuudet käyttäen komentoa:

`pip install -r requirements.txt`

Tämän jälkeen käynnistä ohjelma komennolla

`python3 run.py`

Siirry sen jälkeen osoitteeseen [http://localhost:5000](http://localhost:5000), jossa avautuu sovelluksen tervetuloa näkymä.

### Sovelluksen käyttöönotto selaimessa

Siirry sivulle [https://ostoskassi-tsoha.herokuapp.com/](https://ostoskassi-tsoha.herokuapp.com/), jossa avautuu sovelluksen tervetuloa näkymä
