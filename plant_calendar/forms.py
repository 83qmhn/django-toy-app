from django import forms

from .models import Plant, PlantCalendar
class DateInput(forms.DateInput):
    input_type = 'date'

class PlantForm(forms.ModelForm):

    class Meta:
        model = Plant
        fields = ('name', 'best_season_to_plant')


class PlantRecordForm(forms.ModelForm):

    class Meta:
        model = PlantCalendar
        fields = ('plant_name', 'plant_date', 'fertiliser', 'plant_spot_sunlight_condition', 'harvest_date')
        widgets={
            'plant_date': DateInput(),
            "harvest_date": DateInput()
        }