'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2024-02-21 02:03:13
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-02-25 01:03:29
FilePath: \django1\crepes\blog\views.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import redirect
from datetime import datetime
# Create your views here.

def home(request):
    # text='''<h1>Bienvenue sur mon blog</h1>
    # <p>je teste seulement les vues sur django</p>'''
    date_c=datetime.now().strftime("%H:%M:%S")
    return render(request,'blog/index.html',{'date_c':date_c})

def confection(request):
    return redirect('confection')

def liste(request):
    return render(request,'blog/liste.html')

def inscription(request):
    return render(request,'blog/inscription.html')

# def login(request):
#     if len(request.POST)>0:
#         if 'nom' not in request.POST:
#             error="veuillez bien remplir"
#             return render(request,'blog/index.html')
    

