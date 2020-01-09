# -*- coding: utf-8 -*-
from celery import shared_task


@shared_task
def deactivate_ad(ad):
    print("OOOOOOOOOPAPAPPAPAAAAAAAAAAAAAAAAAAAAAAAAPAPAP@!!!!!!!!!!!!!!")
    ad.deactivate
    print("DEACTIVATE")
    return 'HUIIIIIIILAAAAAAAAAAAAAAAA'
