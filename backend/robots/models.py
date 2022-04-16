from django.db import models

# Create your models here.

class Module(models.Model):
    skill = models.CharField(max_length=255)
    slots = models.IntegerField()
    description = models.TextField()

class Firmware(models.Model):
    version = models.CharField(max_length=255)

class Model_Number(models.Model):
    model_number = models.CharField(max_length=255)
    firmware = models.ForeignKey(
        Firmware, on_delete=models.PROTECT
    )

class Owner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    owner_robot = models.ForeignKey(
        "Robot", on_delete=models.PROTECT, related_name='+'
    )

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
    modules = models.ManyToManyField(Module)
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

