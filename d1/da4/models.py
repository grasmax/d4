from fileinput import fileno
from time import sleep
from django.db import models
import subprocess

from django.core import management
import datetime

import psutil
import importlib
import random
import os
import time 
import datetime

class VPrognoseStunde(models.Model):
   # habe primary_key=True hinzugefügt, um den Fehler Unknown column 'v_prognose_stunde.id' in 'field list zu vermeiden
    stunde = models.DateTimeField(db_column='Stunde', primary_key=True, db_comment='Datum und Uhrzeit der  Ertrags-Stunde, da die backwards-Datenreihe übernommen wird, geben die P-Werte wieder, wieviele kWh bis zu dieser Stunde erwartet werden')  # Field name made lowercase.
    prognose = models.FloatField(db_column='Prognose', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'v_prognose_stunde'
        get_latest_by = 'stunde'

class VPrognoseTag(models.Model):
    stunde = models.DateField(db_column='Stunde', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='Tag', max_length=10, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    kwh = models.FloatField(db_column='kWh', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'v_prognose_tag'
        get_latest_by = 'stunde'

class VPrognoseMonat(models.Model):
    stunde = models.DateField(db_column='Stunde', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    monat = models.CharField(db_column='Monat', max_length=7, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    kwh = models.FloatField(db_column='kWh', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'v_prognose_monat'
        get_latest_by = 'stunde'

class VPrognoseJahr(models.Model):
    stunde = models.DateField(db_column='Stunde', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    jahr = models.CharField(db_column='Jahr', max_length=4, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    kwh = models.FloatField(db_column='kWh', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'v_prognose_jahr'
        get_latest_by = 'stunde'

class VPrognoseDreiTage(models.Model):
    heutestunde = models.CharField(max_length=10, db_collation='utf8mb4_general_ci', blank=True, null=True)
    heutetag = models.CharField(max_length=10, db_collation='utf8mb4_general_ci', blank=True, null=True)
    kwh = models.FloatField(db_column='kWh', blank=True, null=True)  # Field name made lowercase.
    morgenstunde = models.CharField(max_length=10, db_collation='utf8mb4_general_ci', blank=True, null=True)
    morgentag = models.CharField(max_length=10, db_collation='utf8mb4_general_ci', blank=True, null=True)
    uebermorgenstunde = models.CharField(db_column='uebermorgenStunde', max_length=10, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    uebermorgentag = models.CharField(max_length=10, db_collation='utf8mb4_general_ci', blank=True, null=True)
    tag = models.CharField(db_column='Tag', primary_key=True, max_length=11, db_collation='utf8mb4_general_ci')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'v_prognose_drei_tage'


class TAbfragen(models.Model):
    tabfrage = models.DateTimeField(db_column='tAbfrage', primary_key=True, db_comment='Zeitpunkt der Abfrage')  # Field name made lowercase. The composite primary key (tAbfrage, sFeldname) found, that is not supported. The first column is selected.
    sfeldname = models.CharField(db_column='sFeldname', max_length=10, db_comment='Name des Solarfeldes')  # Field name made lowercase.
    dlongitude = models.FloatField(db_column='dLongitude', blank=True, null=True, db_comment='Längengrad des Standorts')  # Field name made lowercase.
    dlatitude = models.FloatField(db_column='dLatitude', blank=True, null=True, db_comment='Breitengrad des Standortes')  # Field name made lowercase.
    tmodelrun = models.DateTimeField(db_column='tModelRun', blank=True, null=True, db_comment='Zeitpunkt des Prognoselaufs bei Meteoblue')  # Field name made lowercase.
    tmodelrunupdate = models.DateTimeField(db_column='tModelRunUpdate', blank=True, null=True, db_comment='Zeitpunkt des Prognoseupdates bei Meteoblue')  # Field name made lowercase.
    dkwpeak = models.FloatField(db_column='dkWPeak', blank=True, null=True, db_comment='Kilowattpeak der installierten Solarkollektoren')  # Field name made lowercase.
    ineigung = models.IntegerField(db_column='iNeigung', blank=True, null=True, db_comment='Neigung der Solarmodule, z.B. 30 Grad')  # Field name made lowercase.
    irichtung = models.IntegerField(db_column='iRichtung', blank=True, null=True, db_comment='Ausrichtung der Solarmodule, z.B. 180 (Süd)')  # Field name made lowercase.
    deffizienz = models.FloatField(db_column='dEffizienz', blank=True, null=True, db_comment='Effizienz der Solarmodule, 0.2 ...1')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_abfragen'
        unique_together = (('tabfrage', 'sfeldname'),)
        db_table_comment = 'speichert den Zeitpunkt der Abfrage der Solarprognose mit den wichtigsten Parametern\r\nabgefragt mit https://docs.meteoblue.com/en/weather-apis/packages-api/forecast-data#pv-pro \r\nin mb_pvpro.py'
        get_latest_by = 'tabfrage'


class TPrognose(models.Model):
    stunde = models.DateTimeField(db_column='Stunde', primary_key=True, db_comment='Datum und Uhrzeit der  Ertrags-Stunde, da die backwards-Datenreihe übernommen wird, geben die P-Werte wieder, wieviele kWh bis zu dieser Stunde erwartet werden')  # Field name made lowercase. The composite primary key (Stunde, Feldname) found, that is not supported. The first column is selected.
    feldname = models.CharField(db_column='Feldname', max_length=10, db_comment='Name des Solarfeldes')  # Field name made lowercase.
    p24 = models.FloatField(db_column='P24', blank=True, null=True)  # Field name made lowercase.
    p12 = models.FloatField(db_column='P12', blank=True, null=True)  # Field name made lowercase.
    p6 = models.FloatField(db_column='P6', blank=True, null=True)  # Field name made lowercase.
    p3 = models.FloatField(db_column='P3', blank=True, null=True)  # Field name made lowercase.
    p1 = models.FloatField(db_column='P1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_prognose'
        unique_together = (('stunde', 'feldname'),)
        db_table_comment = 'Speichert zu jeder Stunde die 24-, 12-, 6-, 3- und 1-Stunden-Prognose\r\nabgefragt mit https://docs.meteoblue.com/en/weather-apis/packages-api/forecast-data#pv-pro \r\nin mb_pvpro.py'




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






class RaspiShellData:
   def __init__(self):
      self.sTempFile = '/mnt/wd2tb/script/django/d1/da4/temp/tmp.txt'
                        

   def Read_subproc(self, sCmd, sReplace1, sReplace2):
      try:
         sRunCmd = f'{sCmd} > {self.sTempFile}'
         subprocess.Popen( sRunCmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
         try:
            f = open(self.sTempFile, "r")
            aLines = f.readlines()
            sLine = aLines[0]
            f.close()
         except Exception as e:
            return f'A1: {sRunCmd}: {e}'#"?1?"
         sValue = sLine.replace("\r", "")
         sValue = sValue.replace("\n", "")
         sValue = sValue.replace(sReplace1, "")
         sValue = sValue.replace(sReplace2, "")

      except Exception as e:
            return f'A2: {sRunCmd}: {e}'#"?2?"
         
      return sValue

   def Read_call_cmd(self, sCmd, sReplace1, sReplace2):
      try:
         sRunCmd = f'{sCmd} > {self.sTempFile}'

         with open("/mnt/wd2tb/script/django/d1/da4/temp/err.txt", "w") as f:
#            management.call_command(sRunCmd, verbosity=0, interactive=False)
            management.call_command(sRunCmd, verbosity=0, interactive=False)
         try:
            f = open(self.sTempFile, "r")
            aLines = f.readlines()
            sLine = aLines[0]
            f.close()
         except Exception as e:
            return f'A1: {sRunCmd}: {e}'#"?1?"
         sValue = sLine.replace("\r", "")
         sValue = sValue.replace("\n", "")
         sValue = sValue.replace(sReplace1, "")
         sValue = sValue.replace(sReplace2, "")

      except Exception as e:
            return f'A2: {sRunCmd}: {e}'#"?2?"
         
      return sValue


class RaspiData:

   def find_proc_by_name(self, name):
      try:
         for p in psutil.process_iter(["pid", "name", "exe", "cmdline"]):
           if name == p.info['name']:
              pro = psutil.Process(p.info['pid'])
              return pro
         return None
      except Exception as e:
         self.SetErr( f'Fehler in find_proc_by_name({name}): {e}')
         return None


   def InitLoad(self):
      try:
         self.sCpuLoad = f'Auslastung (1, 5, 15 Minuten)'
         self.sCpuLoadWert = psutil.cpu_percent(interval=1, percpu=True)
         self.sCpuLoadWert2 = ""
         for x in psutil.getloadavg():
            dLoad = x / psutil.cpu_count() * 100
            if len(self.sCpuLoadWert2) > 0:
               self.sCpuLoadWert2 += f', '
            self.sCpuLoadWert2 += str(round(dLoad,2))
      except Exception as e:
         self.SetErr( f'Fehler in getloadavg: {e}')


   def SetErr(self, sErr):
      try:
         self.lErr.append( sErr)
      except Exception as e:
         self.lErr.append( f'Fehler beim Fehler {sErr}: {e}')

   def OneParaSsh(self, ssh, cmd):
      try:
#$$      return "0"

         stdin,stdout,stderr=ssh.exec_command(cmd)
         outlines=stdout.readlines()
         sLine =''.join(outlines)
         sValue = sLine.replace("\r", "")
         sValue = sValue.replace("\n", "")
         sValue = sValue.replace("value =", "")
         return sValue
      except Exception as e:
         self.SetErr( f'Fehler in OneParaSsh({cmd}): {e}')

   def ParaSsh(self):
      try:
         import paramiko

         ip='192.168.2.38'
         port=22
         username='root'

         ssh=paramiko.SSHClient()
         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


         #fkt nicht print(os.system('eval "$(ssh-agent -k)"'))
         #fkt print(os.system("/usr/bin/ssh-add /home/admin2/.ssh/k4"))
         #fkt nicht: ssh.connect(ip,port)
         #ssh.connect(ip,port,username)) # fkt, aber vor muss agent und key eingetragen worden sein, da agent-Zeile nicht funktioniert, geht das also nicht

         # fkt nicht:                       mykey = paramiko.RSAKey.from_private_key_file('/home/admin2/.ssh/k4')
         # fkt, aber keine gute Stelle:     mykey = paramiko.RSAKey.from_private_key_file('/mnt/wd2tb/script/django/d1/da4/temp/k4')
         # fkt, habe aber trotzdem Bauchschmerzen:
         mykey = paramiko.RSAKey.from_private_key_file('/mnt/wd2tb/script/all/k4')
         #print(mykey)
         try:
            ssh.connect(ip,port,username,pkey=mykey)
         except Exception as e:
            self.SetErr( f'Fehler in ssh.connect(): {e}')
            return

         
         self.nDbusSoc = self.OneParaSsh(ssh, 'dbus -y com.victronenergy.system /Dc/Battery/Soc GetValue')

         sDbusSolarServiceName =  "com.victronenergy.solarcharger.ttyS7"
         self.sDbusErtrag = str(round(float(self.OneParaSsh(ssh, f'dbus -y {sDbusSolarServiceName} /Yield/System GetValue'))))
         self.sDbusErtragHeute = str(round(float(self.OneParaSsh(ssh, f'dbus -y {sDbusSolarServiceName} /History/Daily/0/Yield GetValue')),2))
         
         dMaxPv = float(self.OneParaSsh(ssh, f'dbus -y {sDbusSolarServiceName} /History/Overall/MaxPvVoltage GetValue'))
         sMaxPv = str(round(dMaxPv))
         sMaxPv5 = str(round(dMaxPv / 4 * 5))
         self.nDbusMaxPvVolt = round(dMaxPv)
         self.sDbusMaxPvVolt45 = f'{sMaxPv} V (/4*5: {sMaxPv5} V)'

         self.nDbusAktPvVolt = round(float(self.OneParaSsh(ssh, f'dbus -y {sDbusSolarServiceName} /Pv/V GetValue')))

         sDbusBattServiceName =  "com.victronenergy.battery.socketcan_can1"
         self.sDbusMinCellVolt = str(round(float(self.OneParaSsh(ssh, f'dbus -y {sDbusBattServiceName} /System/MinCellVoltage GetValue')),3))
         self.sDbusMaxCellVolt = str(round(float(self.OneParaSsh(ssh, f'dbus -y {sDbusBattServiceName} /System/MaxCellVoltage GetValue')),3))
         self.sDbusMinCellTemp = str(round(float(self.OneParaSsh(ssh, f'dbus -y {sDbusBattServiceName} /System/MinCellTemperature GetValue')),1))
         self.sDbusMaxCellTemp = str(round(float(self.OneParaSsh(ssh, f'dbus -y {sDbusBattServiceName} /System/MaxCellTemperature GetValue')),1))

         self.nDbusBattVolt = round(float(self.OneParaSsh(ssh, 'dbus -y com.victronenergy.battery.socketcan_can1 /Dc/0/Voltage GetValue')),1)

         sDbusEmServiceName = "com.victronenergy.acload.cgwacs_ttyUSB0_mb1"
         #$$ L1 und L2 fehlen noch

         ssh.close()

      except Exception as e:
         ssh.close()
         self.SetErr( f'Fehler in ParaSsh: {e}')

   def __init__(self):

      #print('RaspiData-Konstruktor') 

      # War ein Versuch, weil psutil scheinbar nur beim ersten Aufruf die richtigen Werte lieferte
      # Das lag vermutlich daran, dass die Member static/global un dnicht mit self definiert waren.
         #  try:
         #     importlib.reload( psutil )
         #  except Exception as e:
         #     errmsg2 = f"Fehler in importlib: {e}"

      self.param1 = ""
      self.param2 = ""

      self.lErr = list()
      
      #self.SetErr( f'Beispiel für einen Fehler')

      self.rd = RaspiShellData()

      self.sProgBis =  ""
      self.sProgMonat =  ""
      self.sProgJahr =  ""
      self.sProgHeute =  ""
      self.sProgMorgen =  ""
      self.sProgUebermorgen =  ""

      self.nDbusSoc = 0
      self.nDbusMaxPvVolt = 0
      self.nDbusBattVolt = 0
      self.nDbusAktPvVolt = 0
      self.sDbusMaxPvVolt45 = ""
#$$      
      self.ParaSsh()

      self.sCpuTemp = "CPU-Temperatur"
      self.sCpuTempWert = str(round(float(psutil.sensors_temperatures()['cpu_thermal'][0].current),1))
   
      self.sLastBoot = "Gestartet am"
      self.sLastBootWert = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%d.%m.%Y %H:%M")

      self.sCpuCount = "Kerne / Auslastung"
      self.sCpuCountWert = len(psutil.Process().cpu_affinity())

      self.sRam = "RAM (MB)"
      vm = psutil.virtual_memory()
      sTotal = str(round(vm.total / 1000000,1))
      sUsed = str(round(vm.used / 1000000,1))
      sAvai = str(round(vm.available / 1000000,1))
      sFree = str(round(vm.free / 1000000,1))
      self.sRamWert = f'total: {sTotal} / used: {sUsed} / available: {sAvai} / free: {sFree}'

      self.sRamSwap = "Swap (MB)"
      sw = psutil.swap_memory()
      sTotal = str(round(sw.total / 1000000,1))
      sUsed = str(round(sw.used / 1000000,1))
      sFree = str(round(sw.free / 1000000,1))
      sIn = str(round(sw.sin / 1000000,1))
      sOut = str(round(sw.sout / 1000000,1))
      self.sRamSwapWert = f'total: {sTotal} / used: {sUsed} / free: {sFree}'
      self.sRamSwapPercent = "Swap (%)"
      self.sRamSwapPercentWert = sw.percent
      
      self.lDisk = list()
      lPart = psutil.disk_partitions()
      #[sdiskpart(device='/dev/sda3', mountpoint='/', fstype='ext4', opts='rw,errors=remount-ro', maxfile=255, maxpath=4096),
      # sdiskpart(device='/dev/sda7', mountpoint='/home', fstype='ext4', opts='rw', maxfile=255, maxpath=4096)]
      for p in lPart:
         if p.mountpoint != '/' and p.mountpoint != '/mnt/wd2tb':
            continue
         sDisk = ''
         if p.mountpoint == '/':
            sDisk = 'eMMC'
         if p.mountpoint == '/mnt/wd2tb':
            sDisk = 'HDD'

         du = psutil.disk_usage(p.mountpoint)
         # sdiskusage(total=21378641920, used=4809781248, free=15482871808, percent=22
         sUnit = 'MB'
         dTeiler = 1000000.0
         iNk = 1
         if du.total > 1000000000000:
            sUnit = 'TB'
            dTeiler = 1000000000000.0
            iNk = 3
         elif du.total > 1000000000:
            sUnit = 'GB'
            dTeiler = 1000000000.0
            iNk = 3

         sTotal = str(round(du.total / dTeiler, iNk))

         sUnitUsed = 'MB'
         dTeiler = 1000000.0
         iNk = 1
         if du.used > 1000000000000:
            sUnitUsed = 'TB'
            dTeiler = 1000000000000.0
            iNk = 3
         elif du.used > 1000000000:
            sUnitUsed = 'GB'
            dTeiler = 1000000000.0
            iNk = 3
         sUsed = str(round(du.used / dTeiler, iNk))

         sUnitFree = 'MB'
         dTeiler = 1000000.0
         iNk = 1
         if du.free > 1000000000000:
            sUnitFree = 'TB'
            dTeiler = 1000000000000.0
            iNk = 3
         elif du.free > 1000000000:
            sUnitFree = 'GB'
            dTeiler = 1000000000.0
            iNk = 3
         sFree = str(round(du.free / dTeiler, iNk))
         self.lDisk.append( f'{sDisk}: total: {sTotal}{sUnit} / used: {sUsed}{sUnitUsed} ({du.percent}%) / free: {sFree}{sUnitFree}')

      # Zeitzone/Timezone einstellen, wichtig für fromtimestamp()
      # Per default ist UTC eingestellt, zum Glück kann man es hier umstellen. Keine andere Möglichkeit gefunden...
      os.environ["TZ"] = "Europe/Berlin"
      time.tzset()

      # Zeitpunkt der letzten Ausführung von \\192.168.2.28\SambaWd2Tb\raspi\ri.sh
      self.sLastSysInfo = 'Letzte Systeminfo'
      path = '/mnt/wd2tb/raspi/log'
      files = os.listdir(path)
      paths = [os.path.join(path, basename) for basename in files]
      t = os.path.getctime(max(paths, key=os.path.getctime))
      self.sLastSysInfoWert = datetime.datetime.fromtimestamp(t).strftime('%d.%m.%Y %H:%M')
      self.sLastSysInfoWert2 = datetime.datetime.utcfromtimestamp(t).strftime('%d.%m.%Y %H:%M')

      # MariaDb prüfen (und ggf neu starten?)
      p = self.find_proc_by_name('mariadbd')
      if p == None:
         try:
#$$ fkt nicht:
            sRunCmd = f'sudo systemctl start mariadb'
            print(subprocess.Popen( sRunCmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate())
            p = self.find_proc_by_name('mariadbd')
            if p == None:
               self.SetErr( 'MariaDB läuft nicht und konnte auch nicht gestartet werden!')

         except Exception as e:
            self.SetErr( f'MariaDB läuft nicht! Fehler bei {sRunCmd}: {e}')
      else:
         sStart = datetime.datetime.fromtimestamp(p.create_time()).strftime('%d.%m.%Y %H:%M')
         self.sMariaDbStatus = f'MariaDB ({p.status()}) gestartet am {sStart}(CET)'


#      try:
 #        for a in TPrognose.objects.raw("select * from t_prognose"):
  #          print( f'{a.stunde}: {a.feldname}')
#      except Exception as e:
 #        print( f'Fehler in raw: {e}')




