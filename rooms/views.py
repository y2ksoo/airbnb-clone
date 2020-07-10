from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.http import Http404
from django.shortcuts import render, redirect
from . import models


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

