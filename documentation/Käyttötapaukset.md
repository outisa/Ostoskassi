## Kategoria

_Tapahtuma:_ | Kategorian luominen
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Kategorian luonti 
_Laukaisija:_ | Kategorialistalta puuttuu haluttu kategoria.
_Esiehto:_ | Käyttäjä on kirjautunut 
_Jälkiehto:_ | Uusi kategoria on luotua
_Käyttötapauksen kulku:_ | 1. Käyttäjä siirtyy _Manage Categories_ linkin kautta näkymään, jossa voi lisätä kategorian. 2. Käyttäjä antaa kategorialle sitä kuvaavan nimen. 3. Käyttäjä lisää kategorian.
_Pokkeuksellinen toiminta:_ | 3a. Kategoria löytyy jo käyttäjän listalta. 3b. Syötteen pituus on liian lyhyt tai pitkä 3c. Syötteessä on käytetty ei-sallittuja merkkejä. 

Käyttötapaukseen liittyvä kysely, jos kategoriaa ei löydy listalta:

INSERT INTO Category (category, account_id) VALUES (?,?);

parametrit: Käyttäjän antama kategoria, automaattisesti haettava käyttäjän id.

_Tapahtuma:_ | Kategorioiden listaus ja katselu
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Kategorialistan luonti 
_Laukaisija:_ | Halutaan nähdä kaikki kategoriat
_Esiehto:_ |  Käyttäjä on kirjautunut 
_Jälkiehto:_ | Kategoriat on listattu
_Käyttötapauksen kulku:_ | 1. Käyttäjä klikkaa _Manage Categories_ linkkiä.  2. Käyttäjä ohjautuu sivulle, jossa kategoriat ovat listattuna.

Käyttötapaukseen liittyvä SQL-kysely

SELECT category FROM Category WHERE account_id = ? OR account.id = 0;

Parametrit: käyttäjän id

_Tapahtuma:_ | Kategorioiden muokkaus
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Kategorian muokkaus 
_Laukaisija:_ | Halutaan muokata jotakin kategoriaa sopivammaksi.
_Esiehto:_ | Käyttäjä on kirjautunut ja on kategorioiden listauksessa
_Jälkiehto:_ | Kategorian nimi on muokattu
_Käyttötapauksen kulku:_ | 1. Käyttäjä klikkaa kategorian nimeä, jolla päästään päivittämään kategoria. 2. Käyttäjä muokkaa kategorian nimeä. 
 _Poikkeuksellinen toiminta:_ | 1a. Kategoria ei ole oma (ei tapahdu mitään). 2b. Syöte ei ole validi.

Tapaukseen liittyvä SQL-kysely

UPDATE CATEGORY SET category = ? WHERE Category.id = ?;

Parametrit: päivitettävän kategorian id


_Tapahtuma:_ | Kategorioiden poisto
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Kategorian poisto 
_Laukaisija:_ | Halutaan poistaa kategoria.
_Esiehto:_ | Käyttäjä on kirjautunut ja on kategorioiden listauksessa
_Jälkiehto:_ | Kategoria on poistettu.
_Käyttötapauksen kulku:_ | 1. Käyttäjä klikkaa itse luomansa kategorian vieressä olevaa _Delete_ nappia.
 _Poikkeuksellinen toiminta:_ | 1a. Kategoria on jollakin tuotteella käytössä.

Tarkistetaan ensin onko kategoria käytössä

SELECT * FROM Product WHERE Product.category_id= ?;

Jos yhtään tuotetta ei löytynyt, poistetaan kategoria. (Jos kategoria on käytössä, kerrotaan käyttäjälle poiston olevan mahdotonta.)

DELETE FROM Category WHERE Category.id = ?;

Parametrit: poistettavan kategorian id

