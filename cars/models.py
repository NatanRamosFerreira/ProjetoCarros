from django.db import models


class Car(models.Model): # o Nome da classe vai ser o nome da tabela
    id = models.AutoField(primary_key=True) #Auto Preenchimento no Banco
    