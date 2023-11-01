from django.contrib import admin

from .models import (
    Country,
    City,
    Flight,
    Hotel,
    Tour,
    Client,
    Sale,
)


@admin.register(
    Country,
    City,
    Flight,
    Hotel,
    Tour,
    Client,
    Sale,
)
class TravelAdmin(admin.ModelAdmin):
    pass
