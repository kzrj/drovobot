# -*- coding: utf-8 -*-
from celery import shared_task

from main.models import Ad


@shared_task
def deactivate_ad(ad_pk):
    print("OOOOOOOOOPAPAPPAPAAAAAAAAAAAAAAAAAAAAAAAAPAPAP@!!!!!!!!!!!!!!")
    ad = Ad.objects.filter(pk=ad_pk).first()
    if ad:
    	ad.deactivate
    else:
    	pass

    print("DEACTIVATE")
    return 'HUIIIIIIILAAAAAAAAAAAAAAAA'
