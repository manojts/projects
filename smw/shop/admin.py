from django.contrib import admin
from .models import item,truck,ware_house,procure_item,customer

admin.site.register(item)
admin.site.register(truck)
admin.site.register(ware_house)
admin.site.register(procure_item)
admin.site.register(customer)
# Register your models here.
