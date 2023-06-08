from django.contrib import admin
from .models import Home
# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display=('course','place','cgpa')

admin.site.register(Home,HomeAdmin)
