from django.contrib import admin
from .models import Apartment, Inquiry, Booking, ApartmentImage


class ApartmentImageInline(admin.TabularInline):
    model = ApartmentImage
    extra = 3


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'available')
    inlines = [ApartmentImageInline]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'apartment', 'check_in', 'check_out', 'status')


admin.site.register(Inquiry)