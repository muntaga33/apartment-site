from django.contrib import admin
from .models import Apartment, ApartmentImage, Booking, Inquiry


admin.site.site_header = "Muntaga's Property Hub Admin"
admin.site.site_title = "Property Hub Admin"
admin.site.index_title = "Administration"


class ApartmentImageInline(admin.TabularInline):
    model = ApartmentImage
    extra = 1


class ApartmentAdmin(admin.ModelAdmin):
    inlines = [ApartmentImageInline]


admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Booking)
admin.site.register(Inquiry)