from django.urls import path
from .views import AppView, set_api_key


urlpatterns = [
    path('test', AppView.as_view()),
    path('set_api_key', set_api_key),
]
