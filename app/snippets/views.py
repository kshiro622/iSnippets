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
        if len(request.POST['snippet_title']) > 0:
            Snippet.objects.filter(id=snippet_id).update(
                title=request.POST['snippet_title']
            )
        if len(request.POST['snippet_lang']) > 0:
            Snippet.objects.filter(id=snippet_id).update(
                language=request.POST['snippet_lang']
            )
        if len(request.POST['snippet_desc']) > 0:
            Snippet.objects.filter(id=snippet_id).update(
                description=request.POST['snippet_desc']
            )
        if len(request.POST['snippet']) > 0:
            Snippet.objects.filter(id=snippet_id).update(
                snippet=request.POST['snippet']
            )
        return redirect('/home/')

def delete(request, snippet_id):
    Snippet(id = snippet_id).delete()
    return HttpResponse({'success'})
        
# def update(request, snippet_id):
    