from ast import Try
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import random

from .models import RaspiData 

from .models import TAbfragen
from .models import TPrognose

from .models import VPrognoseStunde
from .models import VPrognoseTag
from .models import VPrognoseMonat
from .models import VPrognoseJahr
from .models import VPrognoseDreiTage

import os
import psutil

import time 
import datetime


def index(request, key, name):

   rd = RaspiData() # hier passiert sehr viel

   rd.param1 = key
   rd.param2 = name

   try:   
      rd.InitLoad() # hier wird die cpu-Auslastung bestimmt
   except Exception as e:
      rd.SetErr( f'Fehler in InitLoad(): {e}')

   
   # Beispiel für den Zugriff auf die Umgebungsvariablen
   # rd.logdir = os.environ['APACHE_LOG_DIR']
   # TZ (Zeitzone) wird in RaspiData() gesetzt
   # hier nur zur Kontrolle ausgeben:
   try:
      lEnv = list()
      for key, value in os.environ.items():
         lEnv.append(f'{key}: {value}')
   except Exception as e:
       rd.SetErr( f'Fehler env: {e}')


   try:
     vm = psutil.virtual_memory()
   except Exception as e:
       rd.SetErr( f'Fehler vm: {e}')


   # Achtung! Model-Abfragen funktionieren nur hier in views.py, nicht in models.py

   #mitglieder = Mitglieder.objects.all().values()
#   vbstunde = TVictdbusStunde.objects.all().values()
   LetzteMbAbfrage = TAbfragen.objects.latest().tabfrage.strftime('%d.%m.%Y %H:%M')

   #try:
      # der app-Vorspann "da4" ist laut Doku nötig. Ist er aber nicht, weder in der shell noch hier...
      #     for a in TAbfragen.objects.raw("select * from da4_t_abfragen"):
      # Abfrage einzelner Felder funktioniert auch nicht: Fehler: "Fehler in raw: Raw query must include the primary key"
      #for a in TAbfragen.objects.raw("select tabfrage,sfeldname from t_abfragen where sfeldname='Solarport'"):
      #so funktioniert es:
      #for a in TAbfragen.objects.raw("select * from t_abfragen"):
      #   print( f'{a.tabfrage}: {a.sfeldname}')
   #except Exception as e:
   #    print( f'Fehler in raw: {e}')

   try:
      sph = VPrognoseStunde.objects.latest().stunde.strftime('%d.%m.%Y %H')
      spt = VPrognoseTag.objects.latest().tag
      spm = VPrognoseMonat.objects.latest().monat
      spy = VPrognoseJahr.objects.latest().jahr

      rd.sProgBis =  f'{sph}: {VPrognoseStunde.objects.latest().prognose} kWh'

      rd.sProgHeute =  f'Heute: {VPrognoseDreiTage.objects.filter(tag="heute")[0].kwh} kWh'
      rd.sProgMorgen =  f'Morgen: {VPrognoseDreiTage.objects.filter(tag="morgen")[0].kwh} kWh'
      rd.sProgUebermorgen =  f'Übermorgen: {VPrognoseDreiTage.objects.filter(tag="uebermorgen")[0].kwh} kWh'

      rd.sProgMonat =  f'{spm}: {VPrognoseMonat.objects.latest().kwh} kWh'
      rd.sProgJahr =  f'{spy}: {VPrognoseJahr.objects.latest().kwh} kWh'


   except Exception as e:
      print( f'Fehler in Prognose: {e}')



   context = {
    #   'mitglieder': mitglieder,
 #      'vbstunde': vbstunde,
   #    'sprueche': sprueche,
      'rd': rd,
      'env': lEnv,
      'disk': rd.lDisk,
      'vm': vm,
      'mb': LetzteMbAbfrage,
      'err': rd.lErr,
      'errcount': len(rd.lErr),
   }

   template = loader.get_template('temp41.html')

   return HttpResponse(template.render(context, request))
