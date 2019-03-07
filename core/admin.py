from django.contrib import admin
from .models import Organisation, Grant, Fund, Contact

admin.site.register(Organisation)
admin.site.register(Fund)
admin.site.register(Grant)
admin.site.register(Contact)
