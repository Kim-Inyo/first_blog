from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='articledetail'),
    path('friends/', views.friends, name='friends'),
    path('register/', views.signup, name='signup'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('post-creation/', AddPostView.as_view(), name='post-creation')
]