## Käyttäjätili

 _Tapahtuma:_ | Tilin luonti
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Uuden tilin luonti 
_Laukaisija:_ | Halutaan luoda tili, jolla kirjautua sovellukseen
_Esiehto:_ | Sovellus on auki 
_Jälkiehto:_ | Uusi tili on luotu
_Käyttötapauksen kulku:_ | 1. Käyttäjä painaa create account-nappia 2. Käyttäjä ohjautuu tilinluomissivulle 3. Käyttäjä syöttää haluamansa tunnuksen ja salasanan. 4. Käyttäjä luo tunnuksen. 5. Käyttäjä kirjautuu automaattisesti sisään.
 _Poikkeuksellinen toiminta:_ | 4a. Syöte ei ole validi. 4b. Tunnus on jo käytössä. 

Käyttötapaukseen liittyvä SQL-kysely

INSERT INTO Account (username, password) VALUES (?, ?);

Parametrit: käyttäjän antama tunnus, käyttäjän antama salasana

Kirjautuneena ollessaan käyttäjä voi kirjatua ulos ja poistaa tilin halutessaan.

Tilin poistamiseen liittyvät SQL-kyselyt:

Haetaan kaikki käyttäjän luomat tuotteet, yhteydet tuotteen ja ostoslistan välillä, ostoslistat ja kategoriat, sekä poistetaan ne järjestyksessä: yhteydet tuotteen ja ostoslistan välillä, tuotteet, kategoriat ja ostoslistat. Haut ovat normaaleja SELECT * FROM _taulunnimi_ -kyselyjä, joissa haetaan rivejä käyttäjän id:n perusteella. Poikkeuksena on liitostaulu Shoppinglistproduct, jossa rivejä haetaan tuotteen id:n perusteella.
Poistot ovat normaaleja DELETE FROM _taulunnimi_ WHERE account_id = ?; -kyselyjä, paitsi liitostaulusta poistetaan kyselyllä DELETE FROM Shoppinglistproduct WHERE product_id = ?.

Lopuksi poistetaan itse käyttäjä.

DELETE FROM Account WHERE Account.id = ?;

Parametrit: Käyttäjän id

## Ostoslista

_Tapahtuma:_ | Ostoslistan luominen
--- | ---
 _Käyttäjä:_ | Sovelluksen käyttäjä 
 _Tavoite:_ | Ostoslistan luominen
_Laukaisija:_ | Käyttäjän halu luoda ostoslista. 
_Esiehto:_ | Käyttäjä on kirjautunut sovellukseen ja on ostoslistojen listauksessa.
_Jälkiehto:_ | Ostoslista on luotu.
 _Käyttötapauksen kulku:_  |1. Käyttäjä antaa uudelle ostoslistalle nimen. 2. Käyttäjä luo kategorian. 
 _Poikkeuksellinen toiminta:_ | 1a. Syöte ei ole validi.
 
 Käyttötapaukseen liittyvä SQL-kysely:
 
 INSERT INTO Shoppinglist (name, account_id) VALUES (?, ?);
 
 Parametrit: listalle annettu nimi, käyttäjän id

_Tapahtuma:_ | Ostotslistojen listaus ja katselu
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Ostoslistan luonti 
_Laukaisija:_ | Halutaan nähdä kaikki ostoslistat
_Esiehto:_ |  Käyttäjä on kirjautunut 
_Jälkiehto:_ | Ostoslistat on listattu
_Käyttötapauksen kulku:_ | 1. Käyttäjä painaa _Manage Shoppinglists_ linkkiä 2. Käyttäjä ohjautuu sivulle, jossa ostoslistat ovat listattuna luontijärjestyksessä uusin ensin.

Käyttötapaukseen liittyvä SQL-kysely:

SELECT Shoppinglist.id, Shoppinglist.name FROM Shoppinglist
WHERE account_id = ? ORDER_BY Shoppinglist.date DESC;

Parametrit: Käyttäjän id

_Tapahtuma:_ | Ostoslistan sisällön katselu
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Ostoslistan sisällön listaus
_Laukaisija:_ | Käyttäjä haluaa selata ostoslistan sisältöä
_Esiehto:_ | Ostoslista on luotu, käyttäjä on kirjautuneena
_Jälkiehto:_ | Ostoslistan sisältö on listattu
_Käyttötapauksen kulku:_ | 1. Käyttäjä klikkaa sen ostoslistan _Show content_ nappia, minkä sisältö hän haluaa tarkastella.
_Poikkeuksellinen toiminta:_ | 1a. Ostoslista on tyhjä, jolloin listauksessa ei näy yhtään tuotetta.

