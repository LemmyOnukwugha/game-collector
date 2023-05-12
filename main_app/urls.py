from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name='index'),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:game_id>/', views.games_detail, name='detail'),
    path('games/<int:game_id>/add_review/', views.add_review, name='add_review'),
    path('games/<int:pk>/update', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete', views.GameDelete.as_view(), name='games_delete'),
    path('collectibles/', views.CollectibleList.as_view(), name='collectibles_index'),
    path('collectibles/<int:pk>/', views.CollectibleDetail.as_view(), name='collectibles_detail'),
    path('collectibles/create/', views.CollectibleCreate.as_view(), name='collectibles_create'),
    path('collectibles/<int:pk>/update/', views.CollectibleUpdate.as_view(), name='collectibles_update'),
    path('collectibles/<int:pk>/delete/', views.CollectibleDelete.as_view(), name='collectibles_delete'),
]