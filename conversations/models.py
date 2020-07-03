from django.db import models
from core import models as core_models


class Converstion(core_models.TimeStampedModel):

    """ Converstion Model Definition """

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):

    """ Message Model Definition """

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    converstion = models.ForeignKey("Converstion", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.message}"

