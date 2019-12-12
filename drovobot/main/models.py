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


class Ad(CoreModel):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='ads')
    active = models.BooleanField(default=True)
    text = models.CharField(max_length=200, null=True)

    def __str__(self):
        return 'Куплю дрова {} {} {}'.format(self.owner.phone, self.owner.viber_name, self.active)

    @property
    def to_text(self)
        return 'Куплю дрова {} {}'.format(self.owner.phone, self.owner.viber_name)



