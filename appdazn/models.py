from django.db import models as mdb

# Create your models here.

class ProductModel(mdb.Model):
    id = mdb.AutoField(primary_key=True)
    name = mdb.CharField(max_length=100, blank=True)
    description = mdb.CharField(blank=True,max_length=50)
    price = mdb.IntegerField(blank=True)

    class Meta:
        managed = True ## Aqui indica que esse classe irá gerenciar a tabela no banco.
        db_table = 'appdzan_products'

    def __str__(self):
        return self.name ##Em caso de utilizar o objeto, define que display será o name.