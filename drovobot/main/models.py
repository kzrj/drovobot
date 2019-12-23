# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class CoreModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Customer(CoreModel):
    viber_id = models.CharField(max_length=100)
    viber_name = models.CharField(max_length=100)
    viber_avatar = models.URLField(max_length=300, null=True)
    last_seen_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.viber_name

    @property
    def get_ad(self):
        return self.ads.all().first()


class Ad(CoreModel):
    LOCATIONS = [('Левый берег', 'Левый берег'), ('Советский район', 'Советский район'),
        ('Железнодорожный район', 'Железнодорожный район'), ('Октябрьский район', 'Октябрьский район'),
        ('Вахмистрово', 'Вахмистрово')]

    AMOUNTS = [('от 2 до 4 т.р.', 'от 2 до 4 т.р.'), ('от 4 до 6 т.р.', 'от 4 до 6 т.р.'),
        ('от 6 до 8 т.р.', 'от 6 до 8 т.р.'), ('от 8 т.р. и выше', 'от 8 т.р. и выше'),
        ('8/7', '8/7')]

    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='ads')
    active = models.BooleanField(default=True)
    location = models.CharField(max_length=200, null=True, choices=LOCATIONS)
    amount = models.CharField(max_length=200, null=True, choices=AMOUNTS)

    def __str__(self):
        return f'Куплю дрова {self.amount} {self.location} т. {self.owner.phone}'

    @property
    def to_text(self):
        return f'Куплю дрова {self.amount} {self.location} т. {self.owner.phone}'

    @property
    def activate(self):
        self.active = True
        self.save()


