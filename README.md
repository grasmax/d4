# d4 - Cockpit für eine PV-Insel und deren Steuer-Rechner
[Stand vom 12.12.2023](https://github.com/grasmax/d4/blob/main/Doc/20231212.jpg)

Der Rahmen für diese Webseite wurde erstellt mit Hilfe dieses [Grundkurses](https://www.linkedin.com/learning/django-grundkurs) von [Ralph Steyer](http://www.rjs.de). 

Die Anlage selbst ist [hier](https://github.com/grasmax/s1) beschrieben.

Das Cockpit wird bereitgestellt von einem Apache-Server auf einem [Raspberry Pi CM4](https://github.com/grasmax/AcOnOff/blob/main/doc/Inbetriebnahme%20eines%20Steuerrechners%20f%C3%BCr%20eine%20Photovoltaikinsel.pdf).

Es kommmt WSGI und das [Djange-Framework](https://docs.djangoproject.com/en/4.2/contents/) zu Einsatz.

Die Daten aus der PV-Anlage werden mit [Paramiko](https://pypi.org/project/paramiko/) über SSH und [Victron DBUS](https://github.com/victronenergy/dbus_modbustcp/blob/master/attributes.csv) ermittelt.

Prognose-, Ertrags- und Verbrauchsdaten kommen aus einer MariaDB-Datenbank, die auch auf dem CM4 läuft.

Mit Hilfe von [psutil](https://pypi.org/project/psutil/) werden die Systemwerte aus dem CM4 gelesen.

Die Verknüpfung der Daten mit der Anzeige ist mit einem Django-Model-View-Template realisiert:
* [models.py](https://github.com/grasmax/d4/blob/main/d1/da4/models.py) - Bereitstellung von Datenklassen
* [views.py](https://github.com/grasmax/d4/blob/main/d1/da4/views.py) - Verknüpfung von model und html template



