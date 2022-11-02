from django.contrib import admin
from cv_app.models import prof
# Register your models here.

@admin.register(prof)
class ProfileModelAdmin(admin.ModelAdmin):
 list_display = ['id','name','email','dob','state',
 'gender','location','piimage','docfile']
