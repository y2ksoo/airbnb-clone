from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom user model """

    GENDER_MALE = "male"  # male은 DB에 저장되는 값
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),  # Male은 입력값, 웹페이지 표시되는 값
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=10, blank=True)
    superhost = models.BooleanField(default=False)

    def __str__(self):
        return self.username
