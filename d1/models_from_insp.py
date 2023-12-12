# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class TChargeLog(models.Model):
    tlog = models.DateTimeField(db_column='tLog', blank=True, null=True, db_comment='Wann wurde ein- oder ausgeschaltet')  # Field name made lowercase.
    etyp = models.CharField(db_column='eTyp', max_length=20, blank=True, null=True, db_comment='Info oder Fehler')  # Field name made lowercase.
    eladeart = models.CharField(db_column='eLadeart', max_length=20, blank=True, null=True, db_comment='Aus...Stromzufuhr ist ausgeschaltet (kein Laden), Voll...Absorbtions/Ausgleichsladung bis auf 100%, Nach..Batterie unter Beachtung der Solarprognose zwischen 20 und 90 % halten')  # Field name made lowercase.
    stext = models.CharField(db_column='sText', max_length=250, blank=True, null=True, db_comment='Fehler oder Infotext, z.B. Grund für das Ein- oder Ausschalten')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_charge_log'
        db_table_comment = 'Tabelle speichert, wann und warum die Stromzufuhr (AC-IN) für den MultiplusII-Charger ein oder ausgeschaltet wurde'


class TChargeState(models.Model):
    eladeart = models.CharField(db_column='eLadeart', max_length=20, blank=True, null=True, db_comment='Aus...Stromzufuhr ist ausgeschaltet (kein Laden), Voll...Absorbtions/Ausgleichsladung bis auf 100%, Nach..Batterie unter Beachtung der Solarprognose zwischen 20 und 90 % halten')  # Field name made lowercase.
    taenddat = models.DateTimeField(db_column='tAendDat', blank=True, null=True, db_comment='Wann wurden EIN und AUS berechnet und eingeschaltet')  # Field name made lowercase.
    tletzterausgleich = models.DateTimeField(db_column='tLetzterAusgleich', blank=True, null=True, db_comment='Wann das letzte Ausgleichs-Laden stattgefunden hat')  # Field name made lowercase.
    nanzstunden = models.IntegerField(db_column='nAnzStunden', blank=True, null=True, db_comment='Basis für die Berechnung des Stundendurchschnitts im Tagesprofil')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_charge_state'
        db_table_comment = 'Tabelle speichert, ob die Stromzufuhr (AC-IN) für den MultiplusII-Charger ein oder ausgeschaltet ist, wann das letzte Ausgleichsladen stattgefunden hat und den letzten Solarertrag'


class TChargeTicket(models.Model):
    eschaltart = models.CharField(db_column='eSchaltart', max_length=20, blank=True, null=True, db_comment='ausschalten...Stromzufuhr ausschalten (kein Laden), einschalten...Stromzufuhr einschalten für Nachladen oder ausgleichen')  # Field name made lowercase.
    tanldat = models.DateTimeField(db_column='tAnlDat', blank=True, null=True, db_comment='Wann wurde das Ticket angelegt')  # Field name made lowercase.
    tsoll = models.DateTimeField(db_column='tSoll', blank=True, null=True, db_comment='Wann soll eingeschaltet werden')  # Field name made lowercase.
    tist = models.DateTimeField(db_column='tIst', blank=True, null=True, db_comment='Tatsächlicher Schaltzeitpunkt')  # Field name made lowercase.
    tsollaus = models.DateTimeField(db_column='tSollAus', blank=True, null=True, db_comment='Nur bei Einschalt-Ticket (informativ): Wann eingeschaltet werden soll')  # Field name made lowercase.
    sgrund = models.CharField(db_column='sGrund', max_length=30, blank=True, null=True, db_comment='Nur bei Einschalt-Ticket (informativ): Nachladen oder Ausgleichen')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_charge_ticket'
        db_table_comment = 'Tabelle enthält alle Tickets für Schaltvorgänge. Die Tickets werden von mpIIcalcaconoff.py angelegt und von mpIIaconoff abgearbeitet.'


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


class TPrognoseLog(models.Model):
    tlog = models.DateTimeField(db_column='tLog', blank=True, null=True, db_comment='Log-Zeitpunkt')  # Field name made lowercase.
    etyp = models.CharField(db_column='eTyp', max_length=20, blank=True, null=True, db_comment='Info oder Fehler')  # Field name made lowercase.
    stext = models.CharField(db_column='sText', max_length=250, blank=True, null=True, db_comment='Fehler oder Infotext')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_prognose_log'
        db_table_comment = 'Tabelle speichert alle Info und Fehler beim Holen und Speichern der Solarprognose'


