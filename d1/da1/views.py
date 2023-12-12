from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Zitat
#from .models import Mitglieder 
from .models import TVictdbusStunde 

#from pathlib import Path


zitate = ("Der Ball ist rund und ein Spiel dauert 90 Minuten! ",
"Der Ball ist rund. Wäre er eckig, wäre er ja ein Würfel. ",
"Wäre, wäre, Fahrradkette ",
"Ich mache nie Voraussagen und werde dies auch niemals tun. ",
"Ich habe fertig. ",
"Jede Seite hat zwei Medaillen! ",
"Viele sehen es negativ, dass wir schlecht gespielt haben. ")


def index(request, key, name):
#   return HttpResponse(zitate)

#   index = random.randint(0, len(zitate)-1) 
#   return HttpResponse(zitate[index])
   
#   return HttpResponse(f"<h1>Meine Django App {key}-{name}</h1>")

#   # settings.py/APP_DIRS=TRUE --> jede App hat ein eigenes templates-Verzeichnis: da1/templates/temp1.html
#   # es wird immer das erste gefundene Template mit diesem Namen gefunden! Templatedateiname auch über alle Apps im Projekt eindeutig machen!
#   template = loader.get_template('temp1.html')
#   return HttpResponse(template.render())

#   sprueche = Zitat.zitate    
#   template = loader.get_template('temp1.html')
#   context = {
#   'sprueche': sprueche,
#   }
#   return HttpResponse(template.render(context, request)) 



#  mitglieder = Mitglieder.objects.all().values()
#  output = "<table><tr><th>Mitgliedsnummer</th><th>Vorname</th><th>Nachname</th><th>E-Mail-Adresse</th></tr>"
#  for x in mitglieder:
#    output += "<tr><td>"  + str(x["mitgliedsnr"])+ "</td><td>" + x["vname"] + "</td><td>" + x["nname"] + "</td><td>" + x["email"] + "</td></tr>"
#  output+="</table>"
#  return HttpResponse(output)  

   sprueche = Zitat.zitate    

 #  ppp = Path(__file__).resolve().parent.parent
   

   #mitglieder = Mitglieder.objects.all().values()
   vbstunde = TVictdbusStunde.objects.all().values()
   template = loader.get_template('temp1.html')
   context = {
    #   'mitglieder': mitglieder,
       'vbstunde': vbstunde,
       'sprueche': sprueche,
#       'ppp': ppp.name,
   }
   return HttpResponse(template.render(context, request))
