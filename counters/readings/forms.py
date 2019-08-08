from django import forms
from counters.readings.models import Counter

city_choices = (
    ('Город', 'city'),
    ('Село', 'village')
)


# class ApplicationForm(forms.Form):
#     gender = forms.ChoiceField(choices=city_choices, widget=forms.RadioSelect())


