from django.contrib import admin
from .models import User,Users_donations,Contact
# Register your models here.
admin.site.register(User)
admin.site.register(Users_donations)
class session(admin.ModelAdmin):
    list_display=['name','email','phone_number','subject','message']
admin.site.register(Contact,session)






    