from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer


    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)


    def list(self, request, *args, **kwargs):
        return Response({'teste': 123})

    
    def create(self, request, *args, **kwargs):
        return Response({'hello': request.data['nome']})


    def destroy(self, request, *args, **kwargs):
        pass


    def retrieve(self, request, *args, **kwargs):
        pass


    def update(self, request, *args, **kwargs):
        pass


    def parse_update(self, request, *args, **kwargs):
        pass