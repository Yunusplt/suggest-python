from django.urls import path
from .views import search_page, api_search

urlpatterns = [
    path("", search_page, name="home"), 
    path("api/search/", api_search, name="api_search"), 
]
