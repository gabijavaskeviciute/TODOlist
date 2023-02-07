from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uzduotys/', views.UzduotisListView.as_view(), name='uzduotis_list'),
    path('uzduotys/<int:pk>', views.UzduotisDetailView.as_view(), name='uzduotis_detail'),
    path('user_uzduotis/', views.UserUzduotysListView.as_view(), name='user_uzduotis'),
    path('user_uzduotis/new', views.UserUzduotisCreateView.as_view(), name='user_uzduotis_new'),
    path('user_uzduotis/<int:pk>/update', views.UserUzduotisUpdateView.as_view(), name='user_uzduotis_update'),
    path('user_uzduotis/<int:pk>/delete', views.UserUzduotisDeleteView.as_view(), name='user_uzduotis_delete'),
]