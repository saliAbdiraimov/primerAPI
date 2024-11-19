from django.db import models

# Create your models here.

class panel(models.Model):
    TRENER_NAME = [
        ('Менеджер','Менеджер'),
        ('Тренер', 'Тренер'),
        ('Клиент', 'Клиент'),
    ]
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    cat = models.CharField(max_length=20, choices=TRENER_NAME, null=True)
    def __str__(self):
        return f'имя:{self.name} фамилия: {self.second_name} позиция: {self.cat}'



