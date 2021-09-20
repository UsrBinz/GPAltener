# GP Altener
GP Altener - tai įrankis, kuris leidžia sukurti netikrą galimybių pasą (GP) vos per keletą sekundžių.

Reikalingos bibliotekos:
```diff
+ argparse
+ img2pdf
+ qrcode
+ dateutil
+ Pillow
```
Naudojimas:
1) Įsirašykite Python 3.8.
2) Atsidarę komandinę eilutę nueikite į 'BypassGP' aplanką (cd).
3) Naudojant Python įrankį 'PIP', įsidiekite reikalingas bibliotekas, kurios surašytos bibliotekos.txt faile (pip install -r bibliotekos.txt).
4) Po bibliotekų įsidiegimo, paleiskite failą 'main.py' per komandinę eilutę ir duokite reikiamus argumentus.
 Argumentai:
 4.1) -p "JŪSŲ VARDAS"  > Argumentas nurodo, kokį vardą įdėti į galimybių pasą. Šis argumentas privalomas.
 4.2) -g METAI          > Argumentas nurodo, kokius gimimo metus įdėti į galimybių pasą. Šis argumentas privalomas.
 4.3) -d LAIKAS         > Argumentas nurodo, kokį laiką nurodytį galimybių pase. Šis argumentas neprivalomas.
 -d LAIKAS gali turėti tokias vertes: 15m, 15h, 15d ir pan. Skaičiai tai laiko tarpas, o raidė už jų nurodo skaičių tipą: minutės, valandos ar dienos.
5) Jei viskas sėkmingai atlikta - savo aplanke pastebėsite naują failą, kurio galūnė yra .pdf tipo. Tai yra naujai sugeneruotas galimybių pasas.

```diff
- Šią programą galima naudoti ir telefone: įsirašykite 'Termux' programėlę ir susiinstaliuokite visas bibliotekas.
```

Paleidimo pavyzdžiai:
```diff
python (arba python3) main.py -p "VARDAS PAVARDĖ" -g 2000          > galimybių pasas bus išduotas ant "VARDAS PAVARDĖ" žmogaus, kuris gimęs 2000-ais metais.
python (arba python3) main.py -p "VARDAS PAVARDĖ" -g 2001 -d 15m   > toks pat principas, bet galimybių paso išdavimo laikas bus 15 min prieš dabartinę valandą.
python (arba python3) main.py -p "VARDAS PAVARDĖ" -g 2002 -d 15d   > toks pat principas, bet galimybių paso išdavimo laikas bus 15 dienų prieš šiandien.
```

Dėmėsio: `QR kodai nėra sėkmingai nuskenuojami, kadangi nėra galimybės masiškai tikrinti šiuos 'hashes' ieškant braižo.
         Daugelyje vietų laisvai galėsite įeiti, kadangi nedaug kur yra pilnai tikrinami šie galimybių pasai.
         Patarimas būtų toks, kad vertėtų eiti su žmogumi, kuris turi veikiantį GP. Jei praėjo be skenavimo jis - galite eiti ir Jūs.
          Svarbiausia - nepasimeskite ir įsitikinkite, kad šiame sugeneruotame GP yra Jūsų 'realus' amžius, dėl kurio nekiltų įtarimo.

* DISCLAIMER: Nesu atsakingas už šio įrankio padarytas žalas, nors tbh visiškai nusispjaut man. Jei ne mes, kas nors vis tiek būtų ką nors panašaus sukūręs - tad, tai tik laiko klausimas. Smagaus naudojimo!
* Taip pat dėkojame nemažai daliai žmonių už pagalbą, kurie pasidalino savo galimybių pasais (GP). Be jų - neturėtumę nei menkiausio pavyzdžio.

# Et3rnal x UsrBinz
