from django.urls import path, include
from .views import index, MyFileView
app_name = 'mnistapp'

urlpatterns = [
    path('', index, name='home'),
    path('predict/',MyFileView.as_view()),
]

