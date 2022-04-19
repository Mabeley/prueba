from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from authorization.authManager import UserManager
class Usuario(AbstractBaseUser,PermissionsMixin):
    id= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=150,null=False)
    correo=models.EmailField(max_length=45, null=False, unique=True)
    password=models.TextField(null=False)
    numero_cel=models.CharField(max_length=45)
    #estado =models.IntegerField(null=False)
    rol=models.CharField(choices=(
        ['ADMINISTRATOR', 'ADMINISTRADOR'],
        ['USER','USUARIO']), max_length=40)
    codigo_activacion=models.CharField(max_length=6)
    fecha_vence_plan = models.CharField(max_length=45)
    formato_impresion=models.CharField(choices=(
        ['80mm','80mm'],
        ['57mm','57mm']
    ),max_length=20)
    descripcion_cabecera=models.TextField

    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

    objects=UserManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre','rol']

    class Meta:
        db_table= 'usuarios'


