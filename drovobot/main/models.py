# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

import main.tasks as celery_tasks


class CoreModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomerManager(models.Manager):
    pass


class Customer(CoreModel):
    viber_id = models.CharField(max_length=100)
    viber_name = models.CharField(max_length=100)
    viber_avatar = models.URLField(max_length=300, null=True)
    last_seen_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=11)
    banned = models.BooleanField(default=False)

    objects = CustomerManager()

    def __str__(self):
        return self.viber_name

    @property
    def get_ad(self):
        return self.ads.all().first()

    def validate_phone(self, phone):
        # length
        if len(phone) == 11 and \
          phone.isdigit() and \
          phone[:2] == '89' and \
          not Customer.objects.filter(phone=phone).first():
            return True

        return False


class Ad(CoreModel):
    LOCATIONS = [
        ('Левый берег', 'Левый берег'),
        ('Советский район','Советский район'),
        ('Железнодорожный район', 'Железнодорожный район'),
        ('Октябрьский район', 'Октябрьский район'),
        ('Вахмистрово','Вахмистрово'),
    ]

    AMOUNTS = [
        ('от 2 до 4 т.р.', 'от 2 до 4 т.р.'),
        ('от 4 до 6 т.р.', 'от 4 до 6 т.р.'),
        ('от 6 до 8 т.р.', 'от 6 до 8 т.р.'),
        ('от 8 т.р. и выше', 'от 8 т.р. и выше') 
    ]

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
        celery_tasks.deactivate_ad.apply_async(
                    args=[self, ],
                    # eta=timezone.now() + datetime.timedelta(seconds=15),
                    countdown=30
                    # countdown=86400 # 24h
                )
        self.save()

    @property
    def deactivate(self):
        self.active = False
        print("DEACTIVATE MODEL")
        self.save()

    def validate_location(self, location):
        if location in [l[0] for l in self.LOCATIONS]:
            return True
        return False

    def validate_amount(self, amount):
        if amount in [a[0] for a in self.AMOUNTS]:
            return True
        return False


