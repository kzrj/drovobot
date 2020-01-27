# -*- coding: utf-8 -*-
from django.shortcuts import render

def links_page(request):
    return render(request, 'links_page.html')