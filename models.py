# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Job(models.Model):
    id_job = models.CharField(unique=True, max_length=300, blank=True, null=True)
    vacancy_title = models.CharField(max_length=70, blank=True, null=True)
    vacancy_org = models.CharField(max_length=70, blank=True, null=True)
    experience = models.CharField(max_length=75, blank=True, null=True)
    candidates = models.CharField(max_length=50, blank=True, null=True)
    date_publish = models.CharField(max_length=75, blank=True, null=True)
    scraped_at = models.DateTimeField(blank=True, null=True)
    researched_topic = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'job'


class JobDescription(models.Model):
    id_job = models.ForeignKey(Job, models.DO_NOTHING, db_column='id_job', blank=True, null=True)
    text = models.CharField(max_length=15000)

    class Meta:
        managed = False
        db_table = 'job_description'


class JobStandby(models.Model):
    id_job = models.CharField(unique=True, max_length=500)
    used_term = models.CharField(max_length=30)
    status = models.CharField(max_length=10, blank=True, null=True)
    scraped_at = models.DateTimeField(blank=True, null=True)
    site = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'job_standby'


class JobTopics(models.Model):
    id_job = models.ForeignKey(Job, models.DO_NOTHING, db_column='id_job', blank=True, null=True)
    topic = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'job_topics'


class TecnologiesInfo(models.Model):
    tecnologie = models.CharField(unique=True, max_length=50)
    type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tecnologies_info'


class TopicSearch(models.Model):
    topic_search = models.CharField(unique=True, max_length=50)
    topic_classification = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'topic_search'
