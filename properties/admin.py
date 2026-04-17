from django.contrib import admin
from .models import Apartment, Booking, Inquiry


admin.site.site_header = "Muntaga's Property Hub Admin"
admin.site.site_title = "Property Hub Admin"
admin.site.index_title = "Administration"


# Register models so they appear in admin
admin.site.register(Apartment)
admin.site.register(Booking)
admin.site.register(Inquiry)