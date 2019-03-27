
_Tapahtuma:_ | Kategorian luominen
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Kategorian luonti 
_Laukaisija:_ | Kategorialista on tyhjä tai sieltä puuttuu haluttu kategoria.
_Esiehto:_ | Käyttäjä on kirjautunut 
_Jälkiehto:_ | Uusi kategoria on luotu
_Käyttötapauksen kulku:_ | 1. Käyttäjä antaa kategorialle sitä kuvaavan nimen. 2. Käyttäjä lisää kategorian.

_Tapahtuma:_ | Kategorioiden listaus ja katselu
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Kategorialistan luonti 
_Laukaisija:_ | Halutaan nähdä kaikki kategoriat
_Esiehto:_ |  Käyttäjä on kirjautunut 
_Jälkiehto:_ | Kategoriat on listattu
_Käyttötapauksen kulku:_ | 1. Käyttäjä painaa listaa kategoriat nappia 2. Käyttäjä ohjautuu sivulle, jossa kategoriat ovat listattuna.


_Tapahtuma:_ | Kategorioiden muokkaus ja poisto
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Kategorialistan muokkaus 
_Laukaisija:_ | Halutaan muokata jotakin kategoriaa sopivammaksi
_Esiehto:_ | Käyttäjä on kirjautunut
_Jälkiehto:_ | Kategorian nimi on muokattu
_Käyttötapauksen kulku:_ | 1. Käyttäjä painaa listaa kategoriat nappia 2. Käyttäjä ohjautuu sivulle,jossa kategoriat ovat listattuna. 3. Käyttäjä kirjoittaa kategorialle uuden nimen tekstikenttään. 4. Käyttäjä lisää uuden nimen kategorialle. 5. Käyttäjä voi poistaa itselleen ylimääräisen kategorian.
 _Poikkeuksellinen toiminta:_ | 3a. Listalla ei ole yhtään kategoriaa.
 
 _Tapahtuma:_ | Tilin luonti
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Uuden tilin luonti 
_Laukaisija:_ | Halutaan luoda tili, jolla kirjautua sovellukseen
_Esiehto:_ | Sovellus on auki 
_Jälkiehto:_ | Uusi tili on luotu
_Käyttötapauksen kulku:_ | 1. Käyttäjä painaa login-nappia 2. Käyttäjä ohjautuu login-sivulle 3. Käyttäjä painaa create an account -nappia 4. Käyttäjä syöttää tunnuksen ja salasanan (molemmissa vähintään kolme merkkiä) 5. Käyttäjä kirjaantuu login napilla.
 _Poikkeuksellinen toiminta:_ | 
 
 Tilin luomisen jälkeen käyttäjä voi kirjautua tilille tunnuksillaan, kirjatua ulos ja poistaa tilin halutessaan ollessaan kirjautuneena.
 
**Toiminnallisuutta ei olla vielä luotu seuraavissa käyttötapauksissa:**

_Tapahtuma:_ | Ostoslistan luominen
--- | ---
 _Käyttäjä:_ | sovelluksen käyttäjä 
 _Tavoite:_ | Ostoslistan luominen
_Laukaisija:_ | Käyttäjän halu kirjata ostoslista. 
_Esiehto:_ | Käyttäjä on kirjautunut sovellukseen ja tuotelistalle on lisätty tuotteita.
_Jälkiehto:_ | Ostoslistaan on lisätty käyttäjän haluamat tuotteet.
 _Käyttötapauksen kulku:_  |1. Käyttäjä luo uuden ostoslistan.  2. Käyttäjä lisää ostoslistaan tuotteita tuotelistalta 3.Käyttäjälle näytetään lista ostoslistan sisällöstä ja sen kokonaissumma.
 _Poikkeuksellinen toiminta:_ | 2a. Ostoslistaan ei voi valita tuotteita, jos tuotelista on tyhjä. 2b. Käyttäjä ei löydä haluamaansa tuotetta listalta, jolloin se pitää lisätä ensin tuotelistaan.


_Tapahtuma:_ | Ostoslistan muokkaus
--- | ---
_Käyttäjä:_ | sovelluksen käyttäjä
_Tavoite:_ | Ostoslistan muokkaus
_Laukaisija:_ | Ostoslistan sisältö ei vastaa käyttäjän toiveita
_Esiehto:_ | Ostoslista on luotu ja käyttäjä on kirjautuneena
_Jälkiehto:_ | Ostoslistan sisältö on muokattu
_Käyttötapauksen kulku:_ | 1. Käyttäjä avaa sen ostoslistan, jota hän haluaa muokata. 2. Käyttäjä voi lisätä listaan uuden tuotteen. 3.Käyttäjä voi poistaa listalta tuotteen.
_Poikkeuksellinen toiminta:_ | 1a. Käyttäjän haluama tuote puuttuu listalta.


_Tapahtuma:_ | Tuotelistan luominen
--- | ---
_Käyttäjä:_ | sovelluksen käyttäjä
_Tavoite:_ | Tuotteen luominen tuotelistalle
_Laukaisija:_ | Tuotelista on tyhjä tai tarvittu tuote puuttuu listalta.
_Esiehto:_  | Käyttäjä on kirjautuneena, lisättävää tuotetta ei ole listalla ja haluttu tuotekategoria on olemassa.
_Jälkiehto:_ | Tuote lisätään tuotelistalle
_Käyttötapauksen kulku:_ | 1. Käyttäjä lisää tuotteen nimen. 2. Käyttäjä antaa tuotteelle hinnan. 3. Käyttäjä määrittelee tuotteen kategorian kategorialistalta.
_Pokkeuksellinen tilanne:_ | 1a. Tuotteen nimi löytyy jo listalta.


_Tapahtuma:_  | Tuotelistan päivitys
--- | ---
_Käyttäjä:_ |  Sovelluksen käyttäjä
_Tavoite:_ | Tuotelistan päivitys
_Laukaisija:_ | Tuotteella on väärä hinta tai kategoria
_Esiehto:_ | Muokattava tuote löytyy tuotelistalta ja käyttäjä on kirjautuneena
_Jälkiehto:_ | Tuoteen tiedot ovat päivitetty.
_Käyttötapauksen kulku:_ | 1. Muokattava tuote valitaan päivitettäväksi. 2. Päivitettävältä tuotteelta muokataan hinta tai kategoria.
 
 **Tarkennetaan myöhemmin:**
 
 _Tapahtuma:_ | Haut
 --- | ---
 _Käyttäjä:_ | Sovelluksen käyttäjä
 _Tavoite:_ | Haut kategorian tai tuotteen perusteella.
 _Laukaisija:_ | Halutaan tietää tuote tai kategoriakohtaiset menot
 _Esiehto:_ | Ainakin yksi ostoslista on luotu
 _Jälkiehto:_ | Käyttäjällä saa haluamansa haun tulokset
 _Käyttötapauksen kulku:_ | 1. Valitaan haun tyyppi.
