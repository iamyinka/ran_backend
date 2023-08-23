from django.contrib import admin
from .models import Partner, Network, Contact, Donation

admin.site.register(Partner)
admin.site.register(Network)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["lname", "fname", "sent_on"]


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ["sender", "email", "amount", "cause", "frequency", "message", "status", "tx_ref", "paid_on"]