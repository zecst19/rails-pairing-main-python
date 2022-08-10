
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from hello.models import Vehicle
from hello.serializers.VehicleSerializer import VehicleSerializer



class VehicleViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all().values('name')

