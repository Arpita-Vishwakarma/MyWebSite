from django.contrib import admin
from django.urls import path, include
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='Home'),
    path('thank_you/', views.thank_you, name='thank_you'),

]
