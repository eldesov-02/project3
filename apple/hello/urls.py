from django.urls import path
from . import views
from .views import RegisterUser, LoginUser, logout_user
from .views import *



urlpatterns =[
    path('', views.index, name='/'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='addpage'),

    path('send/', EmailAttachementView.as_view(), name='email'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    # path('send/', EmailPostView.as_view(), name='email'),
    # path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail')
    # path('<int:pk>', views.NewsUpdateView.as_view(), name='news-update')

]