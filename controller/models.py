from django.db import models

#SCHEDULER_SCRAP SCHEMA

class PathSite(models.Model):
    id_set = models.ForeignKey('SetPath', models.DO_NOTHING, db_column='id_set', blank=True, null=True)
    type_info = models.CharField(max_length=20)
    path = models.CharField(unique=True, max_length=1000)

    class Meta:
        managed = False
        db_table = 'path_site'


class Scheduler(models.Model):
    id_path = models.ForeignKey(PathSite, models.DO_NOTHING, db_column='id_path', blank=True, null=True)
    tested_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scheduler'


class Schedulerschema(models.Model):
    id_path = models.IntegerField(blank=True, null=True)
    tested_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedulerSchema'


class SetPath(models.Model):
    stage_scrap = models.CharField(unique=True, max_length=20)
    site_scrap = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'set_path'


class UrlTest(models.Model):
    url_job = models.CharField(max_length=400)
    scraped_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'url_test'



#SCRAP_JOB SCHEMA


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

