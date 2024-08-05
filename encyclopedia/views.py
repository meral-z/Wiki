from django.shortcuts import render, redirect

from . import util
from django import forms

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if not util.get_entry(title):
            return render(request, "encyclopedia/error.html")
    
    return render(request, "encyclopedia/entry.html", {
    "entry": util.convert(util.get_entry(title)),
    "title":title})

import random

def random_entry(request):
     #get entries
     entries = util.list_entries()
     
     # generate random number for legnth of entries list
     index = random.randint(0,len(entries) - 1)

     #extract the random entry
     entry = entries[index]
     
     return render(request, "encyclopedia/entry.html", {
     "entry": util.convert(entry)})
    

     


              

