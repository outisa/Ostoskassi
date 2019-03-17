### Ensimmäinen käyttötapaus

* _Käyttäjä:_ sovelluksen käyttäjä

* _Tavoite:_ Ostoskassin luominen

* _Laukaisija:_ Käyttäjän halu kirjata ostoslista.

* _Esiehto:_ Käyttäjä on kirjautunut sovellukseen ja tuotelistalle on lisätty tuotteita.

* _Jälkiehto:_ Ostoskassiin on lisätty käyttäjän haluamat tuotteet.

* _Käyttötapauksen kulku:_ 
  
    1. Käyttäjä luo uuden ostoskassin.

    2. Käyttäjä lisää ostoskassiin tuotteita ostoslistalta.

    3. Käyttäjälle näytetään lista ostoskassin sisällöstä ja sen kokonaissumma.

* _Poikkeuksellinen toiminta_

   2a. Ostoskassiin ei voi valita tuotteita, jos ostoslista on tyhjä.

   2b. Käyttäjä ei löydä haluamaansa tuotetta listalta, jolloin se pitää lisätä ensin tuotelistaan.


### Toinen käyttötapaus

* _Käyttäjä:_ sovelluksen käyttäjä

* _Tavoite:_ Ostoskassin muokkaus

* _Laukaisija:_ Ostoskassin sisältö ei vastaa käyttäjän toiveita

* _Esiehto:_ Ostoskassi on luotu ja käyttäjä on kirjautuneena

* _Jälkiehto:_ Ostoskassin sisältö on muokattu

* _Käyttötapauksen kulku:_

    1. Käyttäjä avaa ostoskassin, jota hän haluaa muokata.

    2. Käyttäjä voi lisätä uuden tuotteen.

    3. Käyttäjä voi poistaa kassista tuotteen.

* _Poikkeuksellinen toiminta:_

    1a. Käyttäjän haluama tuote puuttuu listalta.


### Kolmas käyttötapaus

* _Käyttäjä:_ sovelluksen käyttäjä

* _Tavoite:_ Tuotteen luominen tuotelistalle

* _Laukaisija:_ Tuotelista on tyhjä tai tarvittu tuote puuttuu listalta.

* _Esiehto:_  Käyttäjä on kirjautuneena ja lisättävää tuotetta ei ole listalla

* _Jälkiehto:_ Tuote lisätään tuotelistalle

* _Käyttötapauksen kulku:_

   1. Käyttäjä lisää tuotteen nimen.

   2. Käyttäjä antaa tuotteelle hinnan.

   3. Käyttäjä määrittelee tuotteen kategorian valmiista kategorialistalta.

* _Pokkeuksellinen tilanne:_

   1a. Tuotteen nimi löytyy jo listalta.


### Neljäs käyttötapaus

* _Käyttäjä:_ Sovelluksen käyttäjä

* _Tavoite:_ Tuotelistan päivitys

* _Laukaisija:_ Tuotteella on väärä hinta tai kategoria

* _Esiehto:_ Muokattava tuote löytyy tuotelistalta ja käyttäjä on kirjautuneena

* _Jälkiehto:_ Tuoteen tiedot ovat päivitetty.

* _Käyttötapauksen kulku:_

    1. Muokattava tuote valitaan päivitettäväksi.

    2. Päivitettävältä tuotteelta muokataan hinta tai kategoria. 


### Viides käyttötapaus

* _Käyttäjä:_ Sovelluksen käyttäjä

* _Tavoite:_ Tuotekohta   
