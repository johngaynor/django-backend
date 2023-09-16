from django.urls import path
from . import views
# map URL's to functions

# url configuration, always end routes with '/'
urlpatterns = [
    path('', views.home, name='home'),  # root path URL
    path('hello/', views.say_hello)
]
