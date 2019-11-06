from django.db import models
import datetime
class Cardapio(models.Model):
    data = models.CharField(max_length=50)

    refeicoes = (
        ('CM','Café da Manhã'),
        ('AL','Almoço'),
        ('LC','Lanche da Tarde'),
        ('JT','Janta')
    )

    tipo = models.CharField(max_length=1, choices=refeicoes)

    descricao = models.CharField(max_length=500)

    #def __str__(self):
     #  return self.nome

class Avaliacoes(models.Model):
    disciplina = models.CharField(max_length=100)

    adicionado_em = models.DateTimeField(auto_now_add=True)

    data = models.CharField(max_length=50)

    conteudo = models.CharField(max_length=350)

    avaliacoes_choice = (
        ('PV', 'Prova'),
        ('TP', 'Trabalho Prático'),
        ('SM', 'Seminário')
    )

    tipo = models.CharField(max_length=1, choices=avaliacoes_choice)

    turma = models.ForeignKey("Turma", on_delete=models.CASCADE, null=True)

class Representante(models.Model):
    nome = models.CharField(max_length=255)

    email = models.EmailField()

    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Vice(models.Model):
    nome = models.CharField(max_length=255)

    email = models.EmailField()

    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=2)

    representante = models.OneToOneField(Representante, on_delete=models.CASCADE, null=True)

    vice_representante = models.OneToOneField(Vice, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome
