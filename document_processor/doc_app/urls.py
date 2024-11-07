from django.urls import path
from . import views
# from .views import voices_view

urlpatterns = [
    path('', views.upload_document, name='upload_document'),
  
]
