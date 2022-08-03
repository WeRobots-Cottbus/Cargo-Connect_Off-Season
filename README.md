
# [Aktuelles Thema]

[![License CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-%2300B4D6)](https://creativecommons.org/licenses/by/4.0/)&nbsp;

**Setup:**

1. Überschrift zu aktuellem FLL Thema ändern

2. den Ordner [`src/`](src/) zu `src_{REPOSITORY_ABBREVIATION}` umbennen, damit im Dateisystem des Brick's nicht überall nur `src` steht:
   - "**C**argo **C**onnect" $\to$ `src_cc`
   - "**C**argo **C**onnect - **O**ff-**S**eason" $\to$ `src_cc-os`

3. in Zeile 11 der Datei `src/programs/prgP_T.py` den Pfad `/home/robot/src` zu `/home/robot/src_{REPOSITORY_ABBREVIATION}` ändern
   - "**C**argo **C**onnect" $\to$ `sys.path.insert(0, "/home/robot/src_cc")`

4. in der `src/botconfig.py` die Ports der Motoren und Sensoren sowie die Maße des Roboters konfigurieren
   - `MotorFront = Motor(Port.D)`
   - `ColorRight = ColorSensor(Port.S4)`
   - $5.7\:cm$ Raddurchmesser und $15.4\:cm$ Radabstand $\to$ `Base = DriveBase(MotorLeft, MotorRight, 57, 154)`

5. im Ordner `src/programs/` für jedes Programm eine eigene Python-Datei als Kopie von `prgP_T.py` anlegen und umbennen zu:
   - Programm 1, Teil 1 $\to$ `prg1_1.py`
   - Programm 1, Teil 2 $\to$ `prg1_2.py`
   - Programm 2 $\to$ `prg2.py`

6. in Zeile 12 des *Hauptprogramms* `src/main.py` alle Programme auflisten sowie als Liste in Zeile 14:
   - Zeile 12: `from programs import prg1_1, prg1_2, prg2`
   - Zeile 14: `prg_lst = [prg1_1, prg1_2, prg2]`

7. in Zeile 13 vom `src/motorcontroller.py` die Variablen der Motoren und die zugehörige Anzeige in den Zeilen 35/36 bzw. 38/39 ändern, wenn sie in (3.) verändert wurden

8. am Anfang der `README.md` nach der `license`-Badge die `build`-Status-Badge einfügen und den `{REPOSITORY_NAME}` in die URLs einsetzen:
   ```
   [![build](https://github.com/WeRobots-Cottbus/{REPOSITORY_NAME}/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/WeRobots-Cottbus/ 
   {REPOSITORY_NAME}/actions/workflows/build.yml)&nbsp;
   ```

9.  den `src/` Ordner als eigenständigen Workspace in VS Code öffnen, auf den Brick laden und starten
   - theoretisch fehlerfrei, praktisch erstmal debuggen ...

***

10. den Code der einzelnen Programme in die `run()`-Funktion schreiben
    - hauptsächlich `Base`-Methoden nutzen: z.B. `Base.straight(340)`
    - eigene programmspezifische Funktionen in der gleichen Datei definieren
    - Funktionen die auch in anderen Programmen wiederverwendet werden (können) im `src/toolkit.py` definieren

11. regelmäßig aussagekräftige *Commits* erstellen und spätestens am Ende des Tages *Pushen* 
    - evtl. *Branches*, *Pull-Requests* und *Issues* nutzen

***

12. in diese Datei dokumentierend zum Projekt schreiben und die Setup-Anleitung entfernen
