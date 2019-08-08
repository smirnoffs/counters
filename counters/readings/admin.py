from django.contrib import admin
from .models import Counter, Value, Readings



class ValueAdmin(admin.ModelAdmin):
    search_fields = [
        "counter__identifier",
        "counter__owner__name",
        "counter__owner__surname",
        "counter__owner__patronymic",
        "counter__owner__address__city",
        "counter__owner__address__street",
        "counter__owner__address__house_number",
    ]

    fields = [
        "counter", 
        "value", 
    ]


class CounterAdmin(admin.ModelAdmin):
    list_display = ("counter_id", "region", "city", "owner")


class ReadingsAdmin(CounterAdmin):
    verbose_name = "Поиск"
    search_fields = [
        "counter__counter_id", "counter__region", "counter__owner", "counter__city", "counter__street"
    ]
    fieldsets = (
        ("Показання", {
            "fields": ("value",),
        }),
    )


# class ValueAdmin(admin.ModelAdmin):
#     list_display = ("counter_id", "value")
#     search_fields = [
#         "counter__counter_id", "counter__region", "counter__owner", "counter__city", "counter__street"
#     ]




admin.site.register(Counter, CounterAdmin)
admin.site.register(Readings, ReadingsAdmin)
admin.site.register(Value)
