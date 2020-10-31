from django.contrib import admin
from django.urls import path, include # new
from .views import HomePageView, SearchResultsView


urlpatterns = [
    # path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
]