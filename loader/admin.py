from django.contrib import admin

from loader.models import Bill, Client, Org, Service

# Register your models here.
admin.site.register(Bill)
admin.site.register(Client)
admin.site.register(Org)
admin.site.register(Service)
