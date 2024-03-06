from django.db import models

# Create your models here.

# Сюда добавляются модели (классы) базы данных от программы Django_shop
class Item(models.Model):
    ''' класс представляет собой таблицу: поля в таблице'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = models.CharField(max_length=255, name='item_name')
        self.disc = models.CharField(max_length=255, name='item_disc')
        self.price = models.FloatField(name='item_price')
        self.img = models.CharField(max_length=255, name='item_img_link')

