from django.contrib import admin
from .models import Apartment, Booking, Inquiry


admin.site.site_header = "Muntaga's Property Hub Admin"
admin.site.site_title = "Property Hub Admin"
admin.site.index_title = "Administration"


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "price", "available", "is_featured")
    list_filter = ("available", "is_featured", "location")
    search_fields = ("title", "location")


admin.site.register(Booking)
admin.site.register(Inquiry)