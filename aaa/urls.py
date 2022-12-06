from django.urls import path

from aaa import views

urlpatterns = [
    path('', views.index),
    path('ad/', views.AdsListView.as_view()),
    path('ad/<int:pk>/', views.AdsDetailView.as_view()),
    path('ad/create/', views.AdsCreateView.as_view()),
    path('ad/<int:pk>/update/', views.AdsUpdateView.as_view()),
    path('ad/<int:pk>/delete/', views.AdsDeleteView.as_view()),
    path('user/', views.UserView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('user/create/', views.UserCreateView.as_view()),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', views.UserDeleteView.as_view()),
    # path('user/else/', views.UserElseView.as_view()),   # Выводит кол-во объявлений автора
    path('ad/<int:pk>/upload_image/', views.AdUploadImageView.as_view()),
    path('selections/', views.SelectionView.as_view()),
    path('selections/<int:pk>/', views.SelectionDetailView.as_view()),
    path('selections/create/', views.SelectionCreateView.as_view()),
    path('selections/<int:pk>/update/', views.SelectionUpdateView.as_view()),
    path('selections/<int:pk>/del/', views.SelectionDeleteView.as_view()),
]


# handler404 = pageNotFound
