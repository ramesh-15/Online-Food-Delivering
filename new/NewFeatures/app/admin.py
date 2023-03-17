from django.contrib import admin
from .models import DonarUser,Users_donations,Contact,Clothes,Health,Footware
# Register your models here.
admin.site.register(DonarUser)
admin.site.register(Users_donations)
admin.site.register(Contact)
admin.site.register(Clothes)
admin.site.register(Health)
admin.site.register(Footware)

