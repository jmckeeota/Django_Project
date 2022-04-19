from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_per_page = 10

@admin.register(models.Robot)
class Robot(admin.ModelAdmin):
    list_display = ['name', 'model_name', 'module_capacity', 'owner', 'built']
    list_per_page = 10
    list_select_related = ['owner', 'model']
    
    def model_name(self, robot):
        return robot.model.model_number

admin.site.register(models.Model_Number)