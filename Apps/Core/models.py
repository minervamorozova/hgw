from django.db import models

# Create your models here.

class Users(models.Model):
    idUser = models.IntegerField(primary_key=True)
    idWallet = models.CharField(max_length=42)
    coinInGame = models.DecimalField(max_digits = 10, decimal_places = 6)
    def __str__(self):
        txt = "Usuario: {0} con Wallet {1} tiene ({2}) creditos"
        return txt.format(self.idUser, self.idWallet, self.coinInGame)