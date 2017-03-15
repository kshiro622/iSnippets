from django.shortcuts import render
from django.http import request
from .models import Snippet
from django.shortcuts import redirect
from django.http import HttpResponse

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
def home(request):
    snippets = Snippet.objects.all()

    context = {
        'snippets': snippets
    }
    return render(request, 'snippets/manage_snippets.html', context)

def delete(request, snippet_id):
    Snippet(id = snippet_id).delete()
    return redirect('/home/')
        
        