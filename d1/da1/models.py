from django.db import models


class Zitat:
    zitate = ("Der Ball ist rund und ein Spiel dauert 90 Minuten! ",
"Der Ball ist rund. Wäre er eckig, wäre er ja ein Würfel. ",
"Wäre, wäre, Fahrradkette ",
"Die wissen nicht einmal, dass im Ball Luft ist. Die glauben doch, der springt, weil ein Frosch drin ist. ",
"Wir müssen vor dem Tor einfach cooler sein, einfach heißer. ",
"Da mach‘ ich mir vom Kopf her keine Gedanken. ",
"Viele sehen es negativ, dass wir schlecht gespielt haben. ")

#class Mitglieder(models.Model):
#  vname = models.CharField(max_length=255)
#  nname = models.CharField(max_length=255)
#  email = models.EmailField(max_length=255)
#  mitgliedsnr = models.IntegerField(primary_key=True)

#class Mitglieder(models.Model):
 #   vname = models.CharField(max_length=255)
  #  nname = models.CharField(max_length=255)
   # email = models.CharField(max_length=255)
    #mitgliedsnr = models.AutoField(primary_key=True)
    #
    #class Meta:
     #   managed = False
      #  db_table = 'mitglieder_mitglieder'

class TChargeState(models.Model):
    eladeart = models.CharField(db_column='eLadeart', max_length=20, blank=True, null=True, db_comment='Aus...Stromzufuhr ist ausgeschaltet (kein Laden), Voll...Absorbtions/Ausgleichsladung bis auf 100%, Nach..Batterie unter Beachtung der Solarprognose zwischen 20 und 90 % halten')  # Field name made lowercase.
    taenddat = models.DateTimeField(db_column='tAendDat', blank=True, null=True, db_comment='Wann wurden EIN und AUS berechnet und eingeschaltet')  # Field name made lowercase.
    tletzterausgleich = models.DateTimeField(db_column='tLetzterAusgleich', blank=True, null=True, db_comment='Wann das letzte Ausgleichs-Laden stattgefunden hat')  # Field name made lowercase.
    nanzstunden = models.IntegerField(db_column='nAnzStunden', blank=True, null=True, db_comment='Basis für die Berechnung des Stundendurchschnitts im Tagesprofil')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_charge_state'
        db_table_comment = 'Tabelle speichert, ob die Stromzufuhr (AC-IN) für den MultiplusII-Charger ein oder ausgeschaltet ist, wann das letzte Ausgleichsladen stattgefunden hat und den letzten Solarertrag'

class TVictdbusStunde(models.Model):
    tstunde = models.DateTimeField(db_column='tStunde', primary_key=True)  # Field name made lowercase.
    dertragabs = models.FloatField(db_column='dErtragAbs', blank=True, null=True, db_comment='Gesamt-Solarertrag in kWh')  # Field name made lowercase.
    dertrag = models.FloatField(db_column='dErtrag', blank=True, null=True, db_comment='Solarertrag der letzten Stunde in kWh')  # Field name made lowercase.
    dsocprognose = models.FloatField(db_column='dSocPrognose', blank=True, null=True, db_comment='Von der Prognoserechnung ermittelter Wert')  # Field name made lowercase.
    dsocabs = models.FloatField(db_column='dSocAbs', blank=True, null=True, db_comment='Aktueller SOC in Prozent')  # Field name made lowercase.
    dsoc = models.FloatField(db_column='dSoc', blank=True, null=True, db_comment='Änderung des SOC in der letzten Stunde  in Prozent')  # Field name made lowercase.
    deml1abs = models.FloatField(db_column='dEmL1Abs', blank=True, null=True, db_comment='Zählerstand L1: mit EM540 erfasster Verbrauch in kWh, gemessen am Ausgang AC-OUT1 des MPII')  # Field name made lowercase.
    deml1 = models.FloatField(db_column='dEmL1', blank=True, null=True, db_comment='Änderung des Zählerstands L1 in der letzten Stunde: mit EM540 erfasster Verbrauch in kWh, gemessen am Ausgang AC-OUT1 des MPII')  # Field name made lowercase.
    deml2abs = models.FloatField(db_column='dEmL2Abs', blank=True, null=True, db_comment='Zählerstand L2: mit EM540 erfasster Verbrauch in kWh, gemessen am Eingang AC-IN des MPII')  # Field name made lowercase.
    deml2 = models.FloatField(db_column='dEmL2', blank=True, null=True, db_comment='Änderung des Zählerstands L2 in der letzten Stunde: mit EM540 erfasster Verbrauch in kWh, gemessen am Eingang AC-IN des MPII')  # Field name made lowercase.
    danlagenverbrauch = models.FloatField(db_column='dAnlagenVerbrauch', blank=True, null=True, db_comment='Berechneter Anlagenverbrauch: (dStadt(L2) + dErtrag ) - (dBatt (Soc)   + dHaus (L1))')  # Field name made lowercase.
    dcellvoltagemin = models.FloatField(db_column='dCellVoltageMin', blank=True, null=True, db_comment='Minimale Zellspannung, abgefragt mit dbus')  # Field name made lowercase.
    dcellvoltagemax = models.FloatField(db_column='dCellVoltageMax', blank=True, null=True, db_comment='Maximale Zellspannung, abgefragt mit dbus')  # Field name made lowercase.
    dcelltemperaturmin = models.FloatField(db_column='dCellTemperaturMin', blank=True, null=True, db_comment='Minimale Zelltemperatur, abgefragt mit dbus')  # Field name made lowercase.
    dcelltemperaturmax = models.FloatField(db_column='dCellTemperaturMax', blank=True, null=True, db_comment='Maximale Zelltemperatur, abgefragt mit dbus')  # Field name made lowercase.
    scellidminvoltage = models.CharField(db_column='sCellIdMinVoltage', max_length=10, blank=True, null=True, db_comment='ID der Batteriezelle mit der niedrigsten Spannung')  # Field name made lowercase.
    scellidmaxvoltage = models.CharField(db_column='sCellIdMaxVoltage', max_length=10, blank=True, null=True, db_comment='ID der Batteriezelle mit der höchsten Spannung')  # Field name made lowercase.
    scellidmintemperature = models.CharField(db_column='sCellIdMinTemperature', max_length=10, blank=True, null=True, db_comment='ID der Batteriezelle mit der niedrigsten Temperatur')  # Field name made lowercase.
    scellidmaxtemperature = models.CharField(db_column='sCellIdMaxTemperature', max_length=10, blank=True, null=True, db_comment='ID der Batteriezelle mit der höchsten Temperatur')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_victdbus_stunde'
        db_table_comment = 'per ssh und dbus abgefragte Werte direkt aus der Anlage'

