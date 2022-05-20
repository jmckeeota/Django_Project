from datetime import date
from django.contrib import admin
from django.conf import settings
from django.db import models


# Create your models here.

class Module(models.Model):
    skill = models.CharField(max_length=255)
    slots = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.skill

class Model_Number(models.Model):
    model_number = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.model_number

class Firmware(models.Model):
    version = models.CharField(max_length=255)
    model = models.ForeignKey(
        Model_Number, on_delete=models.PROTECT
    )
    def __str__(self) -> str:
        return self.version

class Owner(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']

    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(null=True, blank=True, max_length=255)

class Robot(models.Model):
    STATUS_ONLINE = 'N'
    STATUS_OFFLINE = 'F'
    STATUS_ERROR = 'E'

    STATUS_CHOICES = [
        ('N', 'Online'),
        ('F', 'Offline'),
        ('E', 'Error'),
    ]

    name = models.CharField(max_length=255)
    module_capacity = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    built = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)
    firmware = models.ForeignKey(
        Firmware, on_delete=models.PROTECT
    )
    model = models.ForeignKey(
        Model_Number, on_delete=models.PROTECT
    )
    owner = models.ForeignKey(
        Owner, on_delete=models.PROTECT, blank=True, null=True,
    )

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    owner = models.ForeignKey(
        Owner, on_delete=models.CASCADE
    )

class ModuleItem(models.Model):
    module = models.ForeignKey(Module, on_delete=models.PROTECT)
    robot = models.ForeignKey(Robot, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()

    # def __str__(self) -> str:
    #     return self.module.skill

class Comment(models.Model):
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)