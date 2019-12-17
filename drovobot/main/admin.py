from django.contrib import admin

from main.models import Customer, Ad


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Customer._meta.fields]


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Ad._meta.fields]