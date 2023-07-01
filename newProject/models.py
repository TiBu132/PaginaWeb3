from django.db import models

class tipoUsuario(models.Model):
    idTipoUsuario = models.AutoField(primary_key=True, db_column='idTipo', verbose_name='ID_tipo_Usuario')
    tipoUsuario = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.tipoUsuario)
    

class Usuario(models.Model):
    rut = models.CharField(max_length=12,primary_key=True)
    nombre = models.CharField(max_length=60, blank=False, null=False)
    apaterno = models.CharField(max_length=60,verbose_name='Apellido Paterno', blank=False, null=False)
    amaterno = models.CharField(max_length=60, verbose_name='Apellido Materno')
    fechaNac = models.DateField(blank=False,verbose_name='Fecha de Nacimiento', null=False)
    tipoUsuario = models.ForeignKey(tipoUsuario,verbose_name='Tipo de Usuario', on_delete=models.CASCADE, db_column='idTipo')
    correo = models.EmailField(unique=True, max_length=100, blank=False, null=False)
    telefono = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self) :
        return str(self.nombre)+ " " + str(self.apaterno) + " " + str(self.amaterno)
    
class Vinilo(models.Model):
    idVinilo = models.AutoField(primary_key=True, db_column='idVinilo', verbose_name='Id_Vinilo')
    nombreArt = models.CharField(max_length=50, blank=False, null=False)
    nombreDisco = models.CharField(max_length=80, blank=False, null=False)
    valorDisco = models.IntegerField()
    stock = models.IntegerField()

class descVinilo(models.Model):
    sello = models.CharField(max_length=60, blank=False, null=False)
    anno_lto = models.DateField(blank=False, null=False)
    pais = models.CharField(max_length=40, blank=False, null=False)
    genero = models.CharField(max_length=100, blank=False, null=False)
    idVinilo = models.ForeignKey(Vinilo, on_delete=models.CASCADE, db_column='idVinilo')

class tracksVinilo(models.Model):
    numTrack = models.IntegerField(db_column='numTrack', verbose_name='Numero_Track')
    nombreTrack = models.CharField(max_length=60, blank=False, null=False)
    idVinilo = models.ForeignKey(Vinilo, on_delete=models.CASCADE, db_column='idVinilo')