Käyttötapaukseen liittyvä SQL-kysely

SELECT Product.id, Product.name, Category.category, Product.price, Shoppinglistproduct.product_total,  
   (Shoppinglistproduct.product_total * Product.Price),  
   (SELECT SUM(Shoppinglistproduct.product_total * Product.Price) FROM Shoppinglistproduct JOIN Product ON Shoppinglistproduct.product_id = Product.id WHERE Shoppinglistproduct.shoppinglist_id = ?) FROM Shoppinglistproduct   
   JOIN Product ON Shoppinglistproduct.product_id = Product.id  
   JOIN Category ON Product.category_id = Category.id 
   WHERE Shoppinglistproduct.shoppinglist_id = ?  
   GROUP BY Product.id, Product.name, Category.category, Product.price, Shoppinglistproduct.product_total  
   ORDER BY Category.category;
 
Parametrit: ostoslistan id

_Tapahtuma:_ | Ostoslistan sisällön lisäys
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Tuotteen lisäys ostoslistaan
_Laukaisija:_ | Ostoslistan sisältö ei vastaa käyttäjän toiveita
_Esiehto:_ | Ostoslista on luotu, käyttäjä on kirjautuneena ja on ostoslistojen listauksessa
_Jälkiehto:_ | Ostoslistalle on lisätty tuote
_Käyttötapauksen kulku:_ | 1. Käyttäjä voi lisätä listaan uuden tuotteen, valitsemalla tuotteen nimen valikosta ja syöttämällä tuotteen määrän syötekenttään väliltä 1-100. 2. Käyttäjä klikkaa _Add_ nappia. 
_Poikkeuksellinen toiminta:_ | 1a. Käyttäjän haluama tuote puuttuu tuotelistalta. 1b. Syöte tuotteen määrälle ei ole validi.
 
Käyttötapaukseen liittyvä SQL-kysely

INSERT INTO Shoppinglistproduct (shoppinglist_id, product_id, product_total) VALUES (?, ?, ?);

Parametrit: ostoslistan id, tuotteen id, ja tuotteiden määrä

_Tapahtuma:_ | Ostoslistan sisällön muokkaus
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Ostoslistan sisällön muokkaus
_Laukaisija:_ | Ostoslistan sisältö ei vastaa käyttäjän toiveita
_Esiehto:_ | Ostoslista on luotu, käyttäjä on kirjautuneena ja on ostoslistojen listauksessa
_Jälkiehto:_ | Ostoslistan sisältö on muokattu
_Käyttötapauksen kulku:_ | 1. Käyttäjä voi muokata jo lisätyn tuotteen määrää listalla valitsemalla tuotteen valikosta ja antamalla uuden halutun tuotemäärän väliltä 1-100. 
_Poikkeuksellinen toiminta:_ | 1a Syöte ei ole validi.

Käyttötapaukseen liittyvä SQL-kysely

UPDATE Shoppinglistproduct SET product_total = ? WHERE shoppinglist_id = ? AND product_id = ?;

Parametrit: Tuotteen määrä, ostoslistan id, tuotteen id

_Tapahtuma:_ | Tuotteen poisto ostoslistalta
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Tuotteen poisto ostoslistalta
_Laukaisija:_ | Ostoslistan sisältö ei vastaa käyttäjän toiveita
_Esiehto:_ | Ostoslista on luotu, käyttäjä on kirjautuneena ja on ostoslistojen listauksessa
_Jälkiehto:_ | Tuote on poistettu ostoslistalta
_Käyttötapauksen kulku:_ | 1. Käyttäjä voi poistaa tuotteen ostoslistalta klikkaamalla _Delete_ -nappia tuotteen kohdalta.

Käyttötapaukseen liittyvät SQL-kysely

DELETE FROM Shoppinglistproduct WHERE shoppinglist_id = ? AND product_id = ?;

