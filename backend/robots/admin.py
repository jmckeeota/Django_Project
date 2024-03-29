from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Owner)
class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['user__username']
    list_display = ['first_name', 'last_name']
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    list_per_page = 10

@admin.register(models.Robot)
class Robot(admin.ModelAdmin):
    autocomplete_fields = ['owner']
    list_display = ['name', 'model_name', 'module_capacity', 'owner_username', 'built']
    list_per_page = 10
    list_select_related = ['owner', 'model']
    
    def model_name(self, robot):
        return robot.model.model_number
    def owner_username(self, robot):
        return robot.owner.user.username

admin.site.register(models.Model_Number)