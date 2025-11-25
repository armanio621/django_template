from django.shortcuts import render

def home(request):
    context = {
        'title': 'Arman Website',
        'welcome_text': 'Welcome to Arman\'s Django Template Demo!'
    }
    return render(request, 'arman/home.html', context)