Parametrit: Ostoslistan id, tuotteen id

_Tapahtuma:_ | Ostoslistan poisto
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Ostoslistan poisto
_Laukaisija:_ | Ostoslista halutaan poistaa
_Esiehto:_ | Ostoslista on luotu, käyttäjä on kirjautuneena ja on ostoslistojen listauksessa
_Jälkiehto:_ | Ostoslista on poistettu
_Käyttötapauksen kulku:_ | 1. Käyttäjä poistaa haluamansa listan painamalla _Delete_ nappia poistettavan ostoslistan vierestä.
_Poikkeuksellinen toiminta:_ | 

Käyttötapaukseen liittyvät SQL-kyselyt:

Ennen ostoslistan poistoa haetaan kaikki ostoslistaan liittyvät rivit Shoppiglistproduct liitostaulusta ja poistetaan ne.

SELECT * FROM Shoppinglistproduct WHERE shoppinglist_id = ?;

parametrit: ostoslistan id

Poisto jokaiselle haetulle liitostaulun riville tapahtuu kyselyllä:

DELETE FROM Shoppinglistproduct WHERE shoppinglist_id = ?, product_id = ?, total_product = ?;

parametrit: ostoslistan id, tuotteen id, tuotteen määrä

Varsinaninen ostoslistan poisto tapahtuu suorittamalla kysely 

DELETE FROM Shoppinglist WHERE Shoppinglist.id = ?;

Parametrit: Ostoslistan id

## Tuote

_Tapahtuma:_ | Tuotteen luominen
--- | ---
_Käyttäjä:_ | sovelluksen käyttäjä
_Tavoite:_ | Tuotteen luominen tuotelistalle
_Laukaisija:_ | Tuotelista on tyhjä tai tarvittava tuote puuttuu listalta.
_Esiehto:_  | Käyttäjä on kirjautuneena, haluttu tuotekategoria on olemassa ja käyttäjä on tuotteiden listaussivulla.
_Jälkiehto:_ | Tuote lisätään tuotelistalle
_Käyttötapauksen kulku:_ | 1. Käyttäjä lisää tuotteen nimen. 2. Käyttäjä antaa tuotteelle hinnan. 3. Käyttäjä määrittelee tuotteen kategorian kategorialistalta. 4. Käyttäjä lisää tuotteen.
_Pokkeuksellinen tilanne:_ | 1a. Syöte ei ole validi 2a Syöte ei ole validi. 3a. Haluttua kategoriaa ei ole olemassa. 4a. Samanniminen tuote on jo olemassa.

Käyttötapaukseen liittyvä SQL-kysely

INSERT INTO Product (name, price, category_id) VALUES (?, ?, ?);

Parametrit: Käyttäjän antamat nimi, hinta sekä käyttäjän valitseman kategorian id.

_Tapahtuma:_ | Tuotteiden listaus ja katselu
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Tuotelistan luonti 
_Laukaisija:_ | Halutaan nähdä kaikki tuotteet
_Esiehto:_ |  Käyttäjä on kirjautunut 
_Jälkiehto:_ | Tuotteet on listattu
_Käyttötapauksen kulku:_ | 1. Käyttäjä painaa _Manage Products_ linkkiä 2. Käyttäjä ohjautuu sivulle, jossa tuotteet ovat listattuna.

Käyttötapaukseen liittyvä SQL-kysely

SELECT Product.id, Product.name, Product.price, Category.category FROM Product  
JOIN Category ON Category.id = Product.category_id   
JOIN Account ON Account.id = Product.account_id  
WHERE Product.account_id = ?  
ORDER BY Product.name;

Parametrit: Käyttäjän id

