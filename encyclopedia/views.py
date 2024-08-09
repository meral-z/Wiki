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
                return entry(request=request,title=ent)
            elif search in ent.lower():
                 found.append(ent)
         if not found:
             return render(request, "encyclopedia/error.html")
         return render(request, "encyclopedia/index.html", {
        "entries": found
    })
     
class Pageform(forms.Form):
     title = forms.CharField(label='Title',max_length=100)
     content = forms.CharField(label='Content', widget= forms.Textarea(attrs={'placeholder': 'Enter markdown content here....','style': 'width: 70%; height: 100px;'}))
     
     
def newpage(request):
     if request.method == 'POST':
         form = Pageform(request.POST)
         entries = util.list_entries()
         if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            if any(title.lower()==entry.lower() for entry in entries):
                 error = "Title already exists"
                 return render(request, "encyclopedia/newpage.html",{'error': error,'form': Pageform()})
            
            util.save_entry(title=title,content=content)
            return entry(request=request,title=title)

     return render(request, 'encyclopedia/newpage.html', {'form': Pageform()})