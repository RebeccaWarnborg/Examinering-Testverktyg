Feature: Hantera böcker på boksidan

  Scenario: Användare kan lägga till en ny bok
    Given att jag har öppnat boksidan
    When jag klickar på "Lägg till bok" och fyller i titel och författare
    Then ska boken sparas och visas i katalogen