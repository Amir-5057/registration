from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    surname = models.CharField(max_length=150, verbose_name='Фамилия')
    create_login = models.CharField(max_length=150, verbose_name='Придумайте логин')
    password = models.CharField(max_length=255, verbose_name='Пароль')
    repet_password = models.CharField(max_length=255, verbose_name='Повторите пароль')
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='Номер телефона')
    email = models.EmailField(max_length=255, null=True, blank=True, verbose_name='Почта')

    def __str__(self):
        return f"{self.name} {self.surname} {self.create_login} {self.password} {self.repet_password} {self.phone} {self.email}"







