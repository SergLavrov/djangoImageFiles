from django.db import models

# Create your models here.

class Car (models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    manufacturer = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField('/car_image/')  # картинка
    file = models.FileField('car_file/')  # можно прикрепить ещё файл (например doc, txt и т.д.)
                                          # затем скачать его в браузере через ссылку, либо скачать в файл



