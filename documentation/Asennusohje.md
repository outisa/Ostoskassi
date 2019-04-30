### Sovelluksen asennus ja käyttöönotto paikallisesti

1. Valitse Ostoskassi repositiosta **_Clone or download_** -valikosta **_Download ZIP_**.
Pura lataamasi ZIP-tiedosto koneellasi klikkaamalla sitä hiiren oikealla painikkeella. Valitse vaihtoehto Extract here, jolloin kansioon syntyy alikansio Ostoskassi-master. Voit nyt poistaa ZIP-tiedoston. Siirry tämän jälkeen kansioon, josta projekti löytyy ja siellä kansioon Ostoskassi komennolla

`~$ cd Ostoskassi-master`

tai kloonaa repositio (vaatii SSH avaimen) komennolla

`~$ git clone git@github.com:outisa/Ostoskassi.git`

jonka jälkeen siirry kansioon Ostoskassi

`~$ cd Ostoskassi`
 
2. Luo ensin Python3 virtuaaliympäristö ja siirry virtuaaliympäristöön suorittamalla komennot

`~/Ostoskassi$ python3 -m venv venv`
`~/Ostoskassi$ source venv/bin/activate`

Huomaa! Kun käytät tai muokkaat sovellusta paikallisesti siirry aina ensin virtuaaliympäristöön.

3. Lataa sovelluksen vaatimat riippuvuudet käyttäen komentoa

`(venv) ~/Ostoskassi$ pip install -r requirements.txt`

4. Tämän jälkeen käynnistä ohjelma komennolla

`(venv) ~/Ostoskassi$ python3 run.py`

5. Siirry sen jälkeen osoitteeseen [http://localhost:5000](http://localhost:5000), jossa avautuu sovelluksen tervetuloa näkymä.

Sovellus sammuu painamalla näppäimistöltä `Ctrl` ja `c` 

### Sovelluksen asennus ja käyttöönotto selaimessa

1. Jos sovellus ei ole vielä asennettuna koneellesi, toteuta _Sovelluksen asennus ja käyttöönotto paikallisesti_ ohjeesta kohdat 1-3.

2. Luodaan seuraavaksi sovellukselle paikka herokussa. Oletuksena on, että käyttäjällä on Herokun käyttäjätunnukset ja työvälineet komentoriville [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli). Nimen täytyy olla uniikki, joten vaihda ostoskassi joksikin toiseksi nimeksi. Nimen poisjättäminen ei varsinaisesti haittaa, sillä Heroku luo tällöin automaattisesti jonkin satunnaisen nimen. 

`(venv) ~/Ostoskassi$ heroku create ostoskassi`

3. Lisätään sitten paikalliseen version hallintaan tieto herokusta 

`(venv) ~/Ostoskassi$ git remote add heroku https://git.heroku.com/ostoskassi.git`

4. Lähetetään projekti Herokuun komennoilla

`(venv) ~/Ostoskassi$ git add .`
`(venv) ~/Ostoskassi$ git commit -m "Initial commit"`
`(venv) ~/Ostoskassi$ git push heroku master`

5. Lisätään sovellukselle tieto, että se on herokussa komentorivillä komennolla

`(venv) ~/Ostoskassi$ heroku config:set HEROKU=1`

6. Tämän jälkeen voidaan tarkistaa onko sovelluksella käytössä tietokanta herokussa komennolla

`(venv) ~/Ostoskassi$ heroku pg:psql`

7. Mikäli tietokantaa ei ole, lisätään se komennolla

`(venv) ~/Ostoskassi$ heroku addons:add heroku-postgresql:hobby-dev`

### Sovelluksen käyttöönotto selaimessa ilman asennusta.

Siirry sivulle [https://ostoskassi-tsoha.herokuapp.com/](https://ostoskassi-tsoha.herokuapp.com/), jossa avautuu sovelluksen tervetuloa näkymä.
