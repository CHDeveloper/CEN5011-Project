from .views import CreateAccountView, ProfileView
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create_account/', CreateAccountView.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('personal/', ProfileView.as_view()),

]