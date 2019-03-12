## Ostoskassi 
 Harjoitustyön aiheena on ostoskassi. Sovelluksen käyttäjä voi kirjautua
ostoskassi -sovellukseen ja lisätä ostoslistalle haluamiaan tuotteita. Jos 
tuotetta ei ole vielä olemassa, niin käytääjä voi lisätä kyseisen tuotteen 
itse. Lisäksi käyttäjä voi poistaa ostoskassinsa kokonaan, luoda uuden 
ostoskassin tai muokata sen sisältöä.
Jokaisella tuotteella on oma kategoria. Kategorioiden perusteella voidaan 
tehdä hakuja, joiden perusteella nähdään paljonko on käytetty rahaa
esimerkiksi herkkuihin asiakkaan ostoskasseissa.

Valmiit kategoriat (ei voida muuttaa):
* Valmisruoat
* Perushygienia
* Siivous
* HeVi
* Herkut
 
Alustavat tietokantataulut:
[Kayttaja|(pk)id:Integer, kayttajatunnus:String, sahkoposti:String, salasana:String]
[Ostoskassi|(pk)id:Integer,(fk) kayttaja_id -> Kayttaja, yhteishinta:Integer, ostosMaara:Integer]
[Tuote|(pk)id:Integer, nimi:String]
[OstoskassiTuote|(fk)tuote_id -> Tuote, (fk)ostoskassi_id -> Ostoskassi]
[Kategoria|(pk)id:Integer, kategoria:String]

[Kayttaja]1-*[Ostoskassi]
[Ostoskassi]1-*[OstoskassiTuote]
[OstoskassiTuote]*-1[Tuote]
[Tuote]*-1[Kategoria]
