# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


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
    phone = models.CharField(max_length=11, null=True)
    banned = models.BooleanField(default=False)

    subscribed = models.BooleanField(default=False)

    active = models.BooleanField(default=True)

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

    def unsubscribe(self):
        self.subscribed = False
        self.save()

    def subscribe(self):
        self.subscribed = True
        self.save()

    def deactivate(self):
        self.active = False
        self.save()

    def activate(self):
        if not self.active:
            self.active = True
            self.save()


class AdManager(models.Manager):
    def create_all_in_one(self):
        text = ''
        for ad in self.get_queryset().filter(active=True):
            text = text + str(ad) + '\n' + '----------------' + '\n'
        return text


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

    objects = AdManager()

    class Meta:
        ordering = ('modified_at', )

    def __str__(self):
        return f'Куплю дрова {self.amount} {self.location} \nт. {self.owner.phone} \n{self.modified_at.strftime("%d-%b-%Y (%H:%M)")}'

    @property
    def to_text(self):
        return f'Куплю дрова {self.amount} {self.location} \nт. {self.owner.phone} \n{self.modified_at.strftime("%d-%b-%Y (%H:%M)")}'

    @property
    def activate(self):
        self.active = True
        self.save()

    @property
    def deactivate(self):
        self.active = False
        self.save()

    def validate_location(self, location):
        if location in [l[0] for l in self.LOCATIONS]:
            return True
        return False

    def validate_amount(self, amount):
        if amount in [a[0] for a in self.AMOUNTS]:
            return True
        return False


