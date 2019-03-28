## Ostoskassi 
Harjoitustyön aiheena on ostoskassisovellus. Sovelluksen käyttäjä voi kirjautua ostoskassi -sovellukseen ja lisätä luomalleen ostoslistalle haluamiaan tuotteita. Alussa tuotteita ei ole olemassa ja kategorialista saattaa olla tyhjä, joten käyttäjän tulee lisätä haluamansa tuotteet ennen ostoslistan tekoa. Kategorialle annetaan vain kategorian nimi sitä lisättäessä. Käyttäjä voi myös päivittää kategorian keksiessään sille vaikkapa kuvaavamman nimen. Käyttäjä näkee myös kategoriat listana ja voi poistaa luomansa kategorian.

Luotaessa uutta tuotetta annetaan sille nimi, hinta ja sille merkitään kategoria kategorialistasta. Lisäksi käyttäjä voi poistaa ostoslistansa kokonaan, luoda uuden ostoslistan sekä tutkia ja muokata tuotteiden määrää ostoslistassa. Käyttäjä pystyy myös poistamaan tuotteen ja hän voi päivittää tuotteen hinnan sekä hän pystyy selailemaan jo olemassa olevia tuotteita. 

Jokaisella tuotteelle merkitään jokin kategoria. Jos kategoria kuitenkin poistetaan, jää tuote ilman kategoriaa ja niiden "kategoria" merkataan hauissa tyhjänä.  Kategorioiden avulla voidaan tehdä hakuja, joiden perusteella 
käyttäjä näkee paljonko rahaa on käytetty ostoskasseissa esimerkiksi herkkuihin. 

Käyttäjälle tarjotaan myös mahdollisuus kirjautua ulos sovelluksesta ja poistaa luomansa käyttötili sovellukseen, jolloin poistetaan myös käyttäjän luoma data.

**Tämän hetkisessä sovelluksessa:**

* **Luotaessa uutta tiliä, ei käyttäjätunnuksen olemassaoloa tarkisteta. Tämä pitää vielä korjata**
* **Jokainen käyttäjä näkee kaikkien luomat kategoriat. Tämä pitää vielä korjata**
* **Vain account ja category tietokantataulut ovat käytössä.**
* **CRUD -ominaisuus on category -taululla.**
* **Tunnukset on luotu valmiiksi yhdelle 'henkilölle', username: hello ja password: world, mutta myös omien tunnusten luonti ja poisto onnistuu**

[Tietokantakaavio](https://github.com/outisa/Ostoskassi/blob/master/documentation/Tietokantakaavio.md)

[Käyttötapaukset](https://github.com/outisa/Ostoskassi/blob/master/documentation/K%C3%A4ytt%C3%B6tapaukset.md)

Alla linkki sovellukseen.

[Ostoskassisovellus](https://ostoskassi-tsoha.herokuapp.com)


