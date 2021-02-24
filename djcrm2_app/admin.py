from django.contrib import admin
from .models import User, Lead, LeadAssigned, LeadStatus




# Register your models here.
admin.site.register(User)
admin.site.register(Lead)
admin.site.register(LeadAssigned)
admin.site.register(LeadStatus)
