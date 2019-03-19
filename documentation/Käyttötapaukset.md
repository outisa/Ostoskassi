
_Tapahtuma:_ | Kategorian luominen
--- | ---
_Käyttäjä:_ | Sovelluksen käyttäjä
_Tavoite:_ | Kategorian luonti 
_Laukaisija:_ | Kategorialista on tyhjä tai sieltä puuttuu haluttu kategoria.
_Esiehto:_ | Käyttäjä on kirjautunut
_Jälkiehto:_ | Uusi kategoria on luotu
_Käyttötapauksen kulku:_ | 1. Käyttäjä antaa kategorialle sitä kuvaavan nimen. 2. Käyttäjä lisää kategorian.

**Toiminnallisuutta ei olla vielä luotu seuraavissa käyttötapauksissa:**

_Tapahtuma:_ | Ostoskassin luominen
--- | ---
 _Käyttäjä:_ | sovelluksen käyttäjä 
 _Tavoite:_ | Ostoskassin luominen
_Laukaisija:_ | Käyttäjän halu kirjata ostoslista. 
_Esiehto:_ | Käyttäjä on kirjautunut sovellukseen ja tuotelistalle on lisätty tuotteita.
_Jälkiehto:_ | Ostoskassiin on lisätty käyttäjän haluamat tuotteet.
 _Käyttötapauksen kulku:_  |1. Käyttäjä luo uuden ostoskassin.  2. Käyttäjä lisää ostoskassiin tuotteita tuotelistalta 3.Käyttäjälle näytetään lista ostoskassin sisällöstä ja sen kokonaissumma.
 _Poikkeuksellinen toiminta:_ | 2a. Ostoskassiin ei voi valita tuotteita, jos ostoslista on tyhjä. 2b. Käyttäjä ei löydä haluamaansa tuotetta listalta, jolloin se pitää lisätä ensin tuotelistaan.


_Tapahtuma:_ | Ostoskassin muokkaus
--- | ---
_Käyttäjä:_ | sovelluksen käyttäjä
_Tavoite:_ | Ostoskassin muokkaus
_Laukaisija:_ | Ostoskassin sisältö ei vastaa käyttäjän toiveita
_Esiehto:_ | Ostoskassi on luotu ja käyttäjä on kirjautuneena
_Jälkiehto:_ | Ostoskassin sisältö on muokattu
_Käyttötapauksen kulku:_ | 1. Käyttäjä avaa ostoskassin, jota hän haluaa muokata. 2. Käyttäjä voi lisätä uuden tuotteen. 3.Käyttäjä voi poistaa kassista tuotteen.
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
 _Esiehto:_ | Ainakin yksi ostoskassi on luotu
 _Jälkiehto:_ | Käyttäjällä saa haluamansa haun tulokset
 _Käyttötapauksen kulku:_ | 1. Valitaan haun tyyppi.
