from django.contrib import admin
from .models import dept_master,sub_dept,tender,bidding,company,complaint

admin.site.register(dept_master)
admin.site.register(sub_dept)
admin.site.register(tender)
admin.site.register(bidding)
admin.site.register(company)
admin.site.register(complaint)



# for registering the models in admin panel
