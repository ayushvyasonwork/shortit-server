from django.urls import path
from . import views
urlpatterns = [
    path('api/create/', views.create_short, name='create_short'),
    path('r/<slug:slug>/', views.redirect_view, name='redirect_view'),
]