class TTagesprofil(models.Model):
    nmonat = models.IntegerField(db_column='nMonat', primary_key=True, db_comment='n= 1-12, 1...Januar, 12...Dezember')  # Field name made lowercase. The composite primary key (nMonat, nStunde) found, that is not supported. The first column is selected.
    nstunde = models.IntegerField(db_column='nStunde', db_comment='n= 1-24, n bedeutet, die Werte in den anderen Spalten geben an, was bis n Uhr verbraucht wurde.')  # Field name made lowercase.
    dkwhhaus = models.FloatField(db_column='dKwhHaus', blank=True, null=True, db_comment='Durchschnitts-Verbrauch der Verbraucher im Solarteil der Hausinstallation in kWh')  # Field name made lowercase.
    dkwhanlage = models.FloatField(db_column='dKwhAnlage', blank=True, null=True, db_comment='Durchschnittlicher Eigenverbrauch der Anlage in kWh')  # Field name made lowercase.
    dkwhhausmin = models.FloatField(db_column='dKwhHausMin', blank=True, null=True, db_comment='Minimaler der Verbraucher im Solarteil der Hausinstallation in kWh')  # Field name made lowercase.
    dkwhhausmax = models.FloatField(db_column='dKwhHausMax', blank=True, null=True, db_comment='Maximaler der Verbraucher im Solarteil der Hausinstallation in kWh')  # Field name made lowercase.
    dkwhanlagemin = models.FloatField(db_column='dKwhAnlageMin', blank=True, null=True, db_comment='Minimaler Eigenverbrauch der Anlage in kWh')  # Field name made lowercase.
    dkwhanlagemax = models.FloatField(db_column='dKwhAnlageMax', blank=True, null=True, db_comment='Maximaler Eigenverbrauch der Anlage in kWh')  # Field name made lowercase.
    dkwhsolarmax = models.FloatField(db_column='dKwhSolarMax', blank=True, null=True, db_comment='Maximaler Solarertrag in dieser Stunde des Monats als Grundlage für die Beschattungsberechnung')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_tagesprofil'
        unique_together = (('nmonat', 'nstunde'),)
        db_table_comment = '24 Datensätze für jede Stunde eines Tages'


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


class TVictportStunde(models.Model):
    tstunde = models.DateTimeField(db_column='tStunde', primary_key=True)  # Field name made lowercase.
    dertragabs = models.FloatField(db_column='dErtragAbs', blank=True, null=True, db_comment='Gesamter Solarertrag in kWh')  # Field name made lowercase.
    dertrag = models.FloatField(db_column='dErtrag', blank=True, null=True, db_comment='Solarertrag in dieser Stunde in kWh')  # Field name made lowercase.
    dbattsoc = models.FloatField(db_column='dBattSOC', blank=True, null=True, db_comment='Batterie-Ladezustand am Ende der Stunde in Prozent')  # Field name made lowercase.
    sabsorption = models.CharField(db_column='sAbsorption', max_length=5, blank=True, null=True, db_comment='j, wenn in der letzten Stunde Absorption erkannt wurde. Sonst n')  # Field name made lowercase.
    dbattspannung = models.FloatField(db_column='dBattSpannung', blank=True, null=True, db_comment='Batteriespannung am Ende der Stunde in Volt')  # Field name made lowercase.
    dmaxpvspannung = models.FloatField(db_column='dMaxPvSpannung', blank=True, null=True, db_comment='Maximale PV-Spannung der Stunde')  # Field name made lowercase.
    dmaxpvleistung = models.FloatField(db_column='dMaxPvLeistung', blank=True, null=True, db_comment='Maximale PV-Leistung der Stunde')  # Field name made lowercase.
    dminbattstrom = models.FloatField(db_column='dMinBattStrom', blank=True, null=True, db_comment='Minimaler Strom von/zur Batterie')  # Field name made lowercase.
    dmaxbattstrom = models.FloatField(db_column='dMaxBattStrom', blank=True, null=True, db_comment='Maximaler Strom von/zur Batterie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_victport_stunde'
        db_table_comment = 'Auszug aus den Daten, die leider manuell per CSV-Export aus der Advanced-Seite des Victron-Portals geholt werden müssen.\r\nNachbearbeitet und importiert mit vp_import_csv_to_db.py\r\n'
