from django.urls import path
from API import views

urlpatterns = [
    path('db/', views.DbFillView.as_view(), name='api-db-fill'),
    path('books/', views.BooksListView.as_view(), name='api-books'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='api-book-detail'),
    path('valves/', views.ValvesListCreate.as_view(), name='api-valves'),
    path('valves/<int:pk>/', views.ValvesRetrieveUpdateDestroy.as_view(), name='api-valve'),
    path('pumps/', views.PumpsListCreate.as_view(), name='api-pumps'),
    path('pumps/<int:pk>/', views.PumpsRetrieveUpdateDestroy.as_view(), name='api-pump'),
]
