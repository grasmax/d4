# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class VPrognoseMonat(models.Model):
    stunde = models.DateField(db_column='Stunde', blank=True, null=True)  # Field name made lowercase.
    monat = models.CharField(db_column='Monat', max_length=7, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    kwh = models.FloatField(db_column='kWh', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'v_prognose_monat'
