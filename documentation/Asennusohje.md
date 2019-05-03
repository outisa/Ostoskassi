### Sovelluksen asennus ja käyttöönotto paikallisesti

1. Valitse Ostoskassi repositiosta **_Clone or download_** -valikosta **_Download ZIP_**.
Pura lataamasi ZIP-tiedosto koneellasi klikkaamalla sitä hiiren oikealla painikkeella. Valitse vaihtoehto Extract here, jolloin kansioon syntyy alikansio Ostoskassi-master. Voit nyt poistaa ZIP-tiedoston. Siirry tämän jälkeen kansioon, josta projekti löytyy ja siellä kansioon Ostoskassi syöttämällä terminaalissa komento  

`cd Ostoskassi-master`

**tai** kloonaa repositio (vaatii SSH avaimen) komennolla

`git clone git@github.com:outisa/Ostoskassi.git`

jonka jälkeen siirry kansioon Ostoskassi

`cd Ostoskassi`
 
 **_Seuraavat komennot tehdään kansiossa Ostoskassi, jonka tarkempi nimi riippuu siitä, kloonasitko vai latasitko ZIP-tiedoston. Katso tarkemmin kohta 1._**
2. Luo ensin Python3 virtuaaliympäristö ja siirry virtuaaliympäristöön suorittamalla komennot

`python3 -m venv venv`

`source venv/bin/activate`

Huomaa! Kun käytät tai muokkaat sovellusta paikallisesti siirry aina ensin virtuaaliympäristöön.

3. Lataa sovelluksen vaatimat riippuvuudet käyttäen komentoa

`pip install -r requirements.txt`

4. Tämän jälkeen käynnistä ohjelma komennolla

`python3 run.py`

5. Siirry sen jälkeen osoitteeseen [http://localhost:5000](http://localhost:5000), jossa avautuu sovelluksen tervetuloa näkymä.

Sovellus sammuu painamalla näppäimistöltä `Ctrl` ja `c` 

### Sovelluksen asennus ja käyttöönotto selaimessa

1. Jos sovellus ei ole vielä asennettuna koneellesi, toteuta _Sovelluksen asennus ja käyttöönotto paikallisesti_ ohjeesta kohdat 1-3. Jos sovellus on jo asennettuna, siirry kansioon Ostoskassi `cd Ostoskassi` paikasta, jonne kansio on ladattuna ja sen jälkeen siirry virtuaaliympäristöön `source venv/bin/activate`. Huomaa, että kansio Ostoskassi saattaa olla muodossa Ostoskassi-master, riippuen tavastasi hakea sovellus koneellesi GitHubista.

2. Luodaan seuraavaksi sovellukselle paikka herokussa. Oletuksena on, että käyttäjällä on Herokun käyttäjätunnukset ja työvälineet komentoriville [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli). Nimen täytyy olla uniikki, joten vaihda ostoskassi joksikin toiseksi nimeksi. Nimen poisjättäminen ei varsinaisesti haittaa, sillä Heroku luo tällöin automaattisesti jonkin satunnaisen nimen.  

`heroku create ostoskassi`

3. Lisätään sitten paikalliseen version hallintaan tieto herokusta 

`git remote add heroku https://git.heroku.com/ostoskassi.git`

4. Lähetetään projekti Herokuun komennoilla

`git add .`  
`git commit -m "Initial commit"`  
`git push heroku master`  

5. Lisätään sovellukselle tieto, että se on herokussa komentorivillä komennolla

`heroku config:set HEROKU=1`

6. Tämän jälkeen voidaan tarkistaa onko sovelluksella käytössä tietokanta herokussa komennolla

`heroku pg:psql`

7. Mikäli tietokantaa ei ole, lisätään se komennolla

`heroku addons:add heroku-postgresql:hobby-dev`

8. Mene seuraavaksi Herokuun omille sivuillesi, ja voit käyttää sovellusta klikkaamalla _Open app_ nappia sivun yläkulmassa.

### Sovelluksen käyttöönotto selaimessa ilman asennusta.

Siirry sivulle [https://ostoskassi-tsoha.herokuapp.com/](https://ostoskassi-tsoha.herokuapp.com/), jossa avautuu sovelluksen tervetuloa näkymä.
