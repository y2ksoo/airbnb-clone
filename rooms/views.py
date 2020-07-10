from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models, forms


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 5
    paginate_orphans = 2
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDeatil Definition """

    model = models.Room


class SearchView(View):
    def get(self, request):
        country = request.GET.get("country")

        filter_args = {}

        if country:
            form = forms.SearchForm(request.GET)

            if form.is_valid():

                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

            if city != "Anywhere":
                filter_args["city__startswith"] = city

            filter_args["country"] = country

            if room_type is not None:
                filter_args["room_type"] = room_type

            if price is not None:
                filter_args["price__lte"] = price

            if guests is not None:
                filter_args["guest__gte"] = guests

            if bedrooms is not None:
                filter_args["bedrooms__gte"] = bedrooms

            if beds is not None:
                filter_args["beds__gte"] = beds

            if baths is not None:
                filter_args["baths__gte"] = baths

            if instant_book is True:
                filter_args["instant_book"] = instant_book

            if superhost is True:
                filter_args["host__superhost"] = superhost

            for amenity in amenities:
                filter_args["amenity"] = amenity

            for facility in facilities:
                filter_args["facility"] = facility

            qs = models.Room.objects.filter(**filter_args).order_by("-created")

            paginator = Paginator(qs, 10, orphans=5)
            page = request.GET.get("page", 1)
            rooms = paginator.get_page(page)

            return render(request, "rooms/search.html", {"form": form, "rooms": rooms})

        else:
            form = forms.SearchForm()

        return render(request, "rooms/search.html", {"form": form})
