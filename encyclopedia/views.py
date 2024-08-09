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
    "title":title.lower()})

import random

def rand(request):
    #get entries
    entries = util.list_entries()
    
    # generate random number for legnth of entries list
    index = random.randint(0,len(entries) - 1)

    #extract the random entry
    title = entries[index]
    
    return render(request, "encyclopedia/entry.html", {
    "entry": util.convert(util.get_entry(title)),
    "title": title })

def search(request):
     if request.method == "POST":
         search = request.POST.get('search').lower()
         entries = util.list_entries()
         found = []
         for ent in entries:
            if ent.lower() == search:
                return render(request, "encyclopedia/entry.html", {
    "entry": util.convert(util.get_entry(ent)),
    "title":ent})
            elif search in ent.lower():
                 found.append(ent)
         if not found:
             return render(request, "encyclopedia/error.html")
         return render(request, "encyclopedia/index.html", {
        "entries": found
    })
                
                 
     
    

     


              

