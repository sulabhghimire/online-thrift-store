from django.contrib import admin

from .models import Category, AdvertiseBuy, AdvertiseSell

admin.site.register(Category)
admin.site.register(AdvertiseBuy)
admin.site.register(AdvertiseSell)