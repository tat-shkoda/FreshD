from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('programs', views.programs, name='programs'),
    path(r'programs/(?P<pk>\d+)', views.show, name='program.show'),
]
