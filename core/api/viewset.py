from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PomtoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    
    queryset = PontoTuristico.objects.all()
    serializer_class = PomtoTuristicoSerializer