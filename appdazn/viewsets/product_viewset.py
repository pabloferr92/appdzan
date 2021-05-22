from rest_framework import viewsets 

from appdazn.serializers.product_serializer import ProductSerializer ### Importar o serializer

from appdazn.models import ProductModel ## Importar o model


# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all() ## essa é a q
    serializer_class = ProductSerializer
