from django.contrib import admin
from .models import Machine, OpsLog, Maintenance

admin.site.register(Machine)
admin.site.register(OpsLog)
admin.site.register(Maintenance)

