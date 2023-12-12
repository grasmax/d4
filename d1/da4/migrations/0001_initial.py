# Generated by Django 4.2.7 on 2023-12-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TChargeState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eladeart', models.CharField(blank=True, db_column='eLadeart', db_comment='Aus...Stromzufuhr ist ausgeschaltet (kein Laden), Voll...Absorbtions/Ausgleichsladung bis auf 100%, Nach..Batterie unter Beachtung der Solarprognose zwischen 20 und 90 % halten', max_length=20, null=True)),
                ('taenddat', models.DateTimeField(blank=True, db_column='tAendDat', db_comment='Wann wurden EIN und AUS berechnet und eingeschaltet', null=True)),
                ('tletzterausgleich', models.DateTimeField(blank=True, db_column='tLetzterAusgleich', db_comment='Wann das letzte Ausgleichs-Laden stattgefunden hat', null=True)),
                ('nanzstunden', models.IntegerField(blank=True, db_column='nAnzStunden', db_comment='Basis für die Berechnung des Stundendurchschnitts im Tagesprofil', null=True)),
            ],
            options={
                'db_table': 't_charge_state',
                'db_table_comment': 'Tabelle speichert, ob die Stromzufuhr (AC-IN) für den MultiplusII-Charger ein oder ausgeschaltet ist, wann das letzte Ausgleichsladen stattgefunden hat und den letzten Solarertrag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TVictdbusStunde',
            fields=[
                ('tstunde', models.DateTimeField(db_column='tStunde', primary_key=True, serialize=False)),
                ('dertragabs', models.FloatField(blank=True, db_column='dErtragAbs', db_comment='Gesamt-Solarertrag in kWh', null=True)),
                ('dertrag', models.FloatField(blank=True, db_column='dErtrag', db_comment='Solarertrag der letzten Stunde in kWh', null=True)),
                ('dsocprognose', models.FloatField(blank=True, db_column='dSocPrognose', db_comment='Von der Prognoserechnung ermittelter Wert', null=True)),
                ('dsocabs', models.FloatField(blank=True, db_column='dSocAbs', db_comment='Aktueller SOC in Prozent', null=True)),
                ('dsoc', models.FloatField(blank=True, db_column='dSoc', db_comment='Änderung des SOC in der letzten Stunde  in Prozent', null=True)),
                ('deml1abs', models.FloatField(blank=True, db_column='dEmL1Abs', db_comment='Zählerstand L1: mit EM540 erfasster Verbrauch in kWh, gemessen am Ausgang AC-OUT1 des MPII', null=True)),
                ('deml1', models.FloatField(blank=True, db_column='dEmL1', db_comment='Änderung des Zählerstands L1 in der letzten Stunde: mit EM540 erfasster Verbrauch in kWh, gemessen am Ausgang AC-OUT1 des MPII', null=True)),
                ('deml2abs', models.FloatField(blank=True, db_column='dEmL2Abs', db_comment='Zählerstand L2: mit EM540 erfasster Verbrauch in kWh, gemessen am Eingang AC-IN des MPII', null=True)),
                ('deml2', models.FloatField(blank=True, db_column='dEmL2', db_comment='Änderung des Zählerstands L2 in der letzten Stunde: mit EM540 erfasster Verbrauch in kWh, gemessen am Eingang AC-IN des MPII', null=True)),
                ('danlagenverbrauch', models.FloatField(blank=True, db_column='dAnlagenVerbrauch', db_comment='Berechneter Anlagenverbrauch: (dStadt(L2) + dErtrag ) - (dBatt (Soc)   + dHaus (L1))', null=True)),
                ('dcellvoltagemin', models.FloatField(blank=True, db_column='dCellVoltageMin', db_comment='Minimale Zellspannung, abgefragt mit dbus', null=True)),
                ('dcellvoltagemax', models.FloatField(blank=True, db_column='dCellVoltageMax', db_comment='Maximale Zellspannung, abgefragt mit dbus', null=True)),
                ('dcelltemperaturmin', models.FloatField(blank=True, db_column='dCellTemperaturMin', db_comment='Minimale Zelltemperatur, abgefragt mit dbus', null=True)),
                ('dcelltemperaturmax', models.FloatField(blank=True, db_column='dCellTemperaturMax', db_comment='Maximale Zelltemperatur, abgefragt mit dbus', null=True)),
                ('scellidminvoltage', models.CharField(blank=True, db_column='sCellIdMinVoltage', db_comment='ID der Batteriezelle mit der niedrigsten Spannung', max_length=10, null=True)),
                ('scellidmaxvoltage', models.CharField(blank=True, db_column='sCellIdMaxVoltage', db_comment='ID der Batteriezelle mit der höchsten Spannung', max_length=10, null=True)),
                ('scellidmintemperature', models.CharField(blank=True, db_column='sCellIdMinTemperature', db_comment='ID der Batteriezelle mit der niedrigsten Temperatur', max_length=10, null=True)),
                ('scellidmaxtemperature', models.CharField(blank=True, db_column='sCellIdMaxTemperature', db_comment='ID der Batteriezelle mit der höchsten Temperatur', max_length=10, null=True)),
            ],
            options={
                'db_table': 't_victdbus_stunde',
                'db_table_comment': 'per ssh und dbus abgefragte Werte direkt aus der Anlage',
                'managed': False,
            },
        ),
    ]