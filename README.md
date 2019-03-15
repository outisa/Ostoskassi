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
esimerkiksi herkkuihin kaikissa (asiakkaan) ostoskasseissa.

Valmiit kategoriat (ei voida muuttaa):
* Valmisruoat
* Perushygienia
* Siivous
* HeVi
* Herkut
 
Alustavat tietokantataulut:


![Tietokantataulu](/documentation/tietokantakaavio.png)

Tietokantakaavioiden lyhyt (vaillinainen) kuvaus:

**Kayttaja:**

**id** on kokonaisluku ja samalla pääavain, joka luodaan automaattisesti tunnuksia tehdessä.

**kayttajatunnus** on käyttäjän antama merkkijono.

**sahkoposti** on käyttäjän antama merkkijono ja järjestelmään ei voida tehdä useita tunnuksia yhdellä sahkopostilla. 

**salasana** on käyttäjän antama merkkijono

**Ostoskassi:**

**id** on kokonaisluku ja samalla taulun pääavain, joka muodostuu ostoskassia luodessa.

**kayttaja_id** on kokonaisluku ja se viittaa kayttaja -tauluun.

**yhteishinta** merkitään muodossa xxx.xx ja se muodostuu ostoskassiin lisättyjen tuotteiden hinnasta.

**ostosMaara** on kokonaisluku ja se kertoo ostoskassiin lisättyjen tuotteiden yhteismäärän.

**Tuote:**

**id** kokonaisluku ja taulun pääavain. Muodostuu automaattisesti luotaessa tuotetta.

**nimi** on tuotteen nimeä kuvaava merkkijono.

**hinta** on muotoa xxx.xx ja sen voi tarvittaessa muuttaa.

**OstoskassiTuote:**

**tuote_id** kokonaisluku, joka viittaa Tuote -tauluun.

**ostoskassi_id** kokonaisluku, joka viittaa Ostoskassiin. 

**tuoteMaara** kokonaisluku, joka kertoo kyseisen tuotteen määrän tuotteeseen liitetyssä ostoskassissa.

**Kategoria:**

**id** on kokonaisluku ja taulun pääavain.

**kategoria** on merkkijonomuotoinen ja kertoo kategorian nimen. Käyttäjä ei voi muokata tätä osiota.
