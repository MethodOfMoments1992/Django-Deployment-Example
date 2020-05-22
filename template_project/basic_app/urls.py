from django.urls import path
from basic_app import views

# TEMPLATE TAGGING (Django will look for the variable called app_name as a directory)
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other')
]
