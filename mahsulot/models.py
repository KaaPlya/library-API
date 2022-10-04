from django.utils import timezone
from django.db import models

class  Menyu(models.Model):
    nomi = models.CharField(max_length=200, help_text = 'Menyu nomini kiriting...')

    def __str__(self):
        return self.nomi


class  Mahsulot(models.Model):
    nomi = models.CharField(max_length=200, help_text = 'Mahsulot nomini kiriting...')
    turi = models.ForeignKey(Menyu, on_delete=models.CASCADE, help_text = 'Mahsulot turini kiriting...')
    mahsulot_haqida = models.TextField()
    rasim = models.ImageField(upload_to='mahsulot/rasmlar', help_text = 'Mahsulot rasmini kiriting')
    narxi = models.IntegerField(help_text = 'Mahsulot narxini kiriting...')

    def __str__(self):
        return self.nomi

