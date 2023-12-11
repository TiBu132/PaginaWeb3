from django.db import models
 
class Vinilo(models.Model):
    idVinilo = models.IntegerField(primary_key=True, db_column='idVinilo', verbose_name='Id_Vinilo')
    nombreArt = models.CharField(max_length=50, blank=False, null=False)
    nombreDisco = models.CharField(max_length=80, blank=False, null=False)
    valorDisco = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return f'{self.nombreArt} -> {self.nombreDisco} -> {self.valorDisco}'

