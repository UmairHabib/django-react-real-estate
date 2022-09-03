from .models import Enquiry
from django.contrib import admin


class EnquiryAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone_number", "message"]


admin.site.register(Enquiry, EnquiryAdmin)

