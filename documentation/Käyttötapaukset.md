## Kategoria

_Tapahtuma:_ | Kategorian luominen
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Kategorian luonti 
_Laukaisija:_ | Kategorialista on tyhjä tai sieltä puuttuu haluttu kategoria.
_Esiehto:_ | Käyttäjä on kirjautunut 
_Jälkiehto:_ | Uusi kategoria on luotu
_Käyttötapauksen kulku:_ | 1. Käyttäjä antaa kategorialle sitä kuvaavan nimen. 2. Käyttäjä lisää kategorian.

Käyttötapaukseen liittyvät SQL-kyselyt:

INSERT INTO Category (category, account_id) VALUES (?,?);

parametrit: Käyttäjän antama kategoria, automaattisesti haettava käyttäjän id.

_Tapahtuma:_ | Kategorioiden listaus ja katselu
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Kategorialistan luonti 
_Laukaisija:_ | Halutaan nähdä kaikki kategoriat
_Esiehto:_ |  Käyttäjä on kirjautunut 
_Jälkiehto:_ | Kategoriat on listattu
_Käyttötapauksen kulku:_ | 1. Käyttäjä painaa listaa kategoriat nappia 2. Käyttäjä ohjautuu sivulle, jossa kategoriat ovat listattuna.

Käyttötapaukseen liittyvät SQL-kyselyt:

SELECT category FROM Category WHERE account_id = ?;

Parametrit: käyttäjän id

_Tapahtuma:_ | Kategorioiden muokkaus ja poisto
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Kategorialistan muokkaus 
_Laukaisija:_ | Halutaan muokata jotakin kategoriaa sopivammaksi.
_Esiehto:_ | Käyttäjä on kirjautunut
_Jälkiehto:_ | Kategorian nimi on muokattu
_Käyttötapauksen kulku:_ | 1. Käyttäjä painaa listaa kategoriat nappia 2. Käyttäjä ohjautuu sivulle,jossa kategoriat ovat listattuna. 3. Käyttäjä kirjoittaa kategorialle uuden nimen tekstikenttään. 4. Käyttäjä lisää uuden nimen kategorialle. 5. Käyttäjä voi poistaa itselleen ylimääräisen kategorian.
 _Poikkeuksellinen toiminta:_ | 3a. Listalla ei ole yhtään kategoriaa. 5a. Kategoria on jollakin tuotteella käytössä.
 
Käyttötapaukseen liittyvät SQL-kyselyt:

1.SELECT category FROM Category WHERE account_id = ?;

Parametrit: käyttäjän id

Päivitys:

4. UPDATE CATEGORY SET category = ? WHERE Category.id = ?;

Parametrit: päivitettävän kategorian id

Poisto:

5. DELETE FROM Category WHERE Category.id = ?;

Parametrit: poistettavan kategorian id

