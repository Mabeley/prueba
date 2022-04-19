from django.db import models

class TablaItems(models.Model):
    id =models.AutoField(primary_key=True)
    uid =models.CharField(max_length=45)
    descripcion = models. CharField(max_length=45, null=False)
    costo = models.FloatField(null=False)
    tipo_comision = models.CharField(choices=(
        ['MONTO','MONTO'],
        ['PORCENTAJE','PORCENTAJE']),max_length=20)
    monto_comision =models.FloatField(null=False)
    factor_comision = models.FloatField(null=False)
    estado= models.BooleanField(null=False)

    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

    class Meta:
        db_table='tablaitems'

# class DetalleOperacion(models.Model):
#     id = models.AutoField(primary_key=True)
#     cantidad =models.IntegerField(null=False)
#     monto_comision = models.DecimalField(max_digits=2,decimal_places=1)
#     total_item =models.DateTimeField(max_digits=2,decimal_places=1)