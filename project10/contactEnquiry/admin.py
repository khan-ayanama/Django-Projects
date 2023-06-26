from django.contrib import admin
from contactEnquiry.models import contactEnquiry

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'user_image']


admin.site.register(contactEnquiry, ContactAdmin)
