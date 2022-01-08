from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from cliente.api.serializers import ClienteSerializer
from cliente.models import Cliente


class ClienteViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    model = Cliente
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
