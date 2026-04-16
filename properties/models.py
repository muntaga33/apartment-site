from django.db import models


class Apartment(models.Model):
    PRICE_TYPE_CHOICES = [
        ('day', 'Per Day'),
        ('month', 'Per Month'),
    ]

    CURRENCY_CHOICES = [
        ('GMD', 'Dalasi'),
        ('USD', 'USD'),
        ('EUR', 'Euro'),
    ]

    PROPERTY_TYPE_CHOICES = [
        ('studio', 'Studio'),
        ('apartment', 'Apartment'),
        ('house', 'House'),
    ]

    FURNISHING_CHOICES = [
        ('furnished', 'Furnished'),
        ('unfurnished', 'Unfurnished'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    phone = models.CharField(max_length=20, default='2200000000')
    price = models.IntegerField()
    price_type = models.CharField(max_length=10, choices=PRICE_TYPE_CHOICES)
    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICES, default='GMD')
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, default='apartment')
    furnishing = models.CharField(max_length=20, choices=FURNISHING_CHOICES, default='furnished')
    bedrooms = models.IntegerField(default=1)
    location = models.CharField(max_length=200)
    map_link = models.URLField(blank=True, null=True)

    # MAIN IMAGE
    image = models.ImageField(upload_to='apartments/', blank=True, null=True)

    available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# 👉 NEW: multiple images
class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='apartments/gallery/')

    def __str__(self):
        return f"Image for {self.apartment.title}"


class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.apartment.title}"