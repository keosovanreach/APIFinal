from django.contrib import admin
from .models import *
 
# Register your models here.
admin.site.register(Roles)

admin.site.site_header = 'S.Management System'
admin.site.site_title = 'Supplier Management System Admin'
admin.site.index_title = 'Welcome to Supplier Management System Admin'
