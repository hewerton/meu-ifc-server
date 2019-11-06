from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Cardapio, Avaliacoes, Representante, Vice, Turma

class CardapioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardapio
        fields = ['data', 'tipo', 'descricao']

class AvaliacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacoes
        fields = ['disciplina','adicionado_em','data', 'conteudo', 'tipo','turma']

class RepresentanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representante
        fields = ['nome', 'email', 'senha']

class ViceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vice
        fields = ['nome','email', 'senha']

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = ['nome', 'representante', 'vice_representante']