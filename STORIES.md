# Läslistan (Examineringsuppgift)

## User stories

**[U1]** Som en användare vill jag kunna lägga till en ny bok genom att fylla i titel och författare,  
så att jag kan bygga upp min personliga läslista.

**[U2]** Som en användare vill jag kunna se alla böcker jag lagt till under fliken "Katalog",  
så att jag kan hålla koll på vilka böcker som är sparade i min lista.

**[U3]** Som användare vill jag kunna lägga till en bok i "Min lista" genom att klicka på titeln i katalogen,  
så att jag kan spara mina favoriter.

**[U4]** Som användare vill jag kunna ta bort en bok från "Min lista" genom att klicka igen på hjärtat i katalogen,  
så att jag kan ångra favorisering.

## Acceptanskriterier

**[A1.1]** När jag klickar på "Lägg till bok" ska ett formulär visas där jag kan fylla i titel och författare.  
**[A1.2]** När jag fyller i titel och författare och trycker på "Lägg till ny bok", ska boken sparas.  
**[A2.1]** När jag trycker på fliken "Katalog", ska min tillagda bok visas i listan.  
**[A3.1]** När jag klickar på en bok i katalogen, ska boken läggas till i "Mina böcker".  
**[A4.1]** När jag klickar igen på hjärtat i katalogen, ska boken tas bort från "Mina böcker".

Testscenarier:

[T1]
1. Gå till sidan.
2. Klicka på "Lägg till bok".
3. Fyll i "Titel" med "Min Testbok".
4. Fyll i "Författare" med "Test Författare".
5. Klicka på "Lägg till ny bok".
6. Klicka på fliken "Katalog".
7. Kontrollera att boken "Min Testbok" visas i listan.

[T2]
1. Lägg till en bok (om ingen redan finns).
2. Gå till fliken "Katalog".
3. Klicka på bokens titel.
4. Gå till fliken "Mina böcker".
5. Kontrollera att boken visas i listan.

[T3]
1. Gå till fliken "Katalog".
2. Klicka på hjärtat på boken "Kaffekokaren som visste för mycket" för att ta bort den från listan.
3. Gå till fliken "Mina böcker".
4. Kontrollera att boken inte längre visas i listan.
