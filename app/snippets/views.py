from django.shortcuts import render

# Create your views here.

# route to add snippets
def add(request):
    return render(request, 'snippets/add_snippets.html', {
        'data': 'Form to add snippets goes here'
    })

#route to view and manage snippets
def manage(request):
    return render(request, 'snippets/manage_snippets.html', {
        'data': 'All snippets can be viewed and managed here'
    })