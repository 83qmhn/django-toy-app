from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from .models import Plant, PlantCalendar
from .forms import PlantForm, PlantRecordForm

# Create your views here.https://docs.djangoproject.com/en/5.1/topics/http/views/


def index(request):
    return render(request, "plant_calendar/index.html")


def plant_table(request):
    planted_plants = PlantCalendar.objects.filter(
        plant_date__lte=timezone.now()
    ).order_by("plant_date")
    return render(
        request, "plant_calendar/plant_table.html", {"planted_plants": planted_plants}
    )


# TODO: how to use pk of plant_record to get the pk of plant
def get_plant(request, pk):
    record = get_object_or_404(PlantCalendar, pk=pk)
    plant_name = record.plant_name
    plant = Plant.objects.get(name=plant_name)
    return render(request, "plant_calendar/plant_detail.html", {"plant": plant})


def new_plant(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    return render(request, "plant_calendar/plant_detail.html", {"plant": plant})


def add_plant(request):
    if request.method == "POST":
        form = PlantForm(request.POST)
        if form.is_valid():
            plant = form.save()
            plant.save()
            pk = plant.pk
            return HttpResponse(
                status=204,
                headers={
                    "HX-Trigger": "plantAdded",
                    "HX-Redirect": ""
                },
            )
    else:
        form = PlantForm()
        return render(request, "plant_calendar/add_plant.html", {"form": form})


def add_record(request):
    if request.method == "POST":
        form = PlantRecordForm(request.POST)
        if form.is_valid():
            plant = form.save()
            plant.save()
            return HttpResponse(
                status=204,
                headers={"HX-Trigger": "plantRecordAdded", "HX-Redirect": ""},
            )
    else:
        form = PlantRecordForm()
    return render(request, "plant_calendar/add_plant_record.html", {"form": form})


def plant_record(request, pk):
    record = get_object_or_404(PlantCalendar, pk=pk)
    if request.method == "POST":
        form = PlantRecordForm(
            request.POST, instance=record
        )  # remember adding the instance!!!
        if form.is_valid():
            record.save()
            # return an empty response with the appropriate status code
            # 'plantTableChanged' is the event name that triggers table content to update
            return HttpResponse(status=204, headers={"HX-Trigger": "plantTableChanged"})
    else:
        form = PlantRecordForm(instance=record)
    return render(request, "plant_calendar/edit_plant_record.html", {"form": form})


def delete_plant_record(request, pk):
    # record = get_object_or_404(PlantCalendar, pk=pk)
    record = PlantCalendar.objects.get(pk=pk)
    record.delete()
    return HttpResponse(status=204, headers={"HX-Trigger": "plantRecordDeleted"})