## Käyttäjätili

 _Tapahtuma:_ | Tilin luonti
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Uuden tilin luonti 
_Laukaisija:_ | Halutaan luoda tili, jolla kirjautua sovellukseen
_Esiehto:_ | Sovellus on auki 
_Jälkiehto:_ | Uusi tili on luotu
_Käyttötapauksen kulku:_ | 1. Käyttäjä painaa create account-nappia 2. Käyttäjä ohjautuu tilinluomissivulle 3. Käyttäjä syöttää tunnuksen ja salasanan (molemmissa vähintään kolme merkkiä 5. Käyttäjä luo tunnuksen. 6. Käyttäjä kirjautuu automaattisesti sisään.
 _Poikkeuksellinen toiminta:_ | 4a. Tunnus on jo käytössä 

Käyttötapaukseen liittyvät SQL-kyselyt:

INSERT INTO Account (username, password) VALUES (?, ?);

Parametrit: käyttäjän antama tunnus, käyttäjän antama salasana

Kirjautuneena ollessaan käyttäjä voi kirjatua ulos ja poistaa tilin halutessaan.

Tilin poistamiseen liittyvät SQL-kyselyt:

DELETE FROM Account WHERE account.id = ?;

Parametrit: Käyttäjän id

## Ostoslista

_Tapahtuma:_ | Ostoslistan luominen
--- | ---
 _Käyttäjä:_ | Sovelluksen käyttäjä 
 _Tavoite:_ | Ostoslistan luominen
_Laukaisija:_ | Käyttäjän halu luoda ostoslista. 
_Esiehto:_ | Käyttäjä on kirjautunut sovellukseen.
_Jälkiehto:_ | Ostoslista on luotu.
 _Käyttötapauksen kulku:_  |1. Käyttäjä luo uuden ostoslistan ja antaa sille nimen.
 _Poikkeuksellinen toiminta:_ | 
 
 Käyttötapaukseen liittyvät SQL-kyselyt:
 
 INSERT INTO Shoppinglist (name, account_id) VALUES (?, ?);
 
 Parametrit: listalle annettu nimi, käyttäjän id

_Tapahtuma:_ | Ostotslistojen listaus ja katselu
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Ostoslistan luonti 
_Laukaisija:_ | Halutaan nähdä kaikki ostoslistat
_Esiehto:_ |  Käyttäjä on kirjautunut 
_Jälkiehto:_ | Ostoslistat on listattu
_Käyttötapauksen kulku:_ | 1. Käyttäjä painaa listaa ostoslistat linkkiä 2. Käyttäjä ohjautuu sivulle, jossa ostoslistat ovat listattuna luontijärjestyksessä uusin ensin.

Käyttötapaukseen liittyvät SQL-kyselyt:

SELECT Shoppinglist.id, Shoppinglist.name FROM Shoppinglist
WHERE account_id = ? ORDER_BY Shoppinglist.date DESC;

Parametrit: Käyttäjän id

_Tapahtuma:_ | Ostoslistan muokkaus ja sisällön katselu
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Ostoslistan muokkaus
_Laukaisija:_ | Ostoslistan sisältö ei vastaa käyttäjän toiveita
_Esiehto:_ | Ostoslista on luotu ja käyttäjä on kirjautuneena
_Jälkiehto:_ | Ostoslistan sisältö on muokattu
_Käyttötapauksen kulku:_ | 1. Käyttäjä avaa listan ostoslistoista 2. Käyttäjä avaa sen ostoslistan, jota hän haluaa muokata. 3. Käyttäjä voi lisätä listaan uuden tuotteen. 4. Käyttäjä voi muokata tuotteen määrää listalla antamalla uuden halutun tuotemäärän väliltä 1-100. 5. Käyttäjä voi poistaa listalta tuotteen antamalla tuotteen määräksi 0. 
_Poikkeuksellinen toiminta:_ | 1a. Käyttäjän haluama tuote puuttuu listalta.

Käyttötapaukseen liittyvät SQL-kyselyt:

2. SELECT Shoppinglist.id, Product.id, Product.name, Category.category, Product.price, Shoppinglistproduct.product_total
   (ShoppinglistProduct.product_total * Product.Price) FROM Shoppinglist
   JOIN Shoppinglistproduct ON Shoppinglistproduct.shoppinglist_id = Shoppinglist.id
   JOIN Product ON Shoppinglistproduct.product_id = Product.id
   JOIN Category ON Product.category_id = Category.id
   WHERE Shoppinglist.id = ? ORDER BY Category.category;

Parametrit: ostoslistan id

3. INSERT INTO Shoppinglistproduct (shoppinglist_id, product_id, product_total) VALUES (?, ?, ?);

Parametrit: ostoslistan id, tuotteen id, ja tuotteiden määrä

4. UPDATE Shoppinglistproduct SET product_total = ?
WHERE shoppinglist_id = ? AND product_id = ?;

Parametrit: Tuotteen määrä, ostoslistan id, tuotteen id

5. DELETE FROM Shoppinglistproduct
WHERE shoppinglist_id = ? AND product_id = ?;

Parametrit: Ostoslistan id, tuotteen id

_Tapahtuma:_ | Ostoslistan poisto
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Ostoslistan poisto
_Laukaisija:_ | Ostoslista halutaan poistaa
_Esiehto:_ | Ostoslista on luotu ja käyttäjä on kirjautuneena
_Jälkiehto:_ | Ostoslista on poistettu
_Käyttötapauksen kulku:_ | 1. Käyttäjä avaa listan ostoslistoista. 2. Käyttäjä poistaa listan.
_Poikkeuksellinen toiminta:_ | 

Käyttötapaukseen liittyvät SQL-kyselyt:

DELETE FROM Shoppinglist WHERE Shoppinglist.id = ?;

Parametrit: Ostoslistan id

## Tuote

_Tapahtuma:_ | Tuotelistan luominen
--- | ---
_Käyttäjä:_ | sovelluksen käyttäjä
_Tavoite:_ | Tuotteen luominen tuotelistalle
_Laukaisija:_ | Tuotelista on tyhjä tai tarvittava tuote puuttuu listalta.
_Esiehto:_  | Käyttäjä on kirjautuneena ja haluttu tuotekategoria on olemassa.
_Jälkiehto:_ | Tuote lisätään tuotelistalle
_Käyttötapauksen kulku:_ | 1. Käyttäjä lisää tuotteen nimen. 2. Käyttäjä antaa tuotteelle hinnan. 3. Käyttäjä määrittelee tuotteen kategorian kategorialistalta.
_Pokkeuksellinen tilanne:_ | 3a Kategoriaa ei ole olemassa.

Käyttötapaukseen liittyvät SQL-kyselyt:

INSERT INTO Product (name, price, category_id) VALUES (?, ?, ?);

Parametrit: Käyttäjän antamat nimi, hinta sekä käyttäjän valiteman kategorian id.

_Tapahtuma:_ | Tuotteiden listaus ja katselu
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Tuotelistan luonti 
_Laukaisija:_ | Halutaan nähdä kaikki tuotteet
_Esiehto:_ |  Käyttäjä on kirjautunut 
_Jälkiehto:_ | Tuotteet on listattu
_Käyttötapauksen kulku:_ | 1. Käyttäjä painaa listaa tuotteet linkkiä 2. Käyttäjä ohjautuu sivulle, jossa tuotteet ovat listattuna.

Käyttötapaukseen liittyvät SQL-kyselyt:

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
_Laukaisija:_ | Tuotteella on väärä hinta
_Esiehto:_ | Muokattava tuote löytyy tuotelistalta ja käyttäjä on kirjautuneena
_Jälkiehto:_ | Tuoteen tiedot ovat päivitetty.
_Käyttötapauksen kulku:_ | 1. Käyttäjä avaa tuotelistan 2. Päivitettävältä tuotteelta muokataan hinta. 3. Tehdään päivitys.

Käyttötapaukseen liittyvät SQL-kyselyt:

Ensin tehdään Tuotelistan listauksessa oleva listauskysely, jossa listataan tuotteet.

UPDATE Product SET price = ? WHERE Product.id = ?;

Parametrit: uusi hinta, tuotteen id.
 
_Tapahtuma:_  | Tuoteen poisto
--- | ---
_Käyttäjä:_ |  Sovelluksen käyttäjä
_Tavoite:_ | Tuotteen poisto tuotelistalta
_Laukaisija:_ | Tuotetta ei haluta pitää tuotelistalla
_Esiehto:_ | Käyttäjä on kirjautuneena ja tuote on olemassa
_Jälkiehto:_ | Tuote on poistettu.
_Käyttötapauksen kulku:_ | 1. Käyttäjä avaa tuotelistan 2. Painetaan delete product-nappia.

Käyttötapaukseen liittyvät SQL-kyselyt:

Ensin tehdään Tuotelistan listauksessa oleva listauskysely, jossa listataan tuotteet.

DELETE FROM Product WHERE Product.id = ?;

Parametrit: Tuotteen id.

 
 **Tarkennetaan myöhemmin:**
 
 _Tapahtuma:_ | Haut
 --- | ---
 _Käyttäjä:_ | Sovelluksen käyttäjä
 _Tavoite:_ | Haut kategorian tai tuotteen perusteella.
 _Laukaisija:_ | Halutaan tietää tuote tai kategoriakohtaiset menot
 _Esiehto:_ | Ainakin yksi ostoslista on luotu
 _Jälkiehto:_ | Käyttäjällä saa haluamansa haun tulokset
 _Käyttötapauksen kulku:_ | 1. Valitaan haun tyyppi.
