from django.shortcuts import render, redirect
from .models import Snippet
from django.http import HttpResponse, request

# Create your views here.

# route to add snippets
def add(request):
    if request.method == 'POST':

        Snippet(
            title=request.POST['title'],
            language=request.POST['language'],
            snippet=request.POST['snippet'],
            description=request.POST['description']
        ).save()

    return render(request, 'snippets/add_snippets.html', {})

#route to view and manage snippets
def home(request, snippet_id):
    if request.method == 'GET':
        snippets = Snippet.objects.all()

        context = {
            'snippets': snippets
        }
        return render(request, 'snippets/manage_snippets.html', context)
    
    elif request.method == 'POST':
        Snippet.objects.filter(id=snippet_id).update(
            title=request.POST['snippet_title'],
            language=request.POST['snippet_lang'],
            description=request.POST['snippet_desc'],
            snippet=request.POST['snippet']
        )
        return redirect('/home/')

def delete(request, snippet_id):
    Snippet(id = snippet_id).delete()
    return HttpResponse({'success'})
        
# def update(request, snippet_id):
    