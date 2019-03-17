from django.contrib import admin
from .models import Organisation, Grant, Fund, Contact, Dashboard

admin.site.register(Organisation)
admin.site.register(Fund)
admin.site.register(Grant)
admin.site.register(Contact)
admin.site.register(Dashboard)
