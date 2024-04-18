from django.db import models


class Car(models.Model): # o Nome da classe vai ser o nome da tabela
    id = models.AutoField(primary_key=True) #Auto Preenchimento no Banco
    model = models.CharField(max_length=200) #Modelo do carro
    brand = models.CharField(max_length=200) #Marca
    factory_year = models.IntegerField(blank=True, null=True) #Ano Fabricação
    model_year = models.IntegerField(blank=True, null=True) # Ano do Modelo
    value = models.FloatField(blank=True, null=True) # Valor do carro
    

    