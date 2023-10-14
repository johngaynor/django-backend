from django.urls import path
from . import views
# map URL's to functions

# url configuration, always end routes with '/'
urlpatterns = [
    path('testpost/', views.test_post),
    path('testget/', views.test_get),
    path('csrf/', views.csrf),
    path('init/', views.init_upload)
]
