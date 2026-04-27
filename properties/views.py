from django.shortcuts import render, get_object_or_404
from .models import Apartment, Inquiry, Booking
from datetime import date, timedelta


def apartment_list(request):
    query = request.GET.get('q', '').strip()
    furnished = request.GET.get('furnished')
    min_price = request.GET.get('min')
    max_price = request.GET.get('max')
    available_only = request.GET.get('available')

    apartments = Apartment.objects.all().order_by('-is_featured', '-id')

    if query:
        apartments = apartments.filter(location__icontains=query)

    if furnished:
        apartments = apartments.filter(furnishing=furnished)

    if min_price:
        apartments = apartments.filter(price__gte=min_price)

    if max_price:
        apartments = apartments.filter(price__lte=max_price)

    if available_only == 'yes':
        apartments = apartments.filter(available=True)

    featured = Apartment.objects.filter(is_featured=True)

    return render(request, 'properties/apartment_list.html', {
        'apartments': apartments,
        'featured': featured,
        'query': query,
        'furnished': furnished,
        'min_price': min_price,
        'max_price': max_price,
        'available_only': available_only,
    })


def apartment_detail(request, id):
    apartment = get_object_or_404(Apartment, id=id)
    return render(request, 'properties/apartment_detail.html', {
        'apartment': apartment
    })


def about(request):
    return render(request, 'properties/about.html')


def contact(request):
    success = False

    if request.method == 'POST':
        name = request.POST.get('name')
        contact_info = request.POST.get('contact')
        message = request.POST.get('message')

        Inquiry.objects.create(
            name=name,
            contact=contact_info,
            message=message
        )
        success = True

    return render(request, 'properties/contact.html', {
        'success': success
    })


def calendar_view(request):
    bookings = Booking.objects.select_related('apartment').order_by('check_in')
    return render(request, 'properties/calendar.html', {
        'bookings': bookings
    })