from django.contrib import admin
from .models import Partner, Network, Contact

admin.site.register(Partner)
admin.site.register(Network)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["lname", "fname", "sent_on"]
