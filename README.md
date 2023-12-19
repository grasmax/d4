# d4 - Cockpit für eine PV-Insel und deren Steuer-Rechner
[Stand vom 19.12.2023](https://github.com/grasmax/d4/blob/main/Doc/20231219.jpg)

Der Rahmen für diese Webseite wurde erstellt mit Hilfe dieses [Grundkurses](https://www.linkedin.com/learning/django-grundkurs) von [Ralph Steyer](http://www.rjs.de). 

Im [Handbuch](https://github.com/grasmax/d4/blob/main/Doc/Handbuch%20Cockpit-Webseite.pdf) ist die Entwicklung mit allen Hürden beschrieben.
Die PV-Anlage selbst ist [hier](https://github.com/grasmax/s1) beschrieben.

Das Cockpit wird bereitgestellt von einem Apache-Server auf einem [Raspberry Pi CM4](https://github.com/grasmax/AcOnOff/blob/main/doc/Inbetriebnahme%20eines%20Steuerrechners%20f%C3%BCr%20eine%20Photovoltaikinsel.pdf).

Es kommt WSGI und das [Djange-Framework](https://docs.djangoproject.com/en/4.2/contents/) zu Einsatz.

Die Daten aus der PV-Anlage werden mit [Paramiko](https://pypi.org/project/paramiko/) über SSH und [Victron DBUS](https://github.com/victronenergy/dbus_modbustcp/blob/master/attributes.csv) ermittelt.

Prognose-, Ertrags- und Verbrauchsdaten kommen aus einer MariaDB-Datenbank, die auch auf dem CM4 läuft.

Mit Hilfe von [psutil](https://pypi.org/project/psutil/)([Doku](https://psutil.readthedocs.io/en/latest/#system-related-functions)) werden die Systemwerte aus dem CM4 gelesen.

Für die Anzeige werden [Google charts](https://developers.google.com/chart/interactive/docs?hl=de) ([vega](https://developers.google.com/chart/interactive/docs/gallery/vegachart?hl=de))) und [Gauge charts](https://github.com/grasmax/g1) eingesetzt.

Die Verknüpfung der Daten mit der Anzeige ist mit einem Django-Model-View-Template realisiert:
* [models.py](https://github.com/grasmax/d4/blob/main/d1/da4/models.py) - Bereitstellung von Datenklassen.
* [views.py](https://github.com/grasmax/d4/blob/main/d1/da4/views.py) - Verknüpfung der Daten mit dem Html-Template.
* [template.html](https://github.com/grasmax/d4/blob/main/d1/da4/templates/temp41.html) - Webseite mit CSS, Javascript und Html und {}-Zugriffen auf die gerenderten Daten.
* [d1/urls.py](https://github.com/grasmax/d4/blob/main/d1/d1/urls.py) - regelt das URL-Mapping der beiden Anwendungen da1 (Test) und da4 (produktiv).
* [da4/urls.py](https://github.com/grasmax/d4/blob/main/d1/da4/urls.py) - regelt das URL-Mapping mit Parametern für die Anwendung da4.

WSGI ist konfiguriert über [wsgi.py](https://github.com/grasmax/d4/blob/main/d1/d1/wsgi.py) und [apache.conf](https://github.com/grasmax/d4/blob/main/etc/apache2/sites-enabled/000-default.conf)

