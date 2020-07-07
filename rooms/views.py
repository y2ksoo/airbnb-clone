from django.views.generic import ListView
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 5
    paginate_orphans = 2
    ordering = "created"

