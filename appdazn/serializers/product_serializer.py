from rest_framework import serializers

from appdazn.models import ProductModel ## Aqui estamos importando a model que será referência desse serializer.


# Serializers define the API representation.
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'description', 'price']
