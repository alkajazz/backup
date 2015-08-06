from django.db import models

class Altigen(models.Model):
    body = models.TextField()
    
    def __str__(self):
        return self.body

    class Meta:
        db_table = 'altigen'

class Equipment(models.Model):
    body = models.TextField()

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'equipment'

class EtiSql(models.Model):
    body = models.TextField()

    def __str__(self):
        return self.body
    
    class Meta:
        db_table = 'etisql'

class Crystal(models.Model):
    body = models.TextField()

    def __str__(self):
        return self.body
    
    class Meta:
        db_table = 'crystal'


# Create your models here.
