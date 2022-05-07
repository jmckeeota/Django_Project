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
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

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