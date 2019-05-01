Alla listattuna muutamia rajoitteita.

* Käyttäjän käyttömukavuutta ajatellen virheviestit voisivat tulla ponnahdusikkunaan käyttäjälle, jolloin ne olisi helpompi huomata. Tällä hetkellä tulevat vasempaan yläkulmaan, joka saattaa jäädä huomaamatta.
* Paikallisesti kokonaishinta ei pysy aina kahden desimaalin tarkkuudella, vaan on epätarkempi. Herokussa en ole tätä käyttäytymistä huomannut.
* Prosenttien pyöristyksissä saattaa tulla sadasosan virheitä, mutta en koe tämän olevan tässä yhteydessä vakava virhe tai puutos.
* Tietokannasta poistaminen tehokkaamaksi ja siistimmäksi. Mahdollisesti Cascade delete-orphan käyttö tässä toimenpiteessä. Alussa tämä toimi, mutta tietokantataulujen lisääntyessä, tämä toiminto meni jostain syystä rikki.
* Ääkköset eivät toimi paikallisesti testauksessa.
* Päivityslinkin kautta siirryttäessä päivittämään kategoriaa tai tuotetta, ei tällä hetkellä lisätä automaattisesti kenttiin muokattavan kategorian tai tuotteen tietoja 'placeholderiksi'. Tämä huonontaa käyttömukavuutta ja altistaa virheille varsinkin, jos tuotteesta haluttaisiin vaihtaa pelkkä hinta.

Alla listattuna muutamia jatkokehitys ideoita.

* Käyttäjien roolit. Yksi tai useampi admin, tavallinen käyttäjä.
* Tilitietojen muuttaminen, kuten salasanan vaihto.
* Esilisättyjä tuotteita valmiina tuotelistassa.
* Haun tuloksen näyttäminen pylväsdiagrammina.
* Ostoslistan tuotelistauksen tulosten järjestäminen hinnan, kategorian tai tuotteen mukaan.
* Käyttö- ja asennusohjeisiin selkeyttävien kuvien lisäys.
