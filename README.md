Examinering – Testautomatisering med Behave och Playwright

Vad jag har testat:
- Att en användare kan lägga till en bok genom att fylla i titel och författare
- Att boken sparas och visas korrekt i listan under fliken "Katalog"

Så här kör du projektet:

1. Skapa och aktivera en virtuell miljö:
python -m venv venv
venv\Scripts\activate

Om det inte funkar skriv följande i terminalen:
set-ExecutionpolicyPolicy -Scope Process -ExecutionPolicy Bypass

2. Installera beroenden från requirements.txt:
pip install -r requirements.txt

3. Kör testerna:
behave

Inga page-objekt har behövts för detta enkla test. All testlogik ligger i features/steps/test_steps.py.