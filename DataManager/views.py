from django.shortcuts import render
from django.http import HttpResponse


# Index
def index(request):
    # data = {"header": "Hello Django", "message": "Welcome to Python"}
    # return render(request, "index.html", context=data)
    return render(request, 'index.html', {
            'title': 'Главная',
        })

def programList(request):
    programs = [
        {
            'id': 1,
            'name': 'name1',
            'description': 'description1',
        },
        {
            'id': 2,
            'name': 'Name2',
            'description': 'description2',
        },
    ]

    return render(request, 'DataManager/program_list.html', {
        'title': 'Список программ',
        'programs': programs,
    })