_Tapahtuma:_  | Tuotelistan päivitys
--- | ---
_Käyttäjä:_ |  Sovelluksen käyttäjä
_Tavoite:_ | Tuotelistan päivitys
_Laukaisija:_ | Tuotteella on väärä hinta ja/tai nimi on väärin
_Esiehto:_ | Muokattava tuote löytyy tuotelistalta, käyttäjä on kirjautuneena ja on tuotteiden listauksessa
_Jälkiehto:_ | Tuoteen tiedot ovat päivitetty.
_Käyttötapauksen kulku:_ | 1. Käyttäjä avaa tuotelistan ja klikkaa tuotteen nimeä. 2. Päivitettävältä tuotteelle annetaan uusi nimi ja hinta. 3. Tehdään päivitys painamalla _Update_ nappia.
_Poikkeuksellinen toiminta:_ | 3a. Syöte ei ole validi. 3b. Tuotteen uusi nimi on käytössä jollakin muulla käyttäjän tuotteella.

Käyttötapaukseen liittyvä SQL-kysely

UPDATE Product SET name = ?, price = ? WHERE Product.id = ?;

Parametrit: uusi nimi, uusi hinta, tuotteen id.
 
_Tapahtuma:_  | Tuoteen poisto
--- | ---
_Käyttäjä:_ |  Sovelluksen käyttäjä
_Tavoite:_ | Tuotteen poisto tuotelistalta
_Laukaisija:_ | Tuotetta ei haluta pitää tuotelistalla
_Esiehto:_ | Käyttäjä on kirjautuneena, tuote on olemassa ja käyttäjä on tuotelistauksessa
_Jälkiehto:_ | Tuote on poistettu.
_Käyttötapauksen kulku:_ | 1. Painetaan _delete_ nappia sen tuotteen kohdalta, joka halutaan poistaa.

Käyttötapaukseen liittyvät SQL-kyselyt:

Haetaan kaikki Shoppinglistproduct rivit, joilla tuote on:

SELECT * FROM Shoppinglistproduct JOIN Product ON Shoppinglist.product_id = Product.id WHERE Product.id = ?;

parametrit: tuotteen id

Poistetaan ensin liitostaulun rivit, jotka saatiin edellisellä kyselyllä samallalailla kuin ostoslistan poistossa on tehty. Lopuksi poistetaan itse tuote.

DELETE FROM Product WHERE Product.id = ?;

Parametrit: Tuotteen id.
 
 _Tapahtuma:_ | Haku kategorioittain
 --- | ---
 _Käyttäjä:_ | Sovelluksen käyttäjä
 _Tavoite:_ | Käytetyn rahan listaus kategorioittain.
 _Laukaisija:_ | Halutaan tietää kategoriakohtaiset menot
 _Esiehto:_ | Ainakin yksi ostoslista on luotu ja käyttäjä on ostoslistojen listaussivulla.
 _Jälkiehto:_ | Käyttäjä saa haluamansa haun tulokset
 _Käyttötapauksen kulku:_ | 1. Painetaan _Show_ nappia, jolloin päästään näkymään, jossa on maksimissaan 15 kategoriaa listattuna. Jokaiselle kategorialle listauksessa näytetään käytetty rahasumma ja sen prosenttiosuus kokonaishinnasta. Kategorioista näytetään vain ne, joille on kertynyt ostoksia.

Käyttötapaukseen liittyvä SQL-kysely

SELECT DISTINCT Category.category, SUM(shoppinglistproduct.product_total * product.price) AS sum,  
SUM(shoppinglistproduct.product_total * product.price) * 100 / (SELECT SUM(shoppinglistproduct.product_total * product.price)   FROM Shoppinglist JOIN Shoppinglistproduct ON Shoppinglistproduct.shoppinglist_id = Shoppinglist.id JOIN Product ON   Shoppinglistproduct.product_id = product.id JOIN account ON account.id = Shoppinglist.account_id WHERE Product.account_id = ?) AS   percent FROM Shoppinglistproduct 
JOIN Product ON Shoppinglistproduct.product_id = product.id  
JOIN Shoppinglist ON   Shoppinglistproduct.shoppinglist_id = Shoppinglist.id  
JOIN account ON account.id = Product.account_id  
JOIN Category ON Category.id = Product.category_id WHERE Product.account_id = ?  
GROUP BY Category.category ORDER BY sum DESC LIMIT 15  

Parametrit: Käyttäjän id
