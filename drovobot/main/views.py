# -*- coding: utf-8 -*-
from django.shortcuts import render

def links_page(request, poll_id):
    return render(request, 'templates/links_page.html')