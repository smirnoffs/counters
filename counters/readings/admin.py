from django import forms
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


class ReadingsForm(forms.ModelForm):
    class Meta:
        model = Counter
        fields = '__all__'

    current_value = forms.IntegerField(label="Текущее значение")
    
    def save(self, commit=True):
        current_value = self.cleaned_data.get("current_value", None)
        last_value = self.instance.value
        if current_value and (last_value is None or current_value > last_value.value) :
            Value.objects.create(value=current_value, counter=self.instance)
        return super().save(commit=commit)


class ReadingsAdmin(CounterAdmin):
    verbose_name = "Поиск"
    search_fields = [
        "counter_id", "region", "owner", "city", "street"
    ]
    readonly_fields = ('counter_id','last_value',)
    fields =("counter_id", "last_value", "current_value") 
    def last_value(self, object):
        return object.value_set.last()
    last_value.short_description = "Последнее показание"
    form = ReadingsForm

admin.site.register(Counter, CounterAdmin)
admin.site.register(Readings, ReadingsAdmin)
admin.site.register(Value)
