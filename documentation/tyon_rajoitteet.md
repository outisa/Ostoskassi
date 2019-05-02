Alla listattuna muutamia rajoitteita ja ongelmakohtia.

* Käyttäjän käyttömukavuutta ajatellen virheviestit voisivat tulla ponnahdusikkunaan käyttäjälle, jolloin ne olisi helpompi huomata. Tällä hetkellä tulevat vasempaan yläkulmaan, joka saattaa jäädä huomaamatta.
* Paikallisesti kokonaishinta ei pysy aina kahden desimaalin tarkkuudella, vaan on epätarkempi. Herokussa en ole tätä käyttäytymistä huomannut.
* kategoriassa, tuotteessa sekä ostoslistassa saman asian eri kirjoitusasut hyväksytään. Esimerkiksi Pesuaine ja pesuaine ovat eri tuotteita.
* Prosenttien pyöristyksissä saattaa tulla sadasosan virheitä, mutta en koe tämän olevan tässä yhteydessä vakava virhe tai puutos.
* Tietokannasta poistaminen tehokkaamaksi ja siistimmäksi. Mahdollisesti Cascade delete-orphan käyttö tässä toimenpiteessä. Alussa tämä toimi, mutta tietokantataulujen lisääntyessä, tämä toiminto meni jostain syystä rikki.
* Ääkköset eivät toimi paikallisesti testauksessa.
* Koodissa toisteisuutta kategoriassa, tuotteessa ja ostoslistassa käyttäjänoikeuden tarkistuksessa eri toiminnallisuuksiin. Kokeilin tehdä tämän omana metodina, mutta toiminta ei ollut toivottua. Tämä ilmeisesti siksi, että ulkopuolisen metodin suorittaman rivin return login_manager.unauthorized()  jälkeen palataan takaisin ulkopuolista metodia kutsuneeseen metodiin suorittamaan jäljelle jääneitä rivejä.  

Alla listattuna muutamia jatkokehitys ideoita.

* Käyttäjien roolit. Yksi tai useampi admin, tavallinen käyttäjä.
* Tilitietojen muuttaminen, kuten salasanan vaihto.
* Esilisättyjä tuotteita valmiina tuotelistassa.
* Haun tuloksen näyttäminen pylväsdiagrammina.
* Ostoslistan tuotelistauksen tulosten järjestäminen hinnan, kategorian tai tuotteen mukaan.
* Käyttö- ja asennusohjeisiin selkeyttävien kuvien lisäys.
