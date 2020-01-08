# -*- coding: utf-8 -*-
from celery import shared_task


@shared_task
def celery_deactivate_ad(subject, ctx, sender, receiver, template):
    print("OOOOOOOOOPAPAPPAPAAAAAAAAAAAAAAAAAAAAAAAAPAPAP@!!!!!!!!!!!!!!")

