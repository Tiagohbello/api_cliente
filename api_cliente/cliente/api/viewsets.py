from rest_framework import viewsets

from cliente.api.serializers import ClienteSerializer
from cliente.models import Cliente


class ClienteViewset(viewsets.ModelViewSet):
    model = Cliente
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
