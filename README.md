## Ostoskassi 
 Harjoitustyön aiheena on ostoskassi. Sovelluksen käyttäjä voi kirjautua
ostoskassi -sovellukseen ja lisätä ostoslistalle haluamiaan tuotteita. Jos 
tuotetta ei ole vielä olemassa, niin käyttäjä voi lisätä kyseisen tuotteen 
itse. Lisäksi käyttäjä voi poistaa ostoskassinsa kokonaan, luoda uuden 
ostoskassin, tutkia tai muokata sen sisältöä ja eri tuotteiden määrää ostoskassissa.
Käyttäjä pystyy lisäämään ja poistamaan tuotteen. 
Lisäksi hän voi päivittää tuotteen hintaa ja pääsee näkemään olemassa olevat tuotteet.
Jokaisella tuotteella on oma kategoria. Kategorioiden avulla voidaan 
tehdä hakuja, joiden perusteella nähdään paljonko rahaa on käytetty
esimerkiksi herkkuihin asiakkaan ostoskasseissa.

Valmiit kategoriat (ei voida muuttaa):
* Valmisruoat
* Perushygienia
* Siivous
* HeVi
* Herkut
 
Alustavat tietokantataulut:
[![Tietokantataulujen väliset suhteet](/Tsoha_2019/tietokantatalulu.png)]

[Kayttaja|(pk)id:Integer, kayttajatunnus:String, sahkoposti:String, salasana:String]

[Ostoskassi|(pk)id:Integer,(fk) kayttaja_id -> Kayttaja, yhteishinta:Double, ostosMaara:Integer]

[Tuote|(pk)id:Integer, nimi:String, hinta:Double]

[OstoskassiTuote|(fk)tuote_id -> Tuote, (fk)ostoskassi_id -> Ostoskassi, tuoteMaara:Integer]

[Kategoria|(pk)id:Integer, kategoria:String]

[Kayttaja]1-*[Ostoskassi]

[Ostoskassi]1-*[OstoskassiTuote]

[OstoskassiTuote]*-1[Tuote]

[Tuote]*-1[Kategoria]
