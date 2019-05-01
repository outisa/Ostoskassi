Alla listattuna muutamia rajoitteita.

* Käyttäjän käyttömukavuutta ajatellen virheviestit voisivat tulla ponnahdusikkunaan käyttäjälle, jolloin ne olisi helpompi huomata. Tällä hetkellä tulevat vasempaan yläkulmaan, joka saattaa jäädä huomaamatta.
* Paikallisesti kokonaishinta ei pysy aina kahden desimaalin tarkkuudella, vaan on epätarkempi. Herokussa en tätä ole huomannut.
* Tietokannasta poistaminen tehokkaamaksi ja siistimmäksi. Mahdollisesti Cascade delete-orphan käyttö tässä toimenpiteessä. Alussa tämä toimi, mutta tietokantataulujen lisääntyessä, tämä toiminto meni jostain syystä rikki.
* Ääkköset eivät toimi paikallisesti testauksessa.


Alla listattuna muutamia jatkokehitys ideoita.

* Käyttäjien roolit. Yksi tai useampi admin, tavallinen käyttäjä.
* Esilisättyjä tuotteita valmiina tuotelistassa.
* Haun tuloksen näyttäminen pylväsdiagrammina.
* Ostoslistan tuotelistauksen tulosten järjestäminen hinnan, kategorian tai tuotteen mukaan.
* Käyttö- ja asennusohjeisiin selkeyttävien kuvien lisäys.
