from django.shortcuts import render, get_object_or_404
from .models import Apartment, Inquiry, Booking
from datetime import date, timedelta


def apartment_list(request):
    query = request.GET.get('q', '').strip()
    min_price = request.GET.get('min')
    max_price = request.GET.get('max')
    available_only = request.GET.get('available')

    apartments = Apartment.objects.all()

    if query:
        apartments = apartments.filter(location__icontains=query)

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
        'min_price': min_price,
        'max_price': max_price,
        'available_only': available_only,
    })


def apartment_detail(request, id):
    apartment = get_object_or_404(Apartment, id=id)
    error = None
    success = None

    if request.method == 'POST':
        name = request.POST.get('name')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')

        overlap = Booking.objects.filter(
            apartment=apartment,
            check_in__lt=check_out,
            check_out__gt=check_in
        ).exclude(status='cancelled').exists()

        if overlap:
            error = "Selected dates are already booked."
        else:
            Booking.objects.create(
                apartment=apartment,
                name=name,
                check_in=check_in,
                check_out=check_out
            )
            success = "Booking request sent successfully."

    bookings = Booking.objects.filter(apartment=apartment).order_by('check_in')

    today = date.today()
    first_day = today.replace(day=1)

    if first_day.month == 12:
        next_month = first_day.replace(year=first_day.year + 1, month=1, day=1)
    else:
        next_month = first_day.replace(month=first_day.month + 1, day=1)

    last_day = next_month - timedelta(days=1)
    num_days = last_day.day

    booked_days = {}

    for booking in bookings:
        current = max(booking.check_in, first_day)
        end = min(booking.check_out, last_day)

        while current <= end:
            booked_days[current.day] = booking.status
            current += timedelta(days=1)

    calendar_days = []
    for day in range(1, num_days + 1):
        status = booked_days.get(day)
        calendar_days.append({
            'day': day,
            'status': status
        })

    return render(request, 'properties/apartment_detail.html', {
        'apartment': apartment,
        'error': error,
        'success': success,
        'bookings': bookings,
        'calendar_days': calendar_days,
        'month_name': first_day.strftime('%B %Y'),
    })


def about(request):
    return render(request, 'properties/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        Inquiry.objects.create(
            name=name,
            message=message
        )

        return render(request, 'properties/contact.html', {
            'success': True,
            'name': name
        })

    return render(request, 'properties/contact.html')


def calendar_view(request):
    bookings = Booking.objects.select_related('apartment').order_by('check_in')
    return render(request, 'properties/calendar.html', {
        'bookings': bookings
    })