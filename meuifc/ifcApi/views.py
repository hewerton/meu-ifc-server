from django.shortcuts import render
from rest_framework import viewsets
from .models import Cardapio, Avaliacoes, Representante, Vice, Turma
from .serializers import CardapioSerializer, AvaliacoesSerializer, RepresentanteSerializer, TurmaSerializer, ViceSerializer

,
class CardapioViewSet(viewsets.ModelViewSet):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer

class AvaliacoesViewSet(viewsets.ModelViewSet):
    queryset = Avaliacoes.objects.filter(turma=1)
    serializer_class = AvaliacoesSerializer

class RepresentanteViewSet(viewsets.ModelViewSet):
    queryset = Representante.objects.all()
    serializer_class = RepresentanteSerializer

class ViceViewSet(viewsets.ModelViewSet):
    queryset = Vice.objects.all()
    serializer_class = ViceSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer