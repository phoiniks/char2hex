# char2hex
Programm zum Konvertieren von Zeichenketten in Abfolgen hexadezimaler Quartette

Sinn und Zweck des vorliegenden Programms:

Sie haben eine binäre Datei vorliegen, aber den Quellcode gelöscht?
Sie müssen den Text der Benutzerschnittstelle dringend verändern?
Dann können Sie mit Hilfe von hexedit unter Umständen den Text noch verändern!
Das Problem: hexedit stellt Ihnen aber leider nur eine hexadezimale
Sicht auf die Binärdatei zur Verfügung. Wenn Sie hier längere Textpassagen
verändern wollen, kann die Umformatierung von Zeichenketten
Ihnen schon einiges Kopfzerbrechen bereiten und Sie vor allen
Dingen viel Zeit kosten. Benutzen Sie hierzu einfach dieses simple
Skript:./char2hex.py 'Dies ist der blöde Text.' (Ihr Text wird natürlich
Sinnvolleres enthalten!) Jetzt können Sie Ihre Binärdatei mit hexedit
öffnen und die 'Zeichenkette' am gewünschten Ort bequem eingeben!
Mit F2 speichern Sie die veränderte Datei und voilà: Die (Text-)
Schnittstelle enthält Ihre Änderung!

