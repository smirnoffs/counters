from django.contrib import admin
from .models import Counter, Address, Owners, Value


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
    search_fields = [
        "address__street"
    ]
    fieldsets = (
        ("Показання", {
            "fields": ('identifier',),
        }),
    )


admin.site.register(Counter, CounterAdmin)
admin.site.register(Address)
admin.site.register(Owners)
admin.site.register(Value, ValueAdmin)
