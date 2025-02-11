from django.contrib import admin
from .models import Case, Client, Lawyer


# Register your models here.
admin.site.register(Case)
admin.site.register(Client)
admin.site.register(Lawyer)