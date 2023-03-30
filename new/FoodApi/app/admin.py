from django.contrib import admin
from .models import DonarUser, Users_donations,Food
# Register your models here.
admin.site.register(DonarUser)
admin.site.register(Users_donations)
admin.site.register(Food)

