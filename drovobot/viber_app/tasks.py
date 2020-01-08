# -*- coding: utf-8 -*-
from celery import shared_task

from .models import Ad

@shared_task
def deactivate_ad():
    print("OOOOOOOOOPAPAPPAPAAAAAAAAAAAAAAAAAAAAAAAAPAPAP@!!!!!!!!!!!!!!")
    # ad.deactivate
    print("DEACTIVATE")

