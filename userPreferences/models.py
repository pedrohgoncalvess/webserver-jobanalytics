from django.db import models

#WEBSERVER SCHEMA

class PreferencesUser(models.Model):
    id = models.AutoField(primary_key=True)
    tecnologie = models.CharField(unique=True, max_length=50)
    type = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = '"web_server"."preferences"'
