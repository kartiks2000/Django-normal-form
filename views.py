# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from formapp import forms
# Create your views here.

def index(request):
    myd = {"mytxt" : "this is Kartik..."}
    return render(request,'index1.html',context=myd)

def fm(request):
    form = forms.Formname()
    return render(request,'index2.html',{'form' : form})

