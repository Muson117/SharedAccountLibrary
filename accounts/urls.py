from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:account_id>/', views.login, name='login'),
    path('<int:account_id>/newpass/', views.pass_change, name='pass_change'),
